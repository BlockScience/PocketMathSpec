from ..Spaces import (application_stake_space, modify_application_pokt_space, application_param_update_space,
                      application_delegate_to_portal_space, application_unstake_space, submit_relay_request_space,
                      application_undelegation_space, return_application_stake_space)

application_stake_policy = {"name": "Application Stake Policy",
                        "description": "The policy which takes care of whether an application can stake and if it should update parameters.",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",
                                        "LEN(DOMAIN[0].services) > 0",
                                        "All chains in DOMAIN[0].services must be valid",
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
                        "codomain": [application_delegate_to_portal_space, application_delegate_to_portal_space],
                        "parameters_used": ["stake_per_app_delegation"]}

application_unstake_policy = {
    "name": "Application Unstake Policy",
    "description": "The policy for determining what happens when an application unstakes.",
    "constraints": [],
    "policy_options": [],
    "domain": [application_unstake_space],
    "codomain": [],
    "parameters_used": []}

submit_relay_request_policy_option_v1 = {"name": "Submit Relay Request Policy Option V1",
                                 "description": "V1 Implementation",
                                 "logic": """During each Session, the amount of POKT an Application has staked (see Application Protocol for more details) is mapped to "Service Tokens" that represent the amount of work a Servicer can provide using the SessionTokenBucketCoefficient governance parameter. The Token Bucket rate limiting algorithm is used to determine the maximum number of requests a Servicer can relay, and be rewarded for, thereby disincentivizing it to process relays for the Application once the cap is reached.

At the beginning of the session, each Servicer initializes: AppSessionTokens = (AppStakeAmount * SessionTokenBucketCoefficient) / NumServicersPerSession. When one of the Servicers in the session is out of session tokens, the Application can continue to use other Servicers until every they are all exhausted.

The mechanism described above enables future iterations of the protocol where different types of request may vary the required number of AppSessionTokens per request."""
                                 }

submit_relay_request_policy = {
    "name": "Submit Relay Request Policy",
    "description": "The policy for determining aspects of the service request.",
    "constraints": [],
    "policy_options": [submit_relay_request_policy_option_v1],
    "domain": [submit_relay_request_space],
    "codomain": [],
    "parameters_used": ["session_token_bucket_coefficient"]}


application_undelegate_to_portal_policy = {"name": "Application Undelegate to Portal Policy",
                        "description": "Policy for taking care of any actions in relation to undelegation.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [application_undelegation_space],
                        "codomain": [application_undelegation_space, application_undelegation_space],
                        "parameters_used": []}

return_application_stake_policy = {
    "name": "Return Application Stake Policy",
    "description": "The policy which determines when an application can have their stake returned.",
    "constraints": [],
    "policy_options": [],
    "domain": [return_application_stake_space],
    "codomain": [application_stake_space, modify_application_pokt_space, modify_application_pokt_space],
    "parameters_used": ["application_unstaking_time"]}