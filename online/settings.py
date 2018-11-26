"""
Django settings for online project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys  # 配置app目录
import pymysql  # 操作mysql 数据库

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xq-9k7c%a*qz31+fy9$&$-x+iksna3ys7j&=_0n!sb=9hxno!3'

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
    'users',
    'organizations',
    'operation',
    'courses',
    'xadmin',
    'crispy_forms',
    'captcha',  # 验证码包，需要配置url，并在数据库中生成表
    'pure_pagination',  # 分页器,在下面有配置
    # 'DjangoUeditor', # 富文本编辑器

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

ROOT_URLCONF = 'online.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'online.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online',
        'USER': 'root',
        'PASSWORD': 'WZQwzq+123',
        'HOST': '127.0.0.1',
        'POST': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 数据库获取本地时间,如果为True则取国际时间

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = '/var/www/online/static/'  # 项目上线使用

# 解决：配置正确，而网页中文件无法加载的问题
STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
)


# 配置用户上传的文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 需要配置TEMPLATES


# UserProfile 覆盖了 django 内置的 users 表
AUTH_USER_MODEL = 'users.UserProfile'

# 发送邮件功能设置
EMAIL_HOST = 'smtp.sina.com'  # 使用SMTP服务器，需要在邮箱中开启此服务
EMAIL_PORT = 25
EMAIL_HOST_USER = 'online_learn_edu@sina.com'
EMAIL_HOST_PASSWORD = '11111111'

EMAIL_FROM = 'online_learn_edu@sina.com'  # 自定义配置，使用时需要引入


# 重写ModelBackend模块下的authenticate方法
AUTHENTICATION_BACKENDS = (
    'users.views.ChongxieAuthenticate',
)

# 分页器
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,   # 中间显示多少个页码
    'MARGIN_PAGES_DISPLAYED': 2,  # 两端显示多少个页码
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,    # 当输入页数不合法是否要跳到第一页
}