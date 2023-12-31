from .Servicer import (
    return_servicer_stake,
    servicer_stake_burn,
    servicer_forced_unstake,
)

# from .Validator import validator_stake_burning, validator_unstake_forced, validator_jailed, validator_block_reward
from .System import mint_block_rewards, jail_node, distribute_fees
from .Application import return_application_stake
from .Gateway import return_gateway_stake

control_actions = {
    # "Validator Stake Burning": validator_stake_burning,
    # "Validator Unstake Forced": validator_unstake_forced,
    # "Validator Jailed": validator_jailed,
    # "Validator Block Reward": validator_block_reward,
    "Mint Block Rewards": mint_block_rewards,
    "Jail Node": jail_node,
    "Return Servicer Stake": return_servicer_stake,
    "Return Application Stake": return_application_stake,
    "Servicer Stake Burn": servicer_stake_burn,
    "Servicer Forced Unstake": servicer_forced_unstake,
    "Return Gateway Stake": return_gateway_stake,
    "Distribute Fees": distribute_fees,
}
