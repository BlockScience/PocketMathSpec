from ..Spaces import validator_stake_burning_space, validator_unstake_space

validator_stake_burning = {
    "name": "Validator Stake Burning",
    "description": """Control action for when validators have their stake burned""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [validator_stake_burning_space],
    "parameters_used": [],
}


validator_unstake_forced = {
    "name": "Validator Unstake Forced",
    "description": "If a Validator stake amount ever falls below the MinimumValidatorStake, the protocol automatically executes an UnstakeMsg on behalf of the node, subjecting the Validator to the unstaking process. After a successful UnstakeMsg, the Validator is no longer eligible to participate in the Consensus protocol. After ValidatorUnstakingTime elapses, any stake amount left is returned to the custodial account.",
    "constraints": [],
    "control_action_options": [],
    "codomain": [validator_unstake_space],
    "parameters_used": ["minimum_validator_stake"],
}