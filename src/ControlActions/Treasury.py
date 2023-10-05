from ..Spaces import mint_block_rewards_space, jail_node_space, distribute_fees_space

mint_block_rewards = {
    "name": "Mint Block Rewards",
    "description": """The action of the protocol minting block rewards""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [mint_block_rewards_space],
    "parameters_used": [],
}

distribute_fees = {
    "name": "Distribute Fees",
    "description": """The action for distributing fees earned from relays and sessions.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [distribute_fees_space],
    "parameters_used": [],
}

jail_node = {
    "name": "Jail Node",
    "description": """The action which results in a node (servicer or validator) being jailed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [jail_node_space],
    "parameters_used": [],
}