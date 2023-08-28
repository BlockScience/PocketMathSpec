from ..Spaces import servicer_stake_space

servicer_stake = {
    "name": "Servicer Stake",
    "description": "In order to participate as a Servicer in Pocket Network, each actor is required to bond a certain amount of tokens in escrow while they are providing Web3 access. These tokens may be burnt or removed from the actor as a result of breaking the Protocol’s Service Level Agreement, a DAO defined set of requirements for the minimum quality of service.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Servicer"],
    "codomain": [servicer_stake_space],
    "parameters_used": [],
}
