from ..Spaces import  modify_application_pokt_space, application_param_update_space


modify_application_pokt_holdings = {"name": "Modify Application POKT Holdings",
                           "description": "The mechanism to update the personal holdings of an application",
                           "constraints": [],
                           "logic": "The application at DOMAIN[0].application_address has its POKT Holdings modified by DOMAIN[0].value",
                           "domain": [modify_application_pokt_space],
                           "parameters_used": []}

modify_application_stake = {"name": "Modify Application Stake",
                           "description": "The mechanism to update the stake of an application",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].application_address has its stake modified by DOMAIN[0].value",
                           "domain": [modify_application_pokt_space],
                           "parameters_used": []}


update_application_params = {"name": "Update Application Params",
                           "description": "The mechanism which updates application params",
                           "constraints": [],
                           "logic": "The application at DOMAIN[0].public_key has its params updated",
                           "domain": [application_param_update_space],
                           "parameters_used": []}

