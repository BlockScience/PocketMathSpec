from ..Spaces import (
    gateway_relay_request_space,
    gateway_registration_space,
    modify_gateway_pokt_space,
    gateway_unregistration_space,
    application_undelegation_space,
    gateway_stake_status_space,
    return_gateway_stake_space,
    submit_relay_request_space,
)

submit_relay_request_gateway_policy = {
    "name": "Submit Relay Request (Gateway) Policy",
    "description": "Policy which handles the logic of gateway relay requests and fees",
    "constraints": [],
    "policy_options": [],
    "domain": [gateway_relay_request_space],
    "codomain": [submit_relay_request_space, submit_relay_request_space],
    "parameters_used": [
        "gateway_bootstrap_unwind_start",
        "gateway_bootstrap_unwind_end",
        "min_bootstrap_gateway_fee_per_relay",
        "maturity_relay_charge",
        "maturity_relay_cost",
    ],
}


gateway_registration_policy = {
    "name": "Gateway Registration Policy",
    "description": "Policy which handles the logic of gateway registration and if enough stake is present. The gateway is also added to the global state if it is approved.",
    "constraints": [],
    "policy_options": [],
    "domain": [gateway_registration_space],
    "codomain": [
        modify_gateway_pokt_space,
        modify_gateway_pokt_space,
        gateway_registration_space,
    ],
    "parameters_used": ["gateway_minimum_stake"],
}

gateway_unregistration_policy = {
    "name": "Gateway Unregistration Policy",
    "description": "Policy which handles the logic of gateway unregistration process. It will set the stake status and remove any references to the gateway in terms of delegation.",
    "constraints": [],
    "policy_options": [],
    "domain": [gateway_unregistration_space],
    "codomain": [gateway_stake_status_space, application_undelegation_space],
    "parameters_used": [],
}


return_gateway_stake_policy = {
    "name": "Return Gateway Stake Policy",
    "description": "The policy which determines when a gateway can have their stake returned.",
    "constraints": [],
    "policy_options": [],
    "domain": [return_gateway_stake_space],
    "codomain": [
        gateway_stake_status_space,
        modify_gateway_pokt_space,
        modify_gateway_pokt_space,
    ],
    "parameters_used": ["gateway_unstaking_time"],
}
