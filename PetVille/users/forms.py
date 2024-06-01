from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class trainingRegisterForm(forms.Form):
    petname = forms.CharField()
    breed = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(
        choices=(
            (1, "8:00 - 10:00"), 
            (2, "11:00 - 13:00"),
            (3, "14:00 - 16:00"), 
            (4, "17:00 - 19:00"),
                 )
    )

class sittingForm(forms.Form):
    petname = forms.CharField()
    breed = forms.CharField()
    address = forms.CharField()
    startdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    days = forms.ChoiceField(
        choices=((1, "1 Days"), (2, "2 Days"),(3, "3 Days"), (4, "4 Days"),(5, "5 Days"), (6, "6 Days"),(7, "7 Days"))
    )

class vetvisitForm(forms.Form):
    PetName = forms.CharField()
    Breed = forms.CharField()
    dateOfVisit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Reason = forms.ChoiceField(
        choices=(
            (1, "Check-up"), 
            (2, "Dental Visit"),
            (3, "Spay/Neuter"), 
                 )
    )
