from .Servicer import (
    servicer_stake_policy,
    set_servicer_parameters_policy,
    servicer_unpause_policy,
    servicer_pause_policy,
    assign_servicer_salary_policy,
    servicer_relay_policy,
    servicer_stake_burn_policy,
    servicer_unstake_policy,
    return_servicer_stake_policy,
    burn_per_relay_policy,
    jail_node_policy,
    unjail_node_policy,
    servicer_forced_unstake_policy,
)
from .Application import (
    application_stake_policy,
    set_application_parameters_policy,
    application_delegate_to_gateway_policy,
    application_unstake_policy,
    submit_relay_request_policy,
    application_undelegate_to_gateway_policy,
    return_application_stake_policy,
    burn_per_session_policy,
)

# from .Validator import validator_stake_policy, set_validator_parameters_policy, validator_unpause_policy, validator_block_reward_policy
from .Validator import validator_block_reward_policy
from .System import (
    block_reward_policy_aggregate,
    burn_pokt_policy,
    distribute_fees_policy,
)
from .DAO import dao_block_reward_policy
from .Gateway import (
    submit_relay_request_gateway_policy,
    gateway_registration_policy,
    gateway_unregistration_policy,
    return_gateway_stake_policy,
)
from .Service import service_join_policy, service_leave_policy

policies = {
    "Servicer Stake Policy": servicer_stake_policy,
    "Set Servicer Parameters Policy": set_servicer_parameters_policy,
    "Servicer Unpause Policy": servicer_unpause_policy,
    "Application Stake Policy": application_stake_policy,
    "Set Application Parameters Policy": set_application_parameters_policy,
    "Servicer Pause Policy": servicer_pause_policy,
    # "Validator Stake Policy": validator_stake_policy,
    # "Set Validator Parameters Policy": set_validator_parameters_policy,
    # "Validator Unpause Policy": validator_unpause_policy,
    "Assign Servicer Salary Policy": assign_servicer_salary_policy,
    "Application Delegate to Gateway Policy": application_delegate_to_gateway_policy,
    "Block Reward Policy Aggregate": block_reward_policy_aggregate,
    "Validator Block Reward Policy": validator_block_reward_policy,
    "DAO Block Reward Policy": dao_block_reward_policy,
    "Submit Relay Request (Gateway) Policy": submit_relay_request_gateway_policy,
    "Servicer Relay Policy": servicer_relay_policy,
    "Servicer Stake Burn Policy": servicer_stake_burn_policy,
    "Gateway Registration Policy": gateway_registration_policy,
    "Servicer Unstake Policy": servicer_unstake_policy,
    "Application Unstake Policy": application_unstake_policy,
    "Submit Relay Request Policy": submit_relay_request_policy,
    "Service Join Policy": service_join_policy,
    "Service Leave Policy": service_leave_policy,
    "Application Undelegate to Gateway Policy": application_undelegate_to_gateway_policy,
    "Gateway Unregistration Policy": gateway_unregistration_policy,
    "Return Servicer Stake Policy": return_servicer_stake_policy,
    "Return Application Stake Policy": return_application_stake_policy,
    "Return Gateway Stake Policy": return_gateway_stake_policy,
    "Burn POKT Policy": burn_pokt_policy,
    "Burn Per Session Policy": burn_per_session_policy,
    "Burn Per Relay Policy": burn_per_relay_policy,
    "Distribute Fees Policy": distribute_fees_policy,
    "Jail Node Policy": jail_node_policy,
    "Unjail Node Policy": unjail_node_policy,
    "Servicer Forced Unstake Policy": servicer_forced_unstake_policy,
}
