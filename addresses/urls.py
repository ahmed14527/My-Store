from django.urls import path
from .views import AddressListCreateView, AddressRetrieveUpdateDestroyView

app_name = 'addresses'

urlpatterns = [
    path('', AddressListCreateView.as_view(), name='address_list_create'),
    path('<int:pk>/', AddressRetrieveUpdateDestroyView.as_view(), name='address_detail'),
]