import os
from retry_requests import retry

from Configuration import env_vars

env_vars.set_env_vars()
Particle_Username = os.environ["Particle_Username"]
Particle_Password = os.environ["Particle_Password"]

my_session = retry()


class ParticleApi:

    def __init__(self):
        self.auth_url = "https://api.particle.io/oauth/token"
        self.devices_url = "https://api.particle.io/v1/devices"
        self.username = Particle_Username
        self.password = Particle_Password
        self.token = self._get_token()
        # self.device_info = self._get_device_info()
        # self.device_names = self.device_info['name'].tolist()

    def _get_token(self):
        """
        Get access token using username and pw
        :return: string
        """
        data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password
        }

        response = my_session.post(self.auth_url, data=data, auth=('particle', 'particle'))

        if response.status_code != 200:
            print("request sent - response:", response)
            print("response content", response.content)

        return response.json()['access_token']

    # def _get_device_info(self):
    #     """
    #     Get a list of all devices on the particle platform, including
    #     ids, available variables, and available functions
    #     :return: dataframe
    #     """
    #     response = my_session.get(self.devices_url, params={"access_token": self.token})
    #
    #     devices = defaultdict(list)
    #     for device in response.json():
    #         devices["name"].append(device["name"])
    #         devices["id"].append(device["id"])
    #         devices["variables"].append(device["variables"])
    #         devices["functions"].append(device["functions"])
    #
    #     df = pd.DataFrame(data=devices).sort_values(by=["name"])
    #
    #     return df

    def device_data(self, device_id, variable_name):
        """
        Get a specific variable value from a specific device
        :param device_id: string
        :param variable_name: string
        :return: json response
        """

        url = f"{self.devices_url}/{device_id}/{variable_name}"

        response = my_session.get(url, params={"access_token": self.token})

        if response.status_code != 200:
            print("request sent - response:", response)
            print("response content", response.content)

        return response

    def send_command(self, device, command):
        """
        Send a specific command to a specific device
        :param device: string
        :param command: string
        :return: nothing
        """

        url = f"{self.devices_url}/%s/{command}"

        response = my_session.post(url % device, data={'access_token': self.token})

        if response.status_code != 200:
            print("request sent - response:", response)
            print("response content", response.content)


# -------------------------------------
#
#  Test if running this module directly
#
# -------------------------------------

if __name__ == '__main__':

    # # Print All Devices
    # print("Printing ALl Connected Particle Devices \n", ParticleApi().device_info.to_string())

    # Print a Room Temp
    print("Office Room Temp (F) =", ParticleApi().device_data("270032000147373334323233", 'ROOMtempf').json()['result'])

    # Print a relay status
    print("Fan Status =", ParticleApi().device_data("2a0036001947393035313138", 'Fan Status:').json()['result'])

