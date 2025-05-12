import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')  # Use environment variable for secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False for production

# Allowed Hosts - Add your production domain and IP address
ALLOWED_HOSTS = ['himanshuprojects.duckdns.org', '51.20.128.222']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student_records',
    'rest_framework',  # Ensure this is added
    'rest_framework_simplejwt',  # Add JWT authentication package
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

ROOT_URLCONF = 'Student_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Student_management_system.wsgi.application'

# Database Configuration (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'table1'),  # Use environment variable for DB name
        'USER': os.getenv('DB_USER', 'himanshu'),  # Use environment variable for DB user
        'PASSWORD': os.getenv('DB_PASSWORD', 'Welcome@001'),  # Use environment variable for DB password
        'HOST': os.getenv('DB_HOST', 'localhost'),  # Use environment variable for DB host
        'PORT': '5432',
    }
}

# Password validation (consider using more strict validators in production)
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # You may change this to the timezone of your choice
USE_I18N = True
USE_TZ = True

# Static files (Important for deployment)
STATIC_URL = '/static/'  # Ensure this is '/static/' for production

# This will specify where the collected static files are stored
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF Authentication/Permission Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Ensures only authenticated users can access the API
    ],
}

# Enable secure cookies and ensure that they are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure this is True for production when using HTTPS
SESSION_COOKIE_SECURE = True  # Ensure this is True for production when using HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure HTTP Strict Transport Security (HSTS) is enabled when using HTTPS
SECURE_HSTS_SECONDS = 31536000  # A long time in seconds, e.g., 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Use this when deploying in production with HTTPS
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS in production

# Enable clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Add other necessary configurations like logging, email settings, etc.

# Email settings (Optional)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or your SMTP provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'your-email-password')

# Logging settings (Optional but recommended for production)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
