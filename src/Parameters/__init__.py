from .Servicer import servicer_parameter_set
from .Application import application_parameter_set
from .Validator import validator_parameter_set
from .Gateway import gateway_parameter_set
from .Sessions import session_parameter_set
from .System import system_parameter_set
from .Service import service_parameter_set

parameters = {
    "Servicer": servicer_parameter_set,
    "Application": application_parameter_set,
    "Validator": validator_parameter_set,
    "Gateway": gateway_parameter_set,
    "Session": session_parameter_set,
    "System": system_parameter_set,
    "Service": service_parameter_set,
}
