from decouple import config
import os



BASE_DIR = os.path.dirname(os.path.realpath(__file__));

class Config : 
    Secret_Key = config('SECRET_KEY');
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI');
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS');


class DevelopmentConfig(Config) : 
    DEBUG = True;
    