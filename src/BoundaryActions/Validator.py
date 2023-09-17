from ..Spaces import (validator_stake_space, validator_pause_space, validator_unstake_space,
                      validator_unpause_space, become_validator_space)

validator_stake = {
    "name": "Validator Stake",
    "description": "Validators registration is permissionless. In order to participate in the network as a Validator, each actor is required to bond a certain amount of tokens in escrow while they are validating state transitions. These tokens are used as collateral to disincentive byzantine behavior.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [validator_stake_space],
    "parameters_used": [],
}

validator_pause = {
    "name": "Validator Pause",
    "description": "The action for a validator pausing their service.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [validator_pause_space],
    "parameters_used": [],
}

validator_unstake = {
    "name": "Validator Unstake",
    "description": "A Validator is able to submit an UnstakeMsg to exit the network and remove itself from Validator Operations. After a successful UnstakeMsg, the Validator is no longer eligible to participate in the Consensus protocol. After ValidatorUnstakingTime elapses, any stake amount left is returned to the custodial account.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [validator_unstake_space],
    "parameters_used": [],
}

validator_unpause = {
    "name": "Validator Unpause",
    "description": "If a Validator is paused, they are able to reverse the paused state by submitting an UnpauseMsg after the MinValidatorPauseTime has elapsed. After a successful UnpauseMsg, the Validator is once again eligible to execute Validator operations.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [validator_unpause_space],
    "parameters_used": [],
}

become_validator = {"name": "Become Validator",
    "description": "To become a Validator Node, you must be in the top 1,000 node stakes on the network (as determined by the MaxValidators parameter). Validator Nodes can claim a block reward percentage for submitting the block equal to the value of the ProposerPercentage parameter.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [become_validator_space],
    "parameters_used": ["max_validators"],}