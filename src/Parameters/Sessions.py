from ..Types import NumberOfBlocksType

session_parameter_set = {"name": "Session Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": NumberOfBlocksType,
                                       "name": "session_block_frequency",
                                       "description": "The number of blocks a session can extend over",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": float,
                                       "name": "session_token_bucket_coefficient",
                                       "description": "Parameter for converting application stake to service tokens",
                                       "symbol": None,
                                       "domain": None
                                       }]}
