
import os
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
tipo = config['PROD']


SECRET_KEY = tipo['SECRET_KEY']


DEBUG = False

ALLOWED_HOSTS = [tipo['HOST']]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': tipo['DB_HOST'],   
        'NAME': tipo['DB_NAME'],        
        'USER': tipo['DB_USER'] ,
        'PASSWORD': tipo['DB_PASSWORD'],
    }
}