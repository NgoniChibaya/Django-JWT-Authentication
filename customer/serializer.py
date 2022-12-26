from rest_flex_fields import FlexFieldsModelSerializer
from customer.models import Customer

class CustomerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name','last_name')
