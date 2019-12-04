from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'usuario',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'usuario' : 'Usuario',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
