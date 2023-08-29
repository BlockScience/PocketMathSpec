from ..Types import PublicKeyType, uPOKTType, ServiceURLType, RelayChainType, GeoZoneType
from typing import TypedDict, List

servicer_stake_space = TypedDict("Servicer Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the Web3 service is provided
                                                          "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                          "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})


#TODO
servicer_pause_space = TypedDict("Servicer Pause Space", {})
servicer_unpause_space = TypedDict("Servicer Unpause Space", {})
assign_servicer_salary_space = TypedDict("Assign Servicer Salary Space", {})