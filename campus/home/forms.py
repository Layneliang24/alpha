from django import forms
from login import models as login_models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = login_models.Profile
        fields = ['nickname', 'gender', 'phone', 'portrait', 'resume']
