from ..Types import PublicKeyType, uPOKTType, ServiceURLType, RelayChainType, GeoZoneType, ActorType, AddressType, BlockHeightType
from typing import TypedDict, List

servicer_stake_space = TypedDict("Servicer Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the Web3 service is provided
                                                          "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                          "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})


modify_servicer_pokt_space = TypedDict("Modify Servicer POKT Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "amount": uPOKTType, # The amount of uPOKT to modify by
})


servicer_param_update_space = TypedDict("Servicer Param Update Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "service_url": ServiceURLType, # The API endpoint where the Web3 service is provided
                                                          "relay_chains": List[RelayChainType], # The flavor(s) of Web3 hosted by this Servicer
                                                          "geo_zone": GeoZoneType, # The physical geo-location identifier this Servicer registered in
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})


servicer_unpause_space = TypedDict("Servicer Unpause Space", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "signer": AddressType,})

# For recording the height of the block at which unpause happens
servicer_unpause_space2 = TypedDict("Servicer Unpause Space 2", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "signer": AddressType,
                                                              "block_height": BlockHeightType})

servicer_unstake_space = TypedDict("Servicer Unstake Space", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "signer": AddressType,})

#TODO
servicer_pause_space = TypedDict("Servicer Pause Space", {})

assign_servicer_salary_space = TypedDict("Assign Servicer Salary Space", {})
