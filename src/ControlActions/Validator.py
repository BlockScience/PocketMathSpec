from ..Spaces import validator_stake_burning_space, validator_unstake_space, validator_jail_space, validator_block_reward_space

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

validator_jailed = {"name": "Validator Jailed",
    "description": """Validators are paused from service by the network if byzantine behaviors are detected. Some examples include:

- Not producing blocks when expected to
- Not signing blocks
- Signing against the majority
- Double signing blocks

Anytime an automatic removal of a Validator occurs, a burn proportional to the violation is applied against the Validator stake. The conditions, limitations, and severity of the Byzantine Validator burns are proposed and voted on by the DAO.

If a Validator is `paused`, they are able to reverse the paused state by submitting an `UnpauseMsg` after the `MinValidatorPauseTime` has elapsed. After a successful UnpauseMsg, the Validator is once again eligible to execute Validator operations.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [validator_jail_space],
    "parameters_used": [],}

validator_block_reward = {"name": "Validator Block Reward",
    "description": """The Block Producer for each height (i.e. a single Validator) will be rewarded `BlockProposerAllocation` % of the total `TransactionFees` and `RelayRewards` held in the new block.

A single Validator's stake relative to the cumulative total of all Validators' stake is directly proportional to the likelihood of them being selected as a block producer. The external Consensus Specification outlines how block producers are selected for each height in greater detail.

The net `BlockProducerReward` is derived from the `TotalBlockReward` by subtracting the `DAOBlockReward` amount. Once a proposal block is finalized into the blockchain, the `BlockProducerReward` is sent to the custodial account.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [validator_block_reward_space],
    "parameters_used": [],}