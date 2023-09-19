from ..Spaces import application_stake_space, modify_application_pokt_space, application_param_update_space, application_delegate_to_portal_space

application_stake_policy = {"name": "Application Stake Policy",
                        "description": "The policy which takes care of whether an application can stake and if it should update parameters.",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",
                                        "LEN(DOMAIN[0].relay_chains) > 0",
                                        "All chains in DOMAIN[0].relay_chains must be valid",
                                        "DOMAIN[0].number_servicers >= PARAMS.MinServicersPerSession",
                                        "DOMAIN[0].number_servicers <= PARAMS.MaxServicersPerSession"],
                        "policy_options": [],
                        "domain": [application_stake_space],
                        "codomain": [application_stake_space, modify_application_pokt_space, modify_application_pokt_space],
                        "parameters_used": ["minimum_servicers_per_session", "maximum_servicers_per_session"]}

set_application_parameters_policy = {"name": "Set Application Parameters Policy",
                        "description": "Policy for determining if application parameters should be updated",
                        "constraints": ["DOMAIN[0].number_servicers >= PARAMS.MinServicersPerSession",
                                        "DOMAIN[0].number_servicers <= PARAMS.MaxServicersPerSession"],
                        "policy_options": [],
                        "domain": [application_stake_space],
                        "codomain": [application_param_update_space],
                        "parameters_used": ["minimum_servicers_per_session", "maximum_servicers_per_session"]}

application_delegate_to_portal_policy = {"name": "Application Delegate to Portal Policy",
                        "description": "Policy for determining if application is able to delegate to a portal. The stake_per_app_delegation parameter, current stake of the portal, and current number of delegators will be used in determining if the portal is able to support the addition of this specific delegation.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [application_delegate_to_portal_space],
                        "codomain": [application_delegate_to_portal_space],
                        "parameters_used": ["stake_per_app_delegation"]}