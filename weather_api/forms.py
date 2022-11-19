from django import forms

class CityForm(forms.Form):
    miejsce = forms.CharField(
        max_length=25, 
        label='Miejsce', 
        widget=forms.TextInput(attrs={
            'placeholder': 'Wpisz swoje miejsce..',
            'size': '60',
            'class': "form-control",
            }),
        )