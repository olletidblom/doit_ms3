from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """Form to create/update a profile."""

    birthdate = forms.DateField(
        label="Birthdate",
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=False  
    )

    bio = forms.CharField(
        label="Bio",
        widget=forms.Textarea(attrs={'rows': 3}),  
        required=False  
    )

    location = forms.CharField(
        label="Location",
        max_length=100, 
        required=False
    )

    fname = forms.CharField(
        label="First Name",
        max_length=50,  
    )

    lname = forms.CharField(
        label="Last Name",
        max_length=50,  
    )


    class Meta:
        model = Profile
        fields = ["bio", "fname", "lname", "location", "birthdate"]  


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

