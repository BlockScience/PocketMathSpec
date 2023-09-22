from ..Types import PercentType

treasury_parameter_set = {"name": "Treasury Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": PercentType,
                                       "name": "dao_fee_percentage",
                                       "description": "The percentage of block rewards that goes to the DAO",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": PercentType,
                                       "name": "validator_fee_percentage",
                                       "description": "The percentage of block rewards that goes to the validators",
                                       "symbol": None,
                                       "domain": None
                                       }]}
