from ..Types import POKTType, Days

validator_parameter_set = {"name": "Validator Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": POKTType,
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
                                       }]}

