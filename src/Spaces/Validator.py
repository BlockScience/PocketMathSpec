from ..Types import PublicKeyType, uPOKTType, ServiceURLType, RelayChainType, GeoZoneType, ActorType, AddressType, BlockHeightType
from typing import TypedDict, List

validator_stake_space = TypedDict("Validator Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the validator service is provided
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})

modify_validator_pokt_space = TypedDict("Modify Validator POKT Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "amount": uPOKTType, # The amount of uPOKT to modify by
})

validator_param_update_space = TypedDict("Validator Param Update Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "service_url": ServiceURLType, # The API endpoint where the Web3 service is provided
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})

validator_pause_space = TypedDict("Validator Pause Space", {"actor_type": ActorType,
                                                              "address": AddressType,
                                                              "caller_address": AddressType, # Who called for the validator to be paused
                                                              "signer": AddressType,})

#TODO


validator_stake_burning_space = TypedDict("Validator Stake Burning Space", {})
validator_unstake_space = TypedDict("Validator Unstake Space", {})
validator_unpause_space = TypedDict("Validator Unpause Space", {})
validator_jail_space = TypedDict("Validator Jail Space", {})
become_validator_space = TypedDict("Become Validator Space", {})
validator_block_reward_space = TypedDict("Validator Block Reward Space", {})