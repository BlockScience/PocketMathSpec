from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space)

block_reward_policy_aggregate = {"name": "Block Reward Policy Aggregate",
                        "description": "The aggregate policy for creating the total amount of block reward and also splitting it between different groups.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [mint_block_rewards_space],
                        "codomain": [mint_pokt_mechanism_space],
                        "parameters_used": []}