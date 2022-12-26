from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer
from customer.serializer import CustomerSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class CustomerViewSet(ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]