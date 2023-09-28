from ..Types import POKTType, Days, PercentType

validator_parameter_set = {"name": "Validator Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": PercentType,
                                       "name": "block_proposer_allocation",
                                       "description": "The percent allocation of fees charged to portals and applications that goes to the validator.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       ]}

"""{"variable_type": POKTType,
                                       "name": "minimum_validator_stake",
                                       "description": "The minimum required stake for validators",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": Days,
                                       "name": "minimum_validator_pause_time",
                                       "description": "The minimum time a validator has to be paused for before they can be unpaused",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": int,
                                       "name": "max_validators",
                                       "description": "The maximum number of validators allowed at any given time",
                                       "symbol": None,
                                       "domain": None
                                       },"""