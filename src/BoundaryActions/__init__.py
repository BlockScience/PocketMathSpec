from .Servicer import (
    servicer_stake,
    servicer_pause,
    servicer_unpause,
    servicer_unstake,
    servicer_relay,
    unjail_node,
)
from .Application import (
    application_stake,
    application_unstake,
    application_delegate_to_gateway,
    application_undelegation,
    submit_relay_request,
)

# from .Validator import validator_stake, validator_pause, validator_unstake, validator_unpause, become_validator
from .Gateway import (
    gateway_registration,
    gateway_unregistration,
    submit_relay_request_gateway,
)
from .System import burn_pokt
from .Service import service_join, service_leave

boundary_actions = {
    "Servicer Stake": servicer_stake,
    "Servicer Pause": servicer_pause,
    "Servicer Unpause": servicer_unpause,
    "Servicer Unstake": servicer_unstake,
    "Application Stake": application_stake,
    "Application Unstake": application_unstake,
    "Application Delegate to Gateway": application_delegate_to_gateway,
    # "Validator Stake": validator_stake,
    "Gateway Registration": gateway_registration,
    "Gateway Unregistration": gateway_unregistration,
    "Application Undelegation": application_undelegation,
    # "Validator Pause": validator_pause,
    # "Validator Unstake": validator_unstake,
    # "Validator Unpause": validator_unpause,
    # "Become Validator": become_validator,
    "Submit Relay Request": submit_relay_request,
    "Servicer Relay": servicer_relay,
    "Burn POKT": burn_pokt,
    "Unjail Node": unjail_node,
    "Service Join": service_join,
    "Service Leave": service_leave,
    "Submit Relay Request (Gateway)": submit_relay_request_gateway,
}
