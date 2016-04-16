"""
Django settings for pypolo project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))iy*8&jyl3s6m58g(z=6xo5yq^hl^-ppk$v-h-pd#@fhn&k@0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MAKE_TRADES = True

ALLOWED_HOSTS = ['trader.owocki.com', '45.55.42.224']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'history',
    'chartit',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pypolo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['history/templates/', ],
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


WSGI_APPLICATION = 'pypolo.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# logfile
LOG_FILE = "/var/log/django.log"

# Default number of threads for workers
NUM_THREADS = 1

TRADER_GRANULARITY_MINS = 10  # TODO: change me when granularity changes (search this string <---)

TRADER_CURRENCY_CONFIG = [
    {'type': 'nn',
     'name': 'ETH / 5',
     'symbol': 'BTC_ETH',
     'weight': 0.1,
     'granularity': TRADER_GRANULARITY_MINS,
     'datasetinputs': 5},
    {'type': 'nn',
     'name': 'ETH / 5',
     'symbol': 'BTC_ETH',
     'weight': 0.1,
     'granularity': TRADER_GRANULARITY_MINS,
     'datasetinputs': 4},
    {'type': 'classifier',
     'symbol': 'USDT_BTC',
     'name': 'AdaBoost',
     'weight': 0.1,
     'granularity': TRADER_GRANULARITY_MINS,
     'datasetinputs': 2,
     'minutes_back': 1000},
    {'type': 'classifier',
     'symbol': 'USDT_BTC',
     'name': 'Naive Bayes',
     'weight': 0.1,
     'granularity': TRADER_GRANULARITY_MINS,
     'datasetinputs': 2,
     'minutes_back': 1000},
    {'type': 'classifier',
     'symbol': 'BTC_ETH',
     'name': 'Naive Bayes',
     'weight': 2,
     'granularity': TRADER_GRANULARITY_MINS * 3,
     'datasetinputs': 2,
     'minutes_back': 1000},
]

# trainer currency config params doc

# ticker - currency pair to trade upon

# min_back how many candlesticks (of granularity length) to pull.
# 'minutes' is a misnomer, artifact of  when only minute-by-minute predictions were made

# granularity - length, in minutes, of candlesticks.

# datasetinputs - number of candlesticks to feed into NN/Classifier

# timedelta_back_in_granularity_increments  - number of candlesticks (of granularity length) back to look from
# present candlestick.
#    starting point of dataset = present - timedelta_back_in_granularity_increments - min_back
#    ending point of dataset = present - timedelta_back_in_granularity_increments

# name - name of classification algorithm (see sklearn documentation for more)

# hidden_layers - number of pybrain hidden layers to use

# epochs  -  Train on the current dataset for the given number of epochs.

# bias  -  (bool) bias flags to indicate whether the network should have biases
# http://pybrain.org/docs/api/tools.html?highlight=buildnetwork#pybrain.tools.shortcuts.buildNetwork

# momentum -   http://pybrain.org/docs/api/supervised/trainers.html?highlight=momentum

# learningrate -  The learning rate gives the ratio of which parameters are changed into the direction of the gradient.
# http://pybrain.org/docs/api/supervised/trainers.html?highlight=learningrate

# weightdecay -  weightdecay corresponds to the weightdecay rate, where 0 is no weight decay at all
# http://pybrain.org/docs/api/supervised/trainers.html?highlight=weightdecay

# recurrent -  (bool) If the recurrent flag is set, a RecurrentNetwork will be created, otherwise a FeedForwardNetwork

TRAINER_CURRENCY_CONFIG = {
    'classifiers': {
        'ticker': ['BTC_ETH', 'USDT_BTC'],
        'min_back': [100, 1000, 24 * 60, 24 * 60 * 2],
        'granularity': [10, 15, 20, 30, 40, 50, 60, 120, 240],
        'datasetinputs': [2, 3, 5],
        'timedelta_back_in_granularity_increments': [10, 30, 60, 100, 1000],
        'name': ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Decision Tree",
                 "Random Forest", "AdaBoost", "Naive Bayes", "Linear Discriminant Analysis",
                 "Quadratic Discriminant Analysis"],
    },
    'supervised_nn': {
        'ticker': ['BTC_ETH', 'USDT_BTC'],
        'hidden_layers': [1, 5, 15, 40],
        # 2/23 -- removed 15, it was barely edged out by 1,5.
        # 2/25 -- added 15, 40 in because of recent bugs
        'min_back': [100, 1000, 24 * 60, 24 * 60 * 2],
        # 2/22 - eliminated 10000
        # 2/25 -- added 24*50, 24*60*2 because "maybe because NN only contains last 1000 data points (1/3 day).
        #   if only selling happened during that time, nn will bias towards selling.  duh!"
        'granularity': [10, 15, 20, 30, 40, 50, 60, 120, 240],
        # 2/23 notes - results so far: 59 (54% correct) 15 (56% correct) 1 (50% correct) 5 (52% correct).
        #   removing 1,5, adding 30 . 2/23 (pt 2) -- added 119, 239
        # 2/24 notes -- removed 120,240, added 20, 40, 45
        # 2/25 notes -- added 10, 50, removed 45
        # 2/25 -- added 120,240 back in to retest in light of recent bugs
        'datasetinputs': [1, 2, 3, 4, 5, 6, 15, 10, 20, 40, 100, 200],
        # 2/23 -- removed 3,5,15 -- added 20,40,100
        # 2/24 -- removed 7,10,20,40,100, added 3,4,5
        # 2/25 -- added 3,5,15,10,20,40,100 back in to retest in light of recent bugs
        'epochs': [1000],
        # 2/22 -- eliminated 4000, 100
        'bias': [True],
        # 2/22 -- Eliminated 'False'
        'momentum': [0.1],
        'learningrate': [0.05],
        # 2/22 -- elimated 0.005, 0.01, adding 0.03 and 0.1 today.  #2/23 - 0.1 (54% correct) 0.05 (55% correct) 0.03
        # (54% correct) .  eliminating everything but 0.05 so i can test more #datasetinput_options
        'weightdecay': [0.0],
        # 2/22 -- eliminated 0.1,0.2
        'recurrent': [True],
        # 2/23 notes - 0 (52% correct) 1 (55% correct), removed false
        'timedelta_back_in_granularity_increments': [10, 30, 60, 100, 1000],
    }
}

SOCIAL_NETWORK_SENTIMENT_CONFIG = {
    'twitter': ['ETH', 'BTC', 'FCT', 'BTS', 'XMR', 'MAID', 'DASH'],
    'bitcointalk': ['ETH', 'BTC', 'FCT', 'BTS', 'XMR', 'MAID', 'DASH']
}

# https://poloniex.com/fees/
FEES = {
    'poloniex': [
        {'maker': 0.0015, 'taker': 0.0025, 'volume': '< 600 BTC'},
        {'maker': 0.0014, 'taker': 0.0024, 'volume': '>= 600 BTC'},
        {'maker': 0.0012, 'taker': 0.0022, 'volume': '>= 1200 BTC'},
        {'maker': 0.001, 'taker': 0.0020, 'volume': '>= 2400 BTC'},
        {'maker': 0.0008, 'taker': 0.0016, 'volume': '>= 6000 BTC'},
        {'maker': 0.0005, 'taker': 0.0014, 'volume': '>= 12000 BTC'},
        {'maker': 0.0002, 'taker': 0.0012, 'volume': '>= 18000 BTC'},
        {'maker': 0.0000, 'taker': 0.0010, 'volume': '>= 24000 BTC'},
    ]}

TRADE_VOLUME_TRAILING_30_DAYS = '< 600 BTC'  # TODO - in the future, make this calculated dynamically
TRADE_MODE = 'taker'  # TODO -- in the future, make this more dynamicly chosen via trade.py

# sets how aggressive user wants to be in managing their trades
# 1 = trade when if & when projected profit >= fees
# 2 = trade when if & when projected profit >= 2x fees
# . . .
# n = trade when if & when projected profit >= nx fees
FEE_MANAGEMENT_STRATEGY = 1


# Include local settings overrides
try:
    from pypolo.local_settings import *  # NOQA
    INSTALLED_APPS += DEBUG_APPS
except (ImportError, NameError) as exp:
    print 'Failed to load pypolo/local_settings.py because: %s' % exp
