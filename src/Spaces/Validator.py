from ..Types import PublicKeyType, uPOKTType, ServiceURLType, RelayChainType, GeoZoneType, ActorType, AddressType, BlockHeightType
from typing import TypedDict, List

validator_stake_space = TypedDict("Validator Stake Space", {"public_key": PublicKeyType, # The public cryptographic id of the custodial account
                                                          "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the validator service is provided
                                                          "operator_public_key": PublicKeyType # OPTIONAL; The non-custodial pubKey operating this node
})