from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space)

treasury_transmission_channels = []

treasury_transmission_channels.append({"origin": "Mint Block Rewards",
                                        "target": "Block Reward Policy Aggregate",
                                        "space": mint_block_rewards_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Block Reward Policy Aggregate",
                                        "target": "Mint POKT Mechanism",
                                        "space": mint_pokt_mechanism_space,
                                        "optional": False})
