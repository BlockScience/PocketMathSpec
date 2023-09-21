from ..Spaces import (servicer_stake_space, modify_servicer_pokt_space, servicer_param_update_space,
                      servicer_unpause_space, servicer_unpause_space2, servicer_pause_space, servicer_pause_space2,
                      assign_servicer_salary_space, servicer_salary_space, servicer_block_reward_space)

servicer_stake_policy = {"name": "Servicer Stake Policy",
                        "description": "Policy which takes care of actions to occur after a servicer attempts to stake",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",
                                        "LEN(DOMAIN[0].relay_chains) > 0",
                                        "All chains in DOMAIN[0].relay_chains must be valid",
                                        "LEN(DOMAIN[0].relay_chains) <= PARAMS.max_chains_servicer"],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [servicer_stake_space, modify_servicer_pokt_space, modify_servicer_pokt_space],
                        "parameters_used": ["minimum_stake_servicer", "max_chains_servicer"]}

set_servicer_parameters_policy = {"name": "Set Servicer Parameters Policy",
                        "description": "Policy for determining the impact of servicer parameter changes",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [servicer_param_update_space, servicer_param_update_space],
                        "parameters_used": []}

servicer_unpause_policy = {"name": "Servicer Unpause Policy",
                        "description": "The policy which determines if an unpause can take place",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_unpause_space],
                        "codomain": [servicer_unpause_space2],
                        "parameters_used": ["minimum_pause_time"]}

servicer_pause_policy = {"name": "Servicer Pause Policy",
                        "description": "The policy which determines if a servicer will be paused. One consideration is whether or not the servicer is already paused currently.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_pause_space],
                        "codomain": [servicer_pause_space2],
                        "parameters_used": []}

assign_servicer_salary_policy = {"name": "Assign Servicer Salary Policy",
                        "description": """A `ServicerSalary` is assigned to each individual Servicer based on their specific `ReportCard`, and is distributed every `SalaryBlockFrequency`. Salaries are distributed from the `TotalAvailableReward` pool, whose inflation is governed by Application volume of each `(RelayChain, GeoZone)` pair and scaled by the `UsageToRewardCoefficient` governance parameter.

A Servicer must accumulate `MinimumTestScoreThreshold` TestScores before it is eligible for salary distribution. A ReportCard can be viewed as a rolling average of the Servicer's performance, where TestScores are removed when either `TestScoreExpiration` is passed or the TestScore FIFO queue exceeds `MaxTestScores`.

Salary distribution is accomplished by aggregating the total volume estimated (see above) for a specific `(RelayChain, GeoZone)` pair (i.e. `TotalVolumeUsage`), multiplied by `UsageToRewardCoefficient`, and evenly divided into buckets per Servicer that exceed the minimum threshold (i.e. the `MinimumReportCardThreshold`). Each Servicer's reward is scaled proportionally to both their stake and their ReportCard. Tokens that are not allocated to a servicer are burnt.

For example, a 100% ReportCard results in zero burning of the `maxServicerReward`, while a 80% ReportCard results in 20% burning of the maxServicerReward. The rate of decrease continues linearly until the `MinimumReportCardThreshold` is reached. Below the MinimumReportCardThreshold no reward is given to prevent cheap Sybil attacks and freeloading nodes. Unstaking causes the Servicer's ReportCard to be cleared and start from scratch.

The following is pseudo-code to illustrate this business logic:

```go
// Called for each (relayChain, geoZone) pair every SessionBlockFrequency
func DistributeRewards(relayChain, geoZone, height):
  totalVolumeUsage = WorldState.RetrieveTotalVolumeEstimate(relayChain, geoZone, height)
  totalAvailableReward = totalVolumeUsage * GovParams.UsageToRewardCoefficient(height)

  allServicers = WorldState.RetrieveEligibleServicers(relayChain, geoZone, height)
  eligibleServicers = filterServicers(allServicers, GovParams.MinimumTestScoreThreshold(height))

  maxServicerReward = totalAvailableReward / len(eligibleServicers)

  for servicer := eligibleServicers {
      stake = WorldState.GetServicerStake(servicer, height)
      score = WorldState.GetReportCard(servicer, height)

      burnPercent = getBurnPercent(stake, score, height)
      burnAmount = burnPercent * maxServicerReward

      awardTokens(servicers, maxServicerReward - burnAmount)
      burnTokens(relayChain, geoZone, burnAmount)
  }
```""",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [assign_servicer_salary_space],
                        "codomain": [servicer_salary_space],
                        "parameters_used": ["usage_to_reward_coeffecient", "minimum_test_score_threshold", "minimum_report_card_threshold"]}


servicer_block_reward_policy = {"name": "Servicer Block Reward Policy",
                        "description": "Policy which determines block rewards for servicers",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_block_reward_space],
                        "codomain": [],
                        "parameters_used": []}