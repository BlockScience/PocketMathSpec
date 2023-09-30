from typing import NewType, TypedDict, List
from .Entity import ServiceEntityType, ApplicationEntityType, ServicerEntityType, FishermanEntityType
from .Primitives import GeoZoneType

SessionType = NewType('Session', TypedDict('Session', {"id": str, # a universally unique ID for the session
                                                       "session_number": int, # a monotonically increasing number representing the # on the chain
                                                       "session_height": int, # the height at which the session starts
                                                       "num_session_blocks": int, # the number of blocks the session is valid from
                                                       "service": ServiceEntityType, # the service the session is valid for
                                                       "geo_zone": GeoZoneType, # the target geographic region where the actors are present
                                                       "application": ApplicationEntityType, # the application that is being served
                                                       "servicers": List[ServicerEntityType], #  the set of servicers that are serving the application
                                                       "fishermen": List[FishermanEntityType], # the set of fishermen that are fishing for servicers
                                                       }))

