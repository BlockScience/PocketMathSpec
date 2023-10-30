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
    application_delegate_to_portal,
    application_undelegation,
    submit_relay_request,
)

# from .Validator import validator_stake, validator_pause, validator_unstake, validator_unpause, become_validator
from .Portal import (
    portal_registration,
    portal_unregistration,
    submit_relay_request_portal,
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
    "Application Delegate to Portal": application_delegate_to_portal,
    # "Validator Stake": validator_stake,
    "Portal Registration": portal_registration,
    "Portal Unregistration": portal_unregistration,
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
    "Submit Relay Request (Portal)": submit_relay_request_portal,
}
