from .Dummy import dummy_state
from .Servicer import servicer_state
from .Fisherman import fisherman_state
from .Application import application_state

state = {"Dummy": dummy_state,
         "Servicer": servicer_state,
         "Fisherman": fisherman_state,
         "Application": application_state}
