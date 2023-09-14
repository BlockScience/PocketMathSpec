from ..Spaces import validator_stake_space

validator_stake = {
    "name": "Validator Stake",
    "description": "Validators registration is permissionless. In order to participate in the network as a Validator, each actor is required to bond a certain amount of tokens in escrow while they are validating state transitions. These tokens are used as collateral to disincentive byzantine behavior.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Validator"],
    "codomain": [validator_stake_space],
    "parameters_used": [],
}