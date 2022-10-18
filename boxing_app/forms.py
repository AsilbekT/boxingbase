from django.forms import ModelForm
from .models import Boxer

# Create the form class.
class BoxerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fio'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['nomeri'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['turar_joyi'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['viloyat'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['trener_1'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['trener_2'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['trener_3'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['trener_4'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['trener_5'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['boxer_rasmi'].widget.attrs.update({'class': 'form__inputs'})
        self.fields['passport_pdf'].widget.attrs.update({'class': 'form__inputs'})

    class Meta:
        model = Boxer
        fields = [
            'fio', 
            'nomeri', 
            'turar_joyi', 
            'viloyat', 
            'trener_1', 
            'trener_2', 
            'trener_3', 
            'trener_4', 
            'trener_5', 
            'boxer_rasmi',
            'passport_pdf'
            ]