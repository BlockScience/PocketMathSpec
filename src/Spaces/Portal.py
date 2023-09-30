from typing import TypedDict, List
from ..Types import PublicKeyType, uPOKTType, ServiceURLType

portal_registration_space = TypedDict("Portal Registration Space", {"public_key": PublicKeyType, # The public cryptographic id of the Portal account
                                                                "stake_amount": uPOKTType, # The amount of uPOKT in escrow (i.e. a security deposit)
                                                          "service_url": ServiceURLType, # The API endpoint where the Portal service is provided
                                                                })

portal_unregistration_space = TypedDict("Portal Unregistration Space", {"public_key": PublicKeyType, # The public cryptographic id of the Portal account
                                                                })

portal_relay_request_space = TypedDict("Portal Relay Request Space", {"payload": dict, # the data payload of the request
                                                                      "meta": dict, # metadata for the relay request
                                                                      "proof": dict, # the authentication scheme needed for work
                                                                      "application_address": PublicKeyType,
                                                                      "portal_address": PublicKeyType})
