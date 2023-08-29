from ..Types import POKTType, Days

servicer_parameter_set = {"name": "Servicer Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": POKTType,
                                       "name": "minimum_stake_servicer",
                                       "description": "The minimum required stake for servicers, default is 15K",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": Days,
                                       "name": "minimum_stake_period_servicer",
                                       "description": "The minimum required period of time that a servicer has to be staked for, default is 21 days.",
                                       "symbol": None,
                                       "domain": None
                                       }]}