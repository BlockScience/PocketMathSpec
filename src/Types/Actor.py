from enum import Enum

class ActorType(Enum):
    ACTOR_TYPE_UNSPECIFIED = 0
    ACTOR_TYPE_APP = 1
    ACTOR_TYPE_SERVICER = 2
    ACTOR_TYPE_FISH = 3
    ACTOR_TYPE_VAL = 4

class StakeStatusType(Enum):
   UnknownStatus = 0
   Unstaking = 1
   Staked = 2
   Unstaked = 3