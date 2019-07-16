# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'logged_out'

GOOGLE_LOGIN_URL = '/auth/login/google-oauth2/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',

    'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
# SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_GOOGLE_KEY = '604496538981-fqt7bc50jksb97po5ltghrd1lt73ghnv.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_SECRET = '1GYqI2q8BEW7EdlcQlag0lrk'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}
# SOCIAL_AUTH_STORAGE = 'social_django_mongoengine.models.DjangoStorage'

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS
