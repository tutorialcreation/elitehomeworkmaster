import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '25a_w5g&vy-#-c3d7mmt1j-2!8qe#r@*r@a!9l@@fvg&cp5w!0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # personal apps
    # 'chats',
    'payments',
    'assignments',
    'contacts',
    'chat',
    'authentication',
    # third-party apps
    'bootstrap_modal_forms',
    'paypal.standard.ipn',
    'channels',
    'widget_tweaks',
    'crispy_forms',
    'writers'
]

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'homeworkdoer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'homeworkdoer.context_processors.chat',
                'chat.context_processors.chat_form',
                'chat.context_processors.messages',
                'payments.context_processors.get_membership_quote',
                'assignments.context_processors.get_notifications',
                'assignments.context_processors.get_first_assignment',
            ],
        },
    },
]

WSGI_APPLICATION = 'homeworkdoer.wsgi.application'
ASGI_APPLICATION = "homeworkdoer.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [('localhost',6379)],
            # "hosts": ["redis://h:pc2492726307364f7b5e05151c944e99c420857a911626ae634b77086b4d6f7d0@ec2-3-211-169-9.compute-1.amazonaws.com:30959"],
            "hosts": [os.environ.get("REDISCLOUD_URL", "")],
        },
    },
}

ASGI_THREADS=1000

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



#heroku config:set DATABASE_URL="postgis://xchxoturerfxst:f81207883ed22185bb3ab0950538591a69ea06d83ef7d0ae41e8cc873aac5c85@ec2-18-210-180-94.compute-1.amazonaws.com:5432/d1pbihmnbr53r6?postgis_extension=true&search_schema_path=public,postgis"

# GDAL_LIBRARY_PATH='/app/lib'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap3'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")

STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "")
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "")
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint

AUTH_USER_MODEL='authentication.User'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
FROM_EMAIL = 'lutherlunyamwi@gmail.com'
DEFAULT_FROM_EMAIL = 'lutherlunyamwi@gmail.com'
SENDGRID_API_KEY=os.getenv('SENDGRID_API_KEY','')
EMAIL_CONFIRMATION_HMAC='lutherlunyamwi@gmail.com'


PAYPAL_RECEIVER_EMAIL='kassimstephen68@gmail.com'
# test for martin
# PAYPAL_CLIENT_ID='AdU1TgEvGSZw4q74_38y5qYXRpCHVGboZb5FPDUBaMETU6d7GPCOY_tD7XRe2x64HAUqiiu-GNxJsk7u'
# PAYPAL_SECRET_ID='EDItyORj80cSYieq0A6Tm9wuzvzUooRq3H45asFnjJ-PltZTB0j6P-3DwcCnobuKGF0cXKZoGSuH9kzY'
# live for martin
# PAYPAL_CLIENT_ID='AdKxhekk6S8VDr5ybQ4Hug-gj-2lA7aCSKEHQlHam9z5oOXQp0ITU_mFFQWlpk5BrpdoGS1UBrxIQULt'
# PAYPAL_SECRET_ID='EJhcTsSypk5_yPwhfuLKfp_7sBJ3Bu20Kvxk-L2kChtur8Hj6Zvrvo-mGKWo4roJRIk4aE8dvxFHEQHE'
# live for Kassim
PAYPAL_CLIENT_ID='ASW6NnMt-FFRheYnCdBxgDyRIZrwYelfkm-MYkMu8CiT-y7E6RGDgEvX6ZZuNfn1_fDPECWWMZ581oeK'
PAYPAL_SECRET_ID='EK9Tjf23-v-4QkvOOEnQORwISSLM0zB1MvjBeYf3s3D8WCKvebP-UeYBEMcMg6s5SkhMJaiR-8GyVTWI'
# LOGIN_REDIRECT_URL='/'

PAYPAL_TEST = True
GEOIP_PATH =os.path.join(BASE_DIR, 'geoip/GeoLite2-Country_20200828')
DJANGO_ALLOW_ASYNC_UNSAFE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME", ""),
        'USER': os.environ.get("DB_USER", ""),
        'PASSWORD': os.environ.get("DB_PASSWORD", ""),
        'HOST': os.environ.get("DB_HOST", ""),
        'PORT': os.environ.get("DB_PORT", ""),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'homeworkdoer',
    #     'USER': 'martin',
    #     'PASSWORD':'martin1996-',
    #     'HOST':'localhost',
    #     'PORT':5432,
    #     'TEST': {
    #         'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
    #     }
    # }
}
