from ..Types import POKTType, NumberOfBlocksType

application_parameter_set = {"name": "Application Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": int,
                                       "name": "minimum_servicers_per_session",
                                       "description": "The minimum servicers per session",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": int,
                                       "name": "maximum_servicers_per_session",
                                       "description": "The maximum servicers per session.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberOfBlocksType,
                                       "name": "application_unstaking_time",
                                       "description": "The time before an application has their stake returned.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": POKTType,
                                       "name": "application_fee_per_relay",
                                       "description": "The fee charged per relay to applications.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": POKTType,
                                       "name": "minimum_application_stake",
                                       "description": "The minimum stake needed for applications.",
                                       "symbol": None,
                                       "domain": None},
                                       {"variable_type": POKTType,
                                       "name": "app_burn_per_session",
                                       "description": "The amount of POKT burned per session initiated. Please note this is outside of the payments for services and serves as a potential parameter to toggle for deflation.",
                                       "symbol": None,
                                       "domain": None},
                                       {"variable_type": POKTType,
                                       "name": "app_burn_per_relay",
                                       "description": "The amount of POKT burned per relay. Please note this is outside of the payments for services and serves as a potential parameter to toggle for deflation.",
                                       "symbol": None,
                                       "domain": None}
                                       ]}


