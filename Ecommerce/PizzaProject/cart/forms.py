
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]

# types of fields: boolean,typedchoice,multipletext etc.
# they all have default types eg boolean has boolean value
# in order ot change its datatype intput we use widget
# since by default boolean value is true for forms
#we have to manually set it to true.(if we are taking both true and false as values)
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
