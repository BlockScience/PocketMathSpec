from .Servicer import servicer_state
from .Fisherman import fisherman_state
from .Application import application_state
from .Validator import validator_state
from .Portal import portal_state
from .Treasury import treasury_state

state = {"Servicer": servicer_state,
         "Fisherman": fisherman_state,
         "Application": application_state,
         "Validator": validator_state,
         "Portal": portal_state,
         "Treasury": treasury_state}
