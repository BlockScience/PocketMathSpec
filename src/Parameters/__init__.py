from .Servicer import servicer_parameter_set
from .Application import application_parameter_set
from .Validator import validator_parameter_set
from .Portal import portal_parameter_set
from .Sessions import session_parameter_set

parameters = {"Servicer": servicer_parameter_set,
              "Application": application_parameter_set,
              "Validator": validator_parameter_set,
              "Portal": portal_parameter_set,
              "Session": session_parameter_set}

