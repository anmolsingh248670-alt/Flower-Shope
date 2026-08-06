from django import forms
from .models import add_product

class add_projuct_Forms(forms.ModelForm):

    class Meta:
        model = add_product
        fields = '__all__'