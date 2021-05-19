from django import forms
from .models import *
from django.conf import settings
import re
from django.core.exceptions import ValidationError
from util.helpers import validate_chars, simple_form_widget
from ckeditor.widgets import CKEditorWidget
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import ImageFieldFile
from django.template.defaultfilters import filesizeformat
import os



# # -------------------------------------------------------------------
# #                               Project
# # -------------------------------------------------------------------

class ProjectManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectManageForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter project name...',
            'maxlength': 100
        })

        self.fields['client_name'].widget.attrs.update({
            'placeholder': 'Enter client name...',
            'maxlength': 100
        })

        self.fields['developement_start_year'].widget.attrs.update({
            'placeholder': 'Enter developemnt start year...'
        })

        self.fields['developement_end_year'].widget.attrs.update({
            'placeholder': 'Enter developemnt end year...'
        })

        self.fields['scope'].widget.attrs.update({
            'id': 'project_scope_input',
            'placeholder': 'Enter project scope...',
            'rows': 10,
            'cols': 5,
        })


    class Meta:
        model = Project
        fields = [
            "name", "client_name", "developement_start_year", "developement_end_year", "image", "scope"
        ]
        widgets = {
            'scope': CKEditorWidget(),
        }

    def clean_developement_end_year(self):
        data = self.cleaned_data['developement_end_year']
        developement_start_year = self.cleaned_data['developement_start_year']
        if data is not None and data != "":
            if int(data) < int(developement_start_year):
                raise forms.ValidationError(
                    "Development End year must be greater than or equal Developemnt Start Year!"
                )
        return data

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and isinstance(image, UploadedFile):
            file_extension = os.path.splitext(image.name)[1]
            allowed_image_types = settings.ALLOWED_IMAGE_TYPES
            content_type = image.content_type.split('/')[0]
            if not file_extension in allowed_image_types:
                raise forms.ValidationError("Only %s file formats are supported! Current image format is %s" % (
                    allowed_image_types, file_extension))
            if image.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(image.size)))
            return image
        return None



# # -------------------------------------------------------------------
# #                               News Category
# # -------------------------------------------------------------------

class NewsCategoryManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsCategoryManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter News Category Title...',
            'maxlength': 100
        })


    class Meta:
        model = NewsCategory
        fields = [
            "title",  "image"
        ]



    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and isinstance(image, UploadedFile):
            file_extension = os.path.splitext(image.name)[1]
            allowed_image_types = settings.ALLOWED_IMAGE_TYPES
            content_type = image.content_type.split('/')[0]
            if not file_extension in allowed_image_types:
                raise forms.ValidationError("Only %s file formats are supported! Current image format is %s" % (
                    allowed_image_types, file_extension))
            if image.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(image.size)))
            return image
        return None
