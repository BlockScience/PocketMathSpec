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
                                       },
                                       {"variable_type": Days,
                                       "name": "minimum_pause_time",
                                       "description": "The minimum required period of time that a servicer has to be paused for before being able to be unpaused.",
                                       "symbol": None,
                                       "domain": None},
                                       {"variable_type": int,
                                       "name": "max_chains_servicer",
                                       "description": "When staking as a servicer, every servicer must register their stake for the relay chains that they support. Currently, servicers can register each stake to apply to their work in up to 15 different blockchains, which is the maximum number that can be chosen. ",
                                       "symbol": None,
                                       "domain": None}]}