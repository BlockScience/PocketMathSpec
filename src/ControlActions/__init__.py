from .Servicer import assign_servicer_salary, return_servicer_stake
from .Validator import validator_stake_burning, validator_unstake_forced, validator_jailed, validator_block_reward
from .Treasury import mint_block_rewards, jail_node
from .Application import return_application_stake

control_actions = {
    "Assign Servicer Salary": assign_servicer_salary,
    "Validator Stake Burning": validator_stake_burning,
    "Validator Unstake Forced": validator_unstake_forced,
    "Validator Jailed": validator_jailed,
    "Validator Block Reward": validator_block_reward,
    "Mint Block Rewards": mint_block_rewards,
    "Jail Node": jail_node,
    "Return Servicer Stake": return_servicer_stake,
    "Return Application Stake": return_application_stake
}
