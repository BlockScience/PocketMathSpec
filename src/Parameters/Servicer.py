from ..Types import POKTType, Days, NumberOfBlocksType, PercentType

servicer_parameter_set = {"name": "Servicer Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": POKTType,
                                       "name": "minimum_stake_servicer",
                                       "description": "The minimum required stake for servicers, default is 15K",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": Days,
                                       "name": "minimum_stake_period_servicer",
                                       "description": "The minimum required period of time that a servicer has to be staked for, default is 21 days.",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": Days,
                                       "name": "minimum_pause_time",
                                       "description": "The minimum required period of time that a servicer has to be paused for before being able to be unpaused.",
                                       "symbol": None,
                                       "domain": None},
                                       {"variable_type": int,
                                       "name": "max_chains_servicer",
                                       "description": "When staking as a servicer, every servicer must register their stake for the relay chains that they support. Currently, servicers can register each stake to apply to their work in up to 15 different blockchains, which is the maximum number that can be chosen. ",
                                       "symbol": None,
                                       "domain": None},
                                       {"variable_type": NumberOfBlocksType,
                                        "name": "salary_block_frequency",
                                        "description": "The frequency of salary blocks for servicers",
                                        "symbol": None,
                                       "domain": None},
                                        {"variable_type": int,
                                        "name": "minimum_test_score_threshold",
                                        "description": "The minimum test scores to be eligible for salary for servicers",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": float,
                                        "name": "minimum_report_card_threshold",
                                        "description": "The minimum report card score to earn salary. Below the MinimumReportCardThreshold no reward is given to prevent cheap Sybil attacks and freeloading nodes.",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": NumberOfBlocksType,
                                        "name": "servicer_unbounding_period",
                                        "description": "The number of blocks before a servicer has their stake returned to them after unstaking.",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": POKTType,
                                        "name": "servicer_stake_floor_multiplier",
                                        "description": """This parameter denotes the size (or width) of the bins. The value here denotes the amount of POKT can vary among nodes to still be considered in the same bin.

When this feature was first implemented, the value was equal to 15,000 POKT, meaning that a node could stake anywhere from (for example) 15,000 POKT to 29,999 POKT and still receive the same reward multiplier.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": POKTType,
                                        "name": "servicer_stake_weight_ceiling",
                                        "description": """When this feature was first implemented, the value was equal to 60,000 POKT, meaning that a node that staked 60,000 or more POKT would always receive the largest multiplier of rewards.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": float,
                                        "name": "servicer_stake_floor_multiplier_exponent",
                                        "description": """The next two parameters determine not the bins, but the multipliers that are applied to those bins to get the final reward multiplier.

This parameter determines how the rewards scale per each bin.

Assuming all else equal, with an exponent of 1 (the initial value when this feature was implemented) the bins would scale linearly.

An exponent value of greater than 1 will incentivize node consolidation, as node runners will earn more by staking their POKT on fewer nodes. Similarly, an exponent value of less than 1 will disincentivize consolidation, because of the reduction in rewards.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": float,
                                        "name": "servicer_stake_weight_multiplier",
                                        "description": """This final parameter exists to offset the inflation caused by Stake-Weighted Servicer Rewards.

With increased rewards for the same amount of POKT staked, the new system of consolidated nodes would encourage inflation. This is an unintended side-effect, so the ServicerStakeWeightMultiplier was added in to offset the inflation, so that the amount of POKT created would be the same regardless of whether Stake-Weighted Servicer Rewards had gone into effect or not.

For example, if the way nodes are positioned in bins leads to an emission rate of 1.8 times of what would have been before, then this parameter would be set to 1.8 which would offset the rewards generated by exactly this amount.

This is the parameter most likely to be changed frequently, since it affects inflation most directly.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": POKTType,
                                        "name": "relays_to_tokens_multiplier",
                                        "description": """The amount of POKT rewarded for each relay in block rewards.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": PercentType,
                                        "name": "slash_fraction_downtime",
                                        "description": """The % of a node’s stake that is burned for downtime, where 1 is 100%.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": PercentType,
                                        "name": "replay_attack_burn_multiplier",
                                        "description": """The multiplier slash factor for submitting a replay attack. The base slash is directly proportional to the amount of relays claimed.""",
                                        "symbol": None,
                                       "domain": None},
                                       {"variable_type": NumberOfBlocksType,
                                        "name": "max_jailed_blocks",
                                        "description": """The amount of time (in blocks) a node has to unjail before being force unstaked and slashed.""",
                                        "symbol": None,
                                       "domain": None}
                                       ]}

