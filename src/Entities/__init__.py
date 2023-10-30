from .Servicer import servicer_entity
from .Watcher import Watcher_entity
from .Application import application_entity
from .Validator import validator_entity
from .Portal import portal_entity
from .Service import service_entity
from .Global import global_entity
from .DAO import dao_entity

entities = {
    "Servicer": servicer_entity,
    "Watcher": Watcher_entity,
    "Application": application_entity,
    "Validator": validator_entity,
    "Portal": portal_entity,
    "Service": service_entity,
    "Global": global_entity,
    "DAO": dao_entity,
}
