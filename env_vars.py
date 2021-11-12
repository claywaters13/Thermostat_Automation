import os


def set_env_vars():
    #  Twilio Env Variables
    os.environ['TWILIO_ACCOUNT_SID'] = 'add your twilio account sid here'
    os.environ['TWILIO_AUTH_TOKEN'] = 'add your twilio auth token here'
    os.environ['Main_Phone_Number'] = 'add your phone number for alerting here'

    #  Particle Env Variables
    os.environ['Particle_Username'] = 'add your particle username here'
    os.environ['Particle_Password'] = 'add your particle password here'
