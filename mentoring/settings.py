from pathlib import Path
import os
from configurations import Configuration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Base(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['SECRET_KEY']

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = [
        'mentoring.ngrok.io',
    ]

    # Project-specific confit

    # days to retain user data
    DATA_RETENTION_DAYS = 180

    # secret key for hashing pair_ids (treat like SECRET_KEY)
    PAIR_ID_HASH_SECRET = os.environ['PAIR_ID_HASH_SECRET']

    # Trust X-Forwarded-Proto to signify a secure connection
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # security settings
    SECURE_HSTS_SECONDS = 3600
    SECURE_SSL_REDIRECT = True
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = 1  # Set that the cookie should only be sent on https
    CSRF_COOKIE_SECURE = 1  # Same for CSRF cookies

    # Application definition

    INSTALLED_APPS = [
        'mentoring.enrollment.apps.EnrollmentConfig',
        'mentoring.participants.apps.ParticipantsConfig',
        'mentoring.pairing.apps.PairingConfig',
        'mentoring.frontend.apps.FrontendConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'mozilla_django_oidc',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'csp.middleware.CSPMiddleware',
    ]

    ROOT_URLCONF = 'mentoring.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['mentoring/templates'],
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

    WSGI_APPLICATION = 'mentoring.wsgi.application'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # Authentication
    # https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html

    AUTHENTICATION_BACKENDS = [
        'mentoring.auth.MentoringAuthBackend',
    ]

    OIDC_RP_SIGN_ALGO = "RS256"
    OIDC_RP_CLIENT_ID = os.environ['OIDC_RP_CLIENT_ID']
    OIDC_RP_CLIENT_SECRET = os.environ['OIDC_RP_CLIENT_SECRET']
    # OIDC_OP_* come from https://auth.mozilla.auth0.com/.well-known/openid-configuration
    OIDC_OP_JWKS_ENDPOINT = "https://auth.mozilla.auth0.com/.well-known/jwks.json"
    OIDC_OP_TOKEN_ENDPOINT = "https://auth.mozilla.auth0.com/oauth/token"
    OIDC_OP_USER_ENDPOINT = "https://auth.mozilla.auth0.com/userinfo"
    OIDC_OP_AUTHORIZATION_ENDPOINT = "https://auth.mozilla.auth0.com/authorize"
    OIDC_RP_SCOPES = "openid email profile"

    # URLs to which the user will be redirected when login/logout are complete
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"

    # URL to which the user should be redirected in order to login
    LOGIN_URL = '/oidc/authenticate/'

    # Members of these Mozilla SSO groups will be Django staff, able to do everything;
    # this capability is given to committee members.
    STAFF_GROUPS = [
        'mozilliansorg_mentoring-committee',
    ]

    # Default permission for all API methods is to require user.is_staff
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
        ]
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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # content security policy
    CSP_DEFAULT_SRC = ["'self'", "'unsafe-inline'"]
    # For development builds of the react app (`yarn dev`, not `yarn build`), eval is needed
    if DEBUG:
        CSP_DEFAULT_SRC.append("'unsafe-eval'")
    CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]
    CSP_STYLE_SRC = ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"]

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

class Development(Base):
    pass
