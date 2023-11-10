


from django import forms

from uploadApp.models import Uploads


class uplodForms(forms.ModelForm):
    
    class Meta:
        model = Uploads
        fields = '__all__'
