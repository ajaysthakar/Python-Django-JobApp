from django import forms
from django.utils.translation import gettext_lazy as _
from Subscribe.models import Subscribe

"""
def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Invalid first name ")
    return value 

class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=200,validators=[validate_comma,])
    last_name = forms.CharField(max_length=200,validators=[validate_comma])
    email = forms.EmailField(max_length=200)

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError("Invalid first name ")
    #     return data 
  
"""
  
#optional to above form if we are creating form for table define in models
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'#['first_name','last_name','email']
        #exclude = ('first_name',)  #excluding amny field from the models while creating form 
        labels={
            'first_name':'Enter First Name :',
            'last_name':'Enter Last Name :',
            'email':'Enter Email Address:'
        }
        help_texts={'first_name':_('enter character only')}
        error_messages={
            'first_name':{
                'required':'You can not move forward without First name'
            },
            'Last_name':{
                'required':'You can not move forward without Last name'
            }
        }
