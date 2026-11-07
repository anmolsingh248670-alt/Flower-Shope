
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# SECURITY
# ==========================================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "change-this-secret-key"
)

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://flower-shope-7rf3.onrender.com",
]


SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)


# ==========================================
# INSTALLED APPLICATIONS
# ==========================================

INSTALLED_APPS = [

    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Flower application
    "app",

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",

    # Django Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Social login providers
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",

]


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


# ==========================================
# URL CONFIGURATION
# ==========================================

ROOT_URLCONF = "Flower.urls"


# ==========================================
# TEMPLATES
# ==========================================

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


WSGI_APPLICATION = "Flower.wsgi.application"


# ==========================================
# DATABASE
# ==========================================

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",

    }

}


# ==========================================
# PASSWORD VALIDATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]


# ==========================================
# INTERNATIONALIZATION
# ==========================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


# ==========================================
# MEDIA FILES
# ==========================================

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# ==========================================
# LOGIN SETTINGS
# ==========================================

LOGIN_URL = "home_login"

LOGIN_REDIRECT_URL = "home"


# ==========================================
# CLOUDINARY
# ==========================================

CLOUDINARY_STORAGE = {

    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),

    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),

    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),

}


STORAGES = {

    "default": {

        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",

    },

    "staticfiles": {

        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",

    },

}


DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)


# ==========================================
# EMAIL SETTINGS - BREVO
# ==========================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp-relay.brevo.com"

EMAIL_PORT = 2525

EMAIL_USE_TLS = True

EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

EMAIL_TIMEOUT = 20


# ==========================================
# RAZORPAY
# ==========================================

RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID")

RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET")


# ==========================================
# DJANGO ALLAUTH
# ==========================================

SITE_ID = 1


AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]


ACCOUNT_LOGIN_METHODS = {"email"}

ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "password1*",
    "password2*",
]


SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_LOGIN_ON_GET = False


# ==========================================
# GOOGLE LOGIN
# ==========================================

SOCIALACCOUNT_PROVIDERS = {

    "google": {

        "APP": {

            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),

            "secret": os.environ.get("GOOGLE_CLIENT_SECRET"),

            "key": "",

        },

        "SCOPE": [

            "profile",

            "email",

        ],

        "AUTH_PARAMS": {

            "prompt": "select_account",

        },

    },

}


# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
