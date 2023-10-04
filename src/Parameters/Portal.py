from ..Types import POKTType, NumberOfBlocksType

portal_parameter_set = {"name": "Portal Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": POKTType,
                                       "name": "stake_per_app_delegation",
                                       "description": "The amount of stake needed per application that is delegating to the portal.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": POKTType,
                                       "name": "portal_fee_per_relay",
                                       "description": "The fee per relay to portals.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": POKTType,
                                       "name": "portal_minimum_stake",
                                       "description": "The minimum stake for the portal, starting at 150,000 POKT.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberOfBlocksType,
                                       "name": "portal_unstaking_time",
                                       "description": "The time before a portal has their stake returned.",
                                       "symbol": None,
                                       "domain": None
                                       },]}