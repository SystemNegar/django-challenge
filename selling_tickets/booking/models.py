from django.db import models, transaction
import uuid

# each stadium is consist of defining statdium and its places and the nuumber of row and seats
# in each place, so in adding stadium action we should define all these models (Stadium, StadiumPlace, PlaceSeats)
class Stadium(models.Model):
    name = models.CharField(max_length=50, verbose_name='Stadium Name')
    city = models.CharField(max_length=50, blank=True, verbose_name='Stadium City')
    address = models.TextField(verbose_name='Stadium Address')

    def __str__(self) -> str:
        return self.name

class StadiumPlace(models.Model):
    """
    each stadium has multiple places such as vip, north , south and ...
    in this model we define these palces and number of rows in each place
    """
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=50, verbose_name='Place Name', unique=True)
    number_of_rows = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return ("stadium: %s place: %s") % (self.stadium, self.name)


class PlaceSeats(models.Model):
    """
    each place in stadium has muultiple rows and each row has different number of saets
    so we define this model to define this feature
    """
    place = models.ForeignKey('StadiumPlace', on_delete=models.CASCADE, related_name='place_seats')
    row_number = models.IntegerField()
    number_of_seats_per_row = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return ("%s row_number: %s") % (self.place, self.row_number) 

    class Meta:
        unique_together = ['place', 'row_number']

# in definattion of matches, we need to add teams too, so for adding a new match we should hav att least two teams

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Team Name', unique=True)

    def __str__(self) -> str:
        return self.name


class Match(models.Model):
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE, related_name='matches')
    host_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='host_team')
    guest_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='guest_team')
    start_time = models.DateTimeField()

    def __str__(self) -> str:
        return "%s VS %s, Date: %s" % (self.host_team, self.guest_team, self.start_time)

    class Meta:
        unique_together = ['stadium', 'start_time']


# by selecting first ticket , we create the invoice for that user
# invoice has many to many relation with ticket model
# so each invoice has multiple tickets and each ticket can assign to many invoice 
# before calling the payment method we change the state of tickets to reserved 
# at this moment nobody can buy those tickets anymore until payment is done
# reservation of selected tickets only occured that user going to pay the invoice amount

class Invoice(models.Model):
    START = 0 # creation of invoice
    IN_PROGGRESS = 1 # user is in payment section
    SUCCESS = 2 # payment is successfull
    FAILED = 3 # payment is faieled or canceled 
    INVOICE_STATUSES = [
        (START, 'START'),
        (IN_PROGGRESS, 'IN_PROGGRESS'),
        (SUCCESS, 'SUCCESS'),
        (FAILED, 'FAILED'),
    ]
    status = models.IntegerField(default=START, choices=INVOICE_STATUSES)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='reservations')
    creation_date = models.DateTimeField(auto_now_add=True)
    payment_date_time = models.DateTimeField(blank=True, null=True)
    payment_description = models.TextField(blank=True)
    payment_number = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return ("user: %s created_date: %s") % (self.user, self.creation_date)

    def set_in_progress(self):
        self.status = Invoice.IN_PROGGRESS
        self.save()

    def set_payment_number(self):
        self.payment_number = uuid.uuid4().hex[:10].upper()
        self.save()

# after we create Stadium and its places, we can add tickets for each seat in stadium accordiing to each match policy
# sometimes we can not define tickets for all of seats in stadium

class Ticket(models.Model):
    EMPTY = 'EMPTY' #first state of Tticket
    RESERVED = 'RESERVED' # user is in payment section and the tickets are reserved for that user
    SOLD = 'SOLD' # user pay the invoice amount successfully and get the reservation number
    STATUS_CHOICES = [
        (EMPTY, 'EMPTY'),
        (RESERVED, 'RESERVED'),
        (SOLD, 'SOLD'),
    ]
    match = models.ForeignKey('Match', on_delete=models.RESTRICT, related_name='tickets')
    stadium = models.ForeignKey('Stadium', on_delete=models.RESTRICT, related_name='tickets')
    status = models.CharField(default=EMPTY, choices=STATUS_CHOICES, max_length=8)
    last_update_time = models.DateTimeField(auto_now=True)
    place = models.ForeignKey('StadiumPlace', on_delete=models.CASCADE, related_name='tickets')
    row_number = models.PositiveSmallIntegerField()
    seat_number = models.PositiveSmallIntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    invoices = models.ManyToManyField(Invoice, blank=True, related_name='tickets')

    def __str__(self) -> str:
        return "%s, %s row: %s seat: %s" % (self.match, self.place, self.row_number, self.seat_number)

    class AlreadyReserved(Exception):
        pass

    def get_queryset(self):
        return self.__class__.objects.filter(id=self.id)

    def reserve_ticket(self):
        if self.status == Ticket.RESERVED: # if status of ticket is already reserved we raise an error
            raise Ticket.AlreadyReserved
        with transaction.atomic(): # the action of reservation of ticket is doing by transaction that nobody can get the rows concurrency 
            ticket = self.get_queryset().select_for_update().get()
            if ticket.status == Ticket.RESERVED:
                raise Ticket.AlreadyReserved
            self._reserve_ticket()

    def _reserve_ticket(self):
        self.status = Ticket.RESERVED
        self.save()

