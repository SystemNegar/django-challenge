from selling.apps.seat.models import BookSeat


class BookSeatService:
    @classmethod
    def create_reservation(cls, user, seat_id):
        try:
            BookSeat.objects.create(user=user, seat_id=seat_id, reserved=True)
        except Exception as e:
            raise e
