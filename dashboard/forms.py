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
# #                              Project Category
# # -------------------------------------------------------------------

class ProjectCategoryManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectCategoryManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter Project Category Title...',
            'maxlength': 100
        })


    class Meta:
        model = ProjectCategory
        fields = [
            "title"
        ]

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
        self.fields['category'].widget.attrs.update({
            'placeholder': 'Enter developemnt start year...'
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
            "name", "client_name","category", "developement_start_year", "developement_end_year", "image", "scope"
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


# # -------------------------------------------------------------------
# #                               News
# # -------------------------------------------------------------------

class NewsManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter News Title...',
            'maxlength': 100
        })
        self.fields['description'].widget.attrs.update({
            'id': 'news_description_input',
            'placeholder': 'Enter News Description...',
            'rows': 10,
            'cols': 5,
        })


    class Meta:
        model = News
        fields = [
            "title",  "image", "category", "description"
        ]
        widgets = {
            'description': CKEditorWidget(),
        }



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
# #                               ImageGroup
# # -------------------------------------------------------------------

class ImageGroupManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageGroupManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter Group Title...',
            'maxlength': 100
        })


    class Meta:
        model = ImageGroup
        fields = [
            "title"
        ]


# # -------------------------------------------------------------------
# #                               Gallery
# # -------------------------------------------------------------------

class GalleryManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalleryManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter News Category Title...',
            'maxlength': 100
        })
        self.fields["image_group"].help_text = "Please select image group"


    class Meta:
        model = Gallery
        fields = [
            "title",  "image", "image_group"
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


# # -------------------------------------------------------------------
# #                               Client
# # -------------------------------------------------------------------


class ClientManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientManageForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter  Client Name...',
            'maxlength': 100
        })
        self.fields['url'].widget.attrs.update({
            'placeholder': 'Enter Client Url...',
            'maxlength': 100
        })


    class Meta:
        model = Client
        fields = [
            "name","url", "category",  "logo"
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

    # # -------------------------------------------------------------------
    # #                               Social Account
    # # -------------------------------------------------------------------

class SocialAccountManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SocialAccountManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter Social Account Title...',
            'maxlength': 100
        })

    class Meta:
        model = SocialAccount
        fields = [
            "title", "logo", "url"
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



# # -------------------------------------------------------------------
# #                               Job Position
# # -------------------------------------------------------------------

class JobPositionManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobPositionManageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter Job Position Title...',
            'maxlength': 100
        })

    class Meta:
        model = JobPosition
        fields = [
            "title"
        ]


# # -------------------------------------------------------------------
# #                               Job
# # -------------------------------------------------------------------

class JobManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobManageForm, self).__init__(*args, **kwargs)

        self.fields['location'].widget.attrs.update({
            'placeholder': 'Enter Job Location...',
        })
        self.fields['hours'].widget.attrs.update({
            'placeholder': 'Enter Hours...',
        })
        self.fields['salary'].widget.attrs.update({
            'placeholder': 'Enter Salary...',
        })
        self.fields['description'].widget.attrs.update({
            'id': 'job_description_input',
            'placeholder': 'Enter Job Description...',
            'rows': 10,
            'cols': 5,
        })

    class Meta:
        model = Job
        fields = [
            "job_position", "job_type", "location", "hours", "salary", "description", "is_active"
        ]
        widgets = {
            'description': CKEditorWidget(),
        }



# # -------------------------------------------------------------------
# #                               Contact
# # -------------------------------------------------------------------

class ContactManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactManageForm, self).__init__(*args, **kwargs)

        self.fields['phone1'].widget.attrs.update({
            'placeholder': 'Enter 1st Phone Number...',
            'maxlength': 50
        })
        self.fields['phone2'].widget.attrs.update({
            'placeholder': 'Enter 2nd Phone Number...',
            'maxlength': 50
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter Email Address...',
            'maxlength': 100
        })
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Enter Address...',

        })

    class Meta:
        model = Contact
        fields = [
            "phone1","phone2","email","address"
        ]


# # -------------------------------------------------------------------
# #                               Job Application
# # -------------------------------------------------------------------

class JobApplicationManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobApplicationManageForm, self).__init__(*args, **kwargs)
        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Enter Contact Number...',
            'maxlength': 50
        })

    class Meta:
        model = Career
        fields = [
            "job", "file", "contact", "status"
        ]

class CVManageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CVManageForm, self).__init__(*args, **kwargs)
        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Enter Contact Number...',
            'maxlength': 50
        })

    class Meta:
        model = Career
        fields = [
            "file", "contact", "status"
        ]


JOB_APPLICATION_STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Review", "Review"),
    ("Confirmed", "Confirmed"),
    ("Rejected", "Rejected"),
)
class JobStatusManageForm(forms.Form):
    status = forms.ChoiceField(
        choices=JOB_APPLICATION_STATUS_CHOICES, label="status"
    )
    mail_body = forms.CharField(
        required=False, widget=CKEditorWidget()
    )

    def __init__(self, *args, **kwargs):
        career_object = kwargs.pop('career_object', None)
        print(career_object, "*** Career Object From View in Form ***")
        super(JobStatusManageForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = career_object.status
