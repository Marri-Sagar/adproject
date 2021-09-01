from django import forms

from user.models import registrationmodel, viewdetailsmodel
from django.core import validators

def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only strings allowed for name")

class registrationform(forms.ModelForm):
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    mobile = forms.CharField(widget=forms.TextInput(),required=True,max_length=100,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    gender = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    age = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    occupation = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    place = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    city = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = registrationmodel
        fields = ['loginid','password','email','mobile','gender','age','occupation','place','city','authkey','status' ]


class viewdetailsform(forms.ModelForm):
    property = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    brand = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    city = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    #file = forms.FileField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    rating = forms.ChoiceField(choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    review = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    
    class Meta:
        model = viewdetailsmodel
        fields = ('property', 'brand', 'city', 'price', 'rating','review')