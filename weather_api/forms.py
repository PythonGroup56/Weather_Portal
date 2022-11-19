from django import forms


class CityForm(forms.Form):
    place = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz swoje miejsce..",
                "size": "85",
                "class": "form-control",
            }
        ),
        label="",
    )
