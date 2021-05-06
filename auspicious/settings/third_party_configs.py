
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
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # mandatory, optional, none
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