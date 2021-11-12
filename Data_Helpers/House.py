from Configuration import env_vars
from External_Utilities import Particle_API
from Data_Helpers import Room


env_vars.set_env_vars()


class House:
    def __init__(self, config):
        self.rooms = []
        self._thermostat_id = []

        self._create_rooms_from_config(config)
        self._create_thermostat_connection_from_config(config)

    def send_command_to_thermostat(self, action):
        """
        Valid Actions =
            'Heat'
            'Cool'
            'Circulate'
            'Do_Nothing'
        """
        Particle_API.ParticleApi().send_command(self._thermostat_id, action)

    def _create_rooms_from_config(self, config):
        for room in config['DEVICES']['ROOMS']:
            name = config['DEVICES']['ROOMS'][room]['NAME']
            id = config['DEVICES']['ROOMS'][room]['PARTICLE_ID']
            self.rooms.append(Room.Room(name, id))

    def _create_thermostat_connection_from_config(self, config):
        self._thermostat_id = config['DEVICES']['THERMOSTAT']['PARTICLE_ID']









