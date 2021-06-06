from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from dashboard.models import Career


class CustomSignupForm(SignupForm):
    NONE = ''
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    UNDEFINED = 'U'
    GENDER_CHOICES = (
        (NONE, '--- Select Gender ---'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (UNDEFINED, 'Do not mention'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, label="Gender", initial='',
        widget=forms.Select(), required=True
    )

    def signup(self, request, user):
        user.save()
        userprofile, created = self.get_or_create(user=user)
        user.userprofile.save()


class CareerManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CareerManageForm, self).__init__(*args, **kwargs)

        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Enter Contact Number...',
            'maxlength': 50
        })

    class Meta:
        model = Career
        fields = [
            "file", "contact"
        ]
