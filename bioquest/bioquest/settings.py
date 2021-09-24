"""
Django settings for bioq project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
#import storages

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*m4hshjfnvk**7829347jnvfknahnvkjf)3_8@8xzv%(+)^#(1_nyx^sfviu^%kjnkj$$#2j*n$b^nbjdfvnsb7n%f'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["bioquest.pythonanywhere.com"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bioquest.main',
    'django.contrib.auth',
    'nested_admin'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'bioquest.bioquest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'bioquest/db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'bioquest/bioquest/bioquest/bioquest-82c3ca97610e.json'


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bioquest/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'bioquest/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static',)

STATICFILES_DIRS = ('static/',)


#DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'
#DEFAULT_MEDIA_STORAGE = 'storages.backends.ftp.FTPStorage'
#FTP_STORAGE_LOCATION = 'ftp://peripatus_bioq:equisetum@217.112.35.72:21'
#DEFAULT_MEDIA_STORAGE = 'storages.backends.ftp.FTPStorage'
#FTP_STORAGE_LOCATION = 'ftp://peripatus_bioq:equisetum@<bioquest.operculum.org:21'
#FTP_STORAGE_LOCATION = 'ftp://peripatus_bioq:equisetum@217.112.35.72:21'
