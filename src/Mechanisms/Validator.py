from ..Spaces import  modify_validator_pokt_space, validator_param_update_space


modify_validator_pokt_holdings = {"name": "Modify Validator POKT Holdings",
                           "description": "The mechanism to update the personal holdings of a validator",
                           "constraints": [],
                           "logic": "The validator at DOMAIN[0].public_key has its POKT Holdings modified by DOMAIN[0].value",
                           "domain": [modify_validator_pokt_space],
                           "parameters_used": []}

modify_validator_stake = {"name": "Modify Validator Stake",
                           "description": "The mechanism to update the stake of a validator",
                           "constraints": [],
                           "logic": "The validator at DOMAIN[0].public_key has its stake modified by DOMAIN[0].value",
                           "domain": [modify_validator_pokt_space],
                           "parameters_used": []}


update_validator_params = {"name": "Update Validator Params",
                           "description": "The mechanism which updates validator params",
                           "constraints": [],
                           "logic": "The validator at DOMAIN[0].public_key has its params updated",
                           "domain": [validator_param_update_space],
                           "parameters_used": []}

