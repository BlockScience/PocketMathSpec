from ..Types import (PublicKeyType, uPOKTType, ServiceURLType, RelayChainType,
                     GeoZoneType, ActorType, AddressType, BlockHeightType, StakeStatusType)
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

servicer_pause_space = TypedDict("Servicer Pause Space", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "caller_address": AddressType, # Who called for the servicer to be paused
                                                              "signer": AddressType,})
servicer_pause_space2 = TypedDict("Servicer Pause Space 2", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "caller_address": AddressType, # Who called for the servicer to be paused
                                                              "signer": AddressType,})

servicer_unstake_space = TypedDict("Servicer Unstake Space", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "signer": AddressType,})


assign_servicer_salary_space = TypedDict("Assign Servicer Salary Space", {"geo_zone": GeoZoneType, # The physical geo-location identifier
                                                                          "relay_chain": RelayChainType,
                                                                          "height": BlockHeightType})


return_servicer_stake_space = TypedDict("Return Servicer Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "amount": uPOKTType})

servicer_block_reward_space = TypedDict("Servicer Block Reward Space", {"public_key": PublicKeyType, # The key of the servicer that is receiving the block reward
                                                                        "number_of_relays": int, # The number of relays that the servicer completed
                                                                        "usage_to_reward_coeffecient": float, # The scalar for rewards to the servicers
                                                                        })
servicer_forced_unstake_space = TypedDict("Servicer Forced Unstaked Space", {"public_key": PublicKeyType, # The key of the servicer that is being force unstaked
                                                                        })

servicer_stake_status_space = TypedDict("Servicer Stake Status Space", {"address": PublicKeyType, # address of the unstaking servicer
                                                                        "height": BlockHeightType,
                                                                        "status": StakeStatusType
                                                                        })



#TODO



servicer_relay_space = TypedDict("Servicer Relay Space", {})
servicer_stake_burn_space = TypedDict("Servicer Stake Burn Space", {})