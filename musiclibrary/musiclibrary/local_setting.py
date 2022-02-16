# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z8n##o$2reoziau0vl(#h5(-r!rqdzm%)+5mwq^)nxeg_i#9c1'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'SaltyMeat1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}