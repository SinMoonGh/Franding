"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
GOOGLE_CLIEND_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_KEY = os.getenv('GOOGLE_KEY')
KAKAO_CLIENT_ID = os.getenv('KAKAO_CLIENT_ID')
KAKAO_KEY = os.getenv('KAKAO_KEY')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*vp_8&e63t5yoa15dp))q58_shk_i*3z1v1a29v&eygbhdjp^#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'widget_tweaks', 
    
    'item',
    'mypage',
    'review',
    'seller',
    'cart',
    # 'bootstrap4',
    'payment',
    'event',
    'subscribe',
    'guide',
    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    
    # 'rest_framework',
    'QnA',
    # 'debug_toolbar',
    'django_filters',
]

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.get_profile_image',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'franding_db',
        'USER': 'postgres',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'hanslab.org',  # 또는 PostgreSQL 서버의 IP 주소
        'PORT': '35432',       # PostgreSQL의 기본 포트 번호
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
)


SITE_ID = 1

SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL='/'
# LOGOUT_REDIRECT_URL='/'
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')
ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_LOGOUT_ON_GET = True
# SOCIALACCOUNT_ADAPTER = 'config.adapters.YourSocialAccountAdapter'


MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1', '[::1]']

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis 서버 위치
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

INTERNAL_IPS = [
    # ...,
    '127.0.0.1',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


# 소셜 로그인을 위한 키와 시크릿 설정

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': GOOGLE_CLIEND_ID, 
            'secret': GOOGLE_KEY, 
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'kakao': {
        'APP': {
            'client_id': KAKAO_CLIENT_ID,
            'secret': KAKAO_KEY, 
            'key': ''
        }
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = '1447wjddbs@gmail.com'
# EMAIL_HOST_PASSWORD = 'digo oqma cdgv aivv'
# DEFAULT_FROM_EMAIL = '1447wjddbs@gmail.com'
