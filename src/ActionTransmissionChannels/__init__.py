from .Servicer import servicer_transmission_channels
from .Application import application_transmission_channels

# from .Validator import validator_transmission_channels
from .System import system_transmission_channels
from .Portal import portal_transmission_channels
from .Service import service_transmission_channels

action_transmission_channels = []
action_transmission_channels.extend(servicer_transmission_channels)
action_transmission_channels.extend(application_transmission_channels)
# action_transmission_channels.extend(validator_transmission_channels)
action_transmission_channels.extend(system_transmission_channels)
action_transmission_channels.extend(portal_transmission_channels)
action_transmission_channels.extend(service_transmission_channels)
