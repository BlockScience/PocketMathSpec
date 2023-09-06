from typing import TypedDict, List
from ..Types import PublicKeyType, uPOKTType, RelayChainType, GeoZoneType

application_stake_space = TypedDict("Application Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the Application
                                                                "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                                "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                                "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                                "number_servicers": int, # The number of Servicers requested per session
                                                                })