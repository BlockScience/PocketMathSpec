from .Servicer import servicer_state
from .Watcher import Watcher_state
from .Application import application_state
from .Validator import validator_state
from .Portal import portal_state
from .Service import service_state
from .Global import global_state
from .DAO import dao_state

state = {
    "Global": global_state,
    "Servicer": servicer_state,
    "Watcher": Watcher_state,
    "Application": application_state,
    "Validator": validator_state,
    "Portal": portal_state,
    "Service": service_state,
    "DAO": dao_state,
}
