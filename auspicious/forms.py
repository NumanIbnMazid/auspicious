from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from dashboard.models import Career
from django.conf import settings
import re
from django.template.defaultfilters import filesizeformat
import os


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

        self.fields['file'].help_text = "Only .doc, .docx, .pdf file format is supported and maximum file size is 2.5MB."

    class Meta:
        model = Career
        fields = [
            "file", "contact"
        ]

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file == None:
            file_extension = os.path.splitext(file.name)[1]
            allowed_file_types = settings.ALLOWED_JOB_APPLY_FILE_TYPES
            content_type = file.content_type.split('/')[0]
            if not file_extension in allowed_file_types:
                raise forms.ValidationError("Only %s file formats are supported! Current file format is %s" % (
                    allowed_file_types, file_extension))
            if file.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(file.size)))
            return file
        return None
