from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    def clean(self):
        # Optional: Add custom validation logic if needed
        cleaned_data = super().clean()
        # Example: Validate that the quantity is a positive number
        quantity = cleaned_data.get("quantity")
        if quantity is not None and quantity < 1:
            self.add_error('quantity', 'Quantity must be a positive number')
        return cleaned_data

