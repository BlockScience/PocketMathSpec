from ..Types import PercentType, USDType, NumberRelaysPerDayType

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
                                       },
                                       {"variable_type": USDType,
                                       "name": "maturity_relay_cost",
                                       "description": "This is set based on the understanding that we should pay servicers/validators/the DAO, etc less than we charge gateways at scale",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": USDType,
                                       "name": "maturity_relay_charge",
                                       "description": "This is set at 30% of Infura's average price per relay",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": USDType,
                                       "name": "min_bootstrap_gateway_fee_per_relay",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": USDType,
                                       "name": "max_bootstrap_servicer_cost_per_relay",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberRelaysPerDayType,
                                       "name": "servicer_bootstrap_unwind_start",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberRelaysPerDayType,
                                       "name": "servicer_bootstrap_end",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberRelaysPerDayType,
                                       "name": "gateway_bootstrap_unwind_start",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": NumberRelaysPerDayType,
                                       "name": "gateway_bootstrap_unwind_end",
                                       "description": "",
                                       "symbol": None,
                                       "domain": None
                                       }
                                       ]}

