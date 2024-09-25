from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

            # for boolean fields:
            if field.name == 'isOutside':
                field.field.widget.attrs["class"] = "form-check-input"

    class Meta:
        model = Flight
        exclude = ['creator', ]
        # ne sum siugren sto e ova ama neka stoi
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
