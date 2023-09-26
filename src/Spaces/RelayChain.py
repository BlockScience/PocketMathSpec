from typing import TypedDict

relay_chain_join_space = TypedDict("Relay Chain Join Space", {"name": str,
                                                              "portal_api_prefix": str,
                                                              "relay_chain_id": str})
relay_chain_leave_space = TypedDict("Relay Chain Leave Space", {"relay_chain_id": str})


