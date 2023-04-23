from environs import Env

env = Env()
env.read_env()

DEBUG = env.str('DEBUG')
DJANGO_SECRET_KEY = env.str('DJANGO_SECRET_KEY')