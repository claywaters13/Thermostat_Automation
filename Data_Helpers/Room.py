import time

from External_Utilities import Particle_API


class Room:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self._data_refresh_s = 20
        self._temp_check = time.time() - 2 * self._data_refresh_s
        self._saved_temp = 0

    @property
    def temp(self):

        # Update data if it's been data_refresh_s seconds since the last time data was pulled
        should_request_new_temperatures = (time.time() > self._temp_check + self._data_refresh_s)

        if should_request_new_temperatures:
            response = Particle_API.ParticleApi()
            temp_f = response.device_data(self.id, 'ROOMtempf').json()['result']
            temp_c = (temp_f - 32) * 5 / 9
            self._saved_temp = temp_c
            self._temp_check = time.time()

        return round(self._saved_temp, 2)


