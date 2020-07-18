from django import forms
from django.core import validators

#creating your own validators
'''
def check_for_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("Name needs to start with z")
'''
class FormName(forms.Form):
    name = forms.CharField() # Character Field (validators=[check_for_z])
    email = forms.EmailField() # Email Field
    verify_email = forms.EmailField(label='Enter your email again',required=True)
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)]) #built in method
    
    #botcatcher method
    '''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("GOTCHA BOT!")
        return  botcatcher
    '''
    # Matching email
    def clean(self):
        allCleanData = super().clean()
        email = allCleanData['email']
        vmail = allCleanData['verify_email']
        if email!=vmail:
            raise forms.ValidationError("Make sure your email match")