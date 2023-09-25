from .Servicer import (servicer_stake_policy, set_servicer_parameters_policy, servicer_unpause_policy,
                       servicer_pause_policy, assign_servicer_salary_policy, servicer_block_reward_policy,
                       servicer_relay_policy, servicer_stake_burn_policy)
from .Application import application_stake_policy, set_application_parameters_policy, application_delegate_to_portal_policy
from .Validator import validator_stake_policy, set_validator_parameters_policy, validator_unpause_policy, validator_block_reward_policy
from .Treasury import block_reward_policy_aggregate
from .DAO import dao_block_reward_policy
from .Portal import submit_relay_request_portal_policy

policies = {
    "Servicer Stake Policy": servicer_stake_policy,
    "Set Servicer Parameters Policy": set_servicer_parameters_policy,
    "Servicer Unpause Policy": servicer_unpause_policy,
    "Application Stake Policy": application_stake_policy,
    "Set Application Parameters Policy": set_application_parameters_policy,
    "Servicer Pause Policy": servicer_pause_policy,
    "Validator Stake Policy": validator_stake_policy,
    "Set Validator Parameters Policy": set_validator_parameters_policy,
    "Validator Unpause Policy": validator_unpause_policy,
    "Assign Servicer Salary Policy": assign_servicer_salary_policy,
    "Application Delegate to Portal Policy": application_delegate_to_portal_policy,
    "Servicer Block Reward Policy": servicer_block_reward_policy,
    "Block Reward Policy Aggregate": block_reward_policy_aggregate,
    "Validator Block Reward Policy": validator_block_reward_policy,
    "DAO Block Reward Policy": dao_block_reward_policy,
    "Submit Relay Request (Portal) Policy": submit_relay_request_portal_policy,
    "Servicer Relay Policy": servicer_relay_policy,
    "Servicer Stake Burn Policy": servicer_stake_burn_policy
}
