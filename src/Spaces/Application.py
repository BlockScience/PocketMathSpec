from typing import TypedDict, List
from ..Types import PublicKeyType, uPOKTType, RelayChainType, GeoZoneType

application_stake_space = TypedDict("Application Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the Application
                                                                "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                                "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                                "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                                "number_servicers": int, # The number of Servicers requested per session
                                                                })


modify_application_pokt_space = TypedDict("Modify Application POKT Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "amount": uPOKTType, # The amount of uPOKT to modify by
})


application_param_update_space = TypedDict("Application Param Update Space", {"public_key": PublicKeyType, # The public cryptographic id of the Application
                                                                "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                                "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                                "number_servicers": int, # The number of Servicers requested per session
                                                                })


# TODO

application_unstake_space = TypedDict("Application Unstake Space", {})
application_delegate_to_portal_space = TypedDict("Application Delegate to Portal Space", {})