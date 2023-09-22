from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space, assign_servicer_salary_space,
                      validator_block_reward_space, modify_servicer_pokt_space, burn_pokt_mechanism_space,
                      dao_block_reward_space, modify_dao_pokt_space)

treasury_transmission_channels = []

treasury_transmission_channels.append({"origin": "Mint Block Rewards",
                                        "target": "Block Reward Policy Aggregate",
                                        "space": mint_block_rewards_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Block Reward Policy Aggregate",
                                        "target": "Mint POKT Mechanism",
                                        "space": mint_pokt_mechanism_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Block Reward Policy Aggregate",
                                        "target": "Assign Servicer Salary Policy",
                                        "space": assign_servicer_salary_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Block Reward Policy Aggregate",
                                        "target": "Validator Block Reward Policy",
                                        "space": validator_block_reward_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Block Reward Policy Aggregate",
                                        "target": "DAO Block Reward Policy",
                                        "space": dao_block_reward_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Assign Servicer Salary Policy",
                                        "target": "Modify Servicer POKT Holdings",
                                        "space": modify_servicer_pokt_space,
                                        "optional": False})

treasury_transmission_channels.append({"origin": "Assign Servicer Salary Policy",
                                        "target": "Burn POKT Mechanism",
                                        "space": burn_pokt_mechanism_space,
                                        "optional": False})


treasury_transmission_channels.append({"origin": "DAO Block Reward Policy",
                                        "target": "Modify DAO POKT Holdings",
                                        "space": modify_dao_pokt_space,
                                        "optional": False})
