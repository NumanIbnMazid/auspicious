"""
----------------------- * Dynamic Content Configuration * -----------------------
"""

MAIL_FROM = "web@auspiciousbd.com"
RECEIVER_EMAIL = "web@auspiciousbd.com"

BLOCKED_URL = '/blocked/'
ACCESS_DENIED_URL = '/access-denied/'

"""
----------------------- * Django Allauth Configuration * -----------------------
"""
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'
HOME_URL = '/'
SITE_NAME = 'Auspicious'
ACCOUNT_EMAIL_MAX_LENGTH = 190
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_USERNAME_MIN_LENGTH = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # mandatory, optional, none
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Auspicious'
ACCOUNT_USERNAME_BLACKLIST = ['robot', 'hacker', 'virus', 'spam']
ACCOUNT_ADAPTER = 'auspicious.adapter.CustomAccountAdapter'
ACCOUNT_FORMS = {
    'signup': 'auspicious.forms.CustomSignupForm',
}
# AUTH_USER_MODEL = 'auspicious.accounts.models.UserProfile'
# ACCOUNT_SIGNUP_FORM_CLASS = 'auspicious.forms.CustomSignupForm'
# Social Account ---
# SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_EMAIL_VERIFICATION = False


"""
----------------------- * Django CK Editor Configuration * -----------------------
"""
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_CONFIGS = {
    'default': {
        'uiColor': '#cdc9ff',
        'height': '100%',
        'width': '100%',
        # 'skin': 'moono',
        # 'skin': 'office2013',
        # 'toolbar_Basic': [
        #     ['Source', '-', 'Bold', 'Italic']
        # ],
        'toolbar_NMNckCustomToolbarConfig': [
            {'name': 'document', 'items': [
                'Print', '-', 'Templates', '-', 'Maximize', 'ShowBlocks', 'Preview']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo', 'Find', 'Replace', '-', 'SelectAll']},
            '/',
            {'name': 'basicstyles',
             'items': ['TextColor', 'BGColor', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
            '/',
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'FontSize']},
        ],
        # 'toolbar': 'NMNckCustomToolbarConfig',  # put selected toolbar config here
        'toolbar': 'Basic',  # put selected toolbar config here
        'toolbar': 'full',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 500,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


"""
----------------------- * File Configuration * -----------------------
"""
ALLOWED_IMAGE_TYPES = ['.jpg', '.jpeg', '.png', '.svg']
MAX_UPLOAD_SIZE = 2621440

# File Validation Staffs
ALLOWED_JOB_APPLY_FILE_TYPES = ['.doc', '.docx', '.pdf']
