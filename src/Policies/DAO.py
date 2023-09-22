from ..Spaces import (dao_block_reward_space)

dao_block_reward_policy = {"name": "DAO Block Reward Policy",
                        "description": "Policy which takes care of allocations to the DAO from block rewards",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [dao_block_reward_space],
                        "codomain": [],
                        "parameters_used": []}