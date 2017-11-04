from django import forms
from django.forms import SelectDateWidget, RadioSelect

from cart.models import Order, ORDER_STATUS_CHOICES

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=True, initial=1, min_value = 1, max_value=21, label="Количество")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_status', 'name', 'number', 'district', 'adress', 'adress_number', 'apartment', 'entrance', 'floor',
                  'time_order', 'date_order']

        widgets = {
            'date_order': SelectDateWidget,
            'payment_status': RadioSelect
        }

class OrderChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status', 'courier']