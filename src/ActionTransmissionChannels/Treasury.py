from ..Spaces import (mint_block_rewards_space)

treasury_transmission_channels = []

treasury_transmission_channels.append({"origin": "Mint Block Rewards",
                                        "target": "Block Reward Policy Aggregate",
                                        "space": mint_block_rewards_space,
                                        "optional": False})

