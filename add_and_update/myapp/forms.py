from .models import shop
from django import forms





class ShopForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = ["name", "desc", "img", "price"]
