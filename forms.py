from django import forms
from.models import item

class ItemForm(forms.ModelForm):
    class Meta:
        model= item
        fields= ['item_name','item_desc','item_price','item_image']