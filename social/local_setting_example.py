# EXAMPLE!!! Rename to local_setting.py after change!!!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hwyo%2)ryzzc*$v9adfgdfgdfx!9_h4(8mr6#^1-_bwdenil@c=e#4j89-'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '67240434534527755-6kobovjsqaodfgdfgd11iqbtmr8ca0f4nghertertm98o.apps.googleusercontent.com',
            'secret': 'Kh4LcqcxLxM9srfsdfsdfsdfgdfguRXRVXIfqJKi',
            'key': ''
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}