import os
from twilio.rest import Client

from Configuration import env_vars

env_vars.set_env_vars()


class TwilioClient:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        self.phone_numbers = [os.environ['Main_Phone_Number']]

    def send_failed_loop_text(self, num_failures):
        for number in self.phone_numbers:
            self.client.api.account.messages.create(
                body=f'Thermostat loop has failed {num_failures} times... you might want to fix it',
                from_='+12244343786',
                to=number
            )

    def send_loop_resume_text(self):
        for number in self.phone_numbers:
            self.client.api.account.messages.create(
                body=f'Thermostat loop has resumed operation, no need to worry',
                from_='+12244343786',
                to=number
            )
