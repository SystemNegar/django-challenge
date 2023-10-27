from rest_framework.serializers import ModelSerializer

from booking.models import Invoice


class InvoiceSerializer(ModelSerializer):
    """
    Serializer for the 'Invoice' model
    """

    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, obj):
        data = super(InvoiceSerializer, self).to_representation(obj)
        data['status'] = obj.get_status_display()
        data['total_amount'] = obj.get_total_amount
        return data
