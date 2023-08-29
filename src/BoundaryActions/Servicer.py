from ..Spaces import servicer_stake_space, servicer_pause_space, servicer_unpause_space

servicer_stake = {
    "name": "Servicer Stake",
    "description": "In order to participate as a Servicer in Pocket Network, each actor is required to bond a certain amount of tokens in escrow while they are providing Web3 access. These tokens may be burnt or removed from the actor as a result of breaking the Protocol’s Service Level Agreement, a DAO defined set of requirements for the minimum quality of service.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Servicer"],
    "codomain": [servicer_stake_space],
    "parameters_used": [],
}

servicer_pause = {
    "name": "Servicer Pause",
    "description": "Servicers are able to gracefully pause their service (e.g. for maintenance reasons) without the need to unstake or face downtime penalization. In addition to an Operator initiated `PauseMsg`, Fishermen are also able to temporarily pause a Servicer if a faulty or malicious process is detected during sampling.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Servicer", "Fisherman"],
    "codomain": [servicer_pause_space],
    "parameters_used": [],
}

servicer_unpause = {
    "name": "Servicer Unpause",
    "description": "When a Servicer is paused, they are able resume service by submitting an `UnpauseMsg` after the `MinPauseTime` has elapsed. After a `UnpauseMsg` is validated and the World State is updated, the Servicer is eligible to continue providing Web3 service to Applications, and receive rewards.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Servicer"],
    "codomain": [servicer_unpause_space],
    "parameters_used": [],
}