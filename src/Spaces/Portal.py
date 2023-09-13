from typing import TypedDict, List
from ..Types import PublicKeyType, uPOKTType, ServiceURLType

portal_registration_space = TypedDict("Portal Registration Space", {"public_key": PublicKeyType, # The public cryptographic id of the Application
                                                                "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the Web3 service is provided
                                                                })