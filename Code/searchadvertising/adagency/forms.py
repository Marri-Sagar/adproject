from django import forms

from adagency.models import adagencyregistrationmodel, uploadmodel
from django.core import validators




class adagencyregistrationform(forms.ModelForm):
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    mobile = forms.CharField(widget=forms.TextInput(),required=True,max_length=100,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    place = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    city = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = adagencyregistrationmodel
        fields = ['loginid','password','email','mobile','place','city','authkey','status' ]

class UploadaddForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[('Marketing','Marketing'),('Education','Education'),('Realestates','Realestates'),('Mobiles','Mobiles'),('Vehicles','Vehicles'
                                                                                                                                                              '')])
    class Meta:
        model = uploadmodel
        fields = ('category','property','brand','city','price','file')
