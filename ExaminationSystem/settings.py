import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!-!e_i8^#cn0mmz4n&$4qg1+oelex1!vf10m&zp9yx-ds7hnwg'

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
    'users.apps.UsersConfig',
    'organization.apps.OrganizationConfig',
    'xadmin',
    'crispy_forms',
    'reversion',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'social_django',
    'corsheaders',
]

AUTH_USER_MODEL = 'users.UserProfile'

#跨域
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:8000','http://127.0.0.1:5500']
CORS_ALLOW_CREDENTIALS = True

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

APPEND_SLASH = False
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}
import datetime
#有效期限
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_RESPONSE_PAYLOAD_HANDLER':'users.views.jwt_response_payload_handler'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 中间键
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'ExaminationSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ExaminationSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ExaminationSystem',
        'USER': 'root',
        'PASSWORD': 'byf12138',
        'HOST': '47.107.118.146',
        'PORT': '3306'
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

SOCIAL_AUTH_WEIBO_KEY = '3978227208'
SOCIAL_AUTH_WEIBO_SECRET = '1a27b77144ba9ad64e2e13449975103e'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://127.0.0.1:5500/templates/web/index.html'



# 云片网 api_key
APIKEY = '9125dde81bd0553fde56fb1db6177193'


#邮箱
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = "25"
EMAIL_HOST_USER = "1419517126@qq.com"
#生成的授权码
EMAIL_HOST_PASSWORD = "hcuuamtyygumjaee"
EMAIL_USE_TLS = True
EMAIL_FROM = "1419517126@qq.com"


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
