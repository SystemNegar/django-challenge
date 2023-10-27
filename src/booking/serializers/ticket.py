from rest_framework.serializers import ModelSerializer

from booking.models import Ticket


class TicketSerializer(ModelSerializer):
    """
    Serializer for the 'Ticket' model
    """

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('invoice', 'match', 'section', 'status', 'created_at', 'updated_at')

    def to_representation(self, obj):
        data = super(TicketSerializer, self).to_representation(obj)
        data['status'] = obj.get_status_display()
        return data
