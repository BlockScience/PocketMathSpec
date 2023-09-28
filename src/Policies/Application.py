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
                        "parameters_used": ["minimum_servicers_per_session", "maximum_servicers_per_session",
                                            "minimum_application_stake"]}

set_application_parameters_policy_option_v1 = {"name": "Set Application Parameters Policy Option V1",
                                 "description": "This policy determines if the parameters of an application should be updated and if so executes on it.",
                                 "logic": "As long as the application has a staking amount equal to or greater than the current staked amount and as well the passed NumServicers is bounded between MinServicersPerSession and MaxServicersPerSession, the application will have its parameters all updated. "
                                 }

set_application_parameters_policy = {"name": "Set Application Parameters Policy",
                        "description": "Policy for determining if application parameters should be updated",
                        "constraints": ["DOMAIN[0].number_servicers >= PARAMS.MinServicersPerSession",
                                        "DOMAIN[0].number_servicers <= PARAMS.MaxServicersPerSession"],
                        "policy_options": [set_application_parameters_policy_option_v1],
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