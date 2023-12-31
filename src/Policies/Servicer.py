from ..Spaces import (
    servicer_stake_space,
    modify_servicer_pokt_space,
    servicer_param_update_space,
    servicer_unpause_space,
    servicer_unpause_space2,
    servicer_pause_space,
    servicer_pause_space2,
    assign_servicer_salary_space,
    modify_servicer_pokt_space,
    burn_pokt_mechanism_space,
    servicer_relay_space,
    servicer_stake_burn_space,
    servicer_unstake_space,
    servicer_stake_status_space,
    return_servicer_stake_space,
    modify_gateway_pokt_space,
    modify_application_pokt_space,
    increase_relay_fees_space,
    jail_node_space,
    unjail_node_space,
    servicer_forced_unstake_space,
    remove_servicer_space,
)

servicer_stake_policy = {
    "name": "Servicer Stake Policy",
    "description": "Policy which takes care of actions to occur after a servicer attempts to stake",
    "constraints": [
        "DOMAIN[0].public_key must not be null",
        "DOMAIN[0].amount > 0",
        "LEN(DOMAIN[0].services) > 0",
        "All chains in DOMAIN[0].services must be valid",
        "LEN(DOMAIN[0].services) <= PARAMS.max_chains_servicer",
    ],
    "policy_options": [],
    "domain": [servicer_stake_space],
    "codomain": [
        servicer_stake_space,
        modify_servicer_pokt_space,
        modify_servicer_pokt_space,
    ],
    "parameters_used": ["minimum_stake_servicer", "max_chains_servicer"],
}

set_servicer_parameters_policy_option_v1 = {
    "name": "Set Servicer Parameters Policy V1",
    "description": "This policy determines if the parameters of a servicer should be updated and if so executes on it.",
    "logic": "As long as the servicer has a staking amount equal to or greater than the current staked amount, the servicer will have its parameters all updated. In addition, the Servicer's historical QoS (TestScores, ReportCard, etc...) will be pruned from the state.",
}


set_servicer_parameters_policy = {
    "name": "Set Servicer Parameters Policy",
    "description": "Policy for determining the impact of servicer parameter changes",
    "constraints": [],
    "policy_options": [set_servicer_parameters_policy_option_v1],
    "domain": [servicer_stake_space],
    "codomain": [servicer_param_update_space, servicer_param_update_space],
    "parameters_used": [],
}

servicer_unpause_policy = {
    "name": "Servicer Unpause Policy",
    "description": "The policy which determines if an unpause can take place",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_unpause_space],
    "codomain": [servicer_unpause_space2],
    "parameters_used": ["minimum_pause_time"],
}

servicer_pause_policy = {
    "name": "Servicer Pause Policy",
    "description": "The policy which determines if a servicer will be paused. One consideration is whether or not the servicer is already paused currently.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_pause_space],
    "codomain": [servicer_pause_space2],
    "parameters_used": [],
}

assign_servicer_salary_policy = {
    "name": "Assign Servicer Salary Policy",
    "description": """A `ServicerSalary` is assigned to each individual Servicer based on their specific `ReportCard`, and is distributed every `SalaryBlockFrequency`. Salaries are distributed from the `TotalAvailableReward` pool, whose inflation is governed by Application volume of each `(Service, GeoZone)` pair and scaled by the `UsageToRewardCoefficient` governance parameter.

A Servicer must accumulate `MinimumTestScoreThreshold` TestScores before it is eligible for salary distribution. A ReportCard can be viewed as a rolling average of the Servicer's performance, where TestScores are removed when either `TestScoreExpiration` is passed or the TestScore FIFO queue exceeds `MaxTestScores`.

Salary distribution is accomplished by aggregating the total volume estimated (see above) for a specific `(Service, GeoZone)` pair (i.e. `TotalVolumeUsage`), multiplied by `UsageToRewardCoefficient`, and evenly divided into buckets per Servicer that exceed the minimum threshold (i.e. the `MinimumReportCardThreshold`). Each Servicer's reward is scaled proportionally to both their stake and their ReportCard. Tokens that are not allocated to a servicer are burnt.

For example, a 100% ReportCard results in zero burning of the `maxServicerReward`, while a 80% ReportCard results in 20% burning of the maxServicerReward. The rate of decrease continues linearly until the `MinimumReportCardThreshold` is reached. Below the MinimumReportCardThreshold no reward is given to prevent cheap Sybil attacks and freeloading nodes. Unstaking causes the Servicer's ReportCard to be cleared and start from scratch.

The following is pseudo-code to illustrate this business logic:

```go
// Called for each (Service, geoZone) pair every SessionBlockFrequency
func DistributeRewards(Service, geoZone, height):
  totalVolumeUsage = WorldState.RetrieveTotalVolumeEstimate(Service, geoZone, height)
  totalAvailableReward = totalVolumeUsage * GovParams.UsageToRewardCoefficient(height)

  allServicers = WorldState.RetrieveEligibleServicers(Service, geoZone, height)
  eligibleServicers = filterServicers(allServicers, GovParams.MinimumTestScoreThreshold(height))

  maxServicerReward = totalAvailableReward / len(eligibleServicers)

  for servicer := eligibleServicers {
      stake = WorldState.GetServicerStake(servicer, height)
      score = WorldState.GetReportCard(servicer, height)

      burnPercent = getBurnPercent(stake, score, height)
      burnAmount = burnPercent * maxServicerReward

      awardTokens(servicers, maxServicerReward - burnAmount)
      burnTokens(Service, geoZone, burnAmount)
  }
```""",
    "constraints": [],
    "policy_options": [],
    "domain": [assign_servicer_salary_space],
    "codomain": [modify_servicer_pokt_space, burn_pokt_mechanism_space],
    "parameters_used": [
        "minimum_test_score_threshold",
        "minimum_report_card_threshold",
    ],
}


servicer_relay_policy = {
    "name": "Servicer Relay Policy",
    "description": "The policy which determines what happens with a servicer relay including the fees. The servicer will be awarded their POKT and then either a gateway or application will be charged this POKT (depending on the session). As well, it is possible that it is the end of the session in which case the session would be removed from the global state.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_relay_space],
    "codomain": [
        modify_servicer_pokt_space,
        modify_gateway_pokt_space,
        modify_application_pokt_space,
        increase_relay_fees_space,
        servicer_relay_space,
        servicer_relay_space,
    ],
    "parameters_used": [
        "servicer_bootstrap_unwind_start",
        "servicer_bootstrap_end",
        "maturity_relay_cost",
        "maturity_relay_charge",
    ],
}


servicer_stake_burn_policy = {
    "name": "Servicer Stake Burn Policy",
    "description": "The policy which determines how much burning a servicer might experience for bad behavior.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_stake_burn_space],
    "codomain": [],
    "parameters_used": ["slash_fraction_downtime", "replay_attack_burn_multiplier"],
}

servicer_unstake_policy = {
    "name": "Servicer Unstake Policy",
    "description": "The policy which determines any behaviors around servicers unstaking.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_unstake_space],
    "codomain": [servicer_stake_status_space],
    "parameters_used": [],
}

return_servicer_stake_policy = {
    "name": "Return Servicer Stake Policy",
    "description": "The policy which determines when a servicer can have their stake returned.",
    "constraints": [],
    "policy_options": [],
    "domain": [return_servicer_stake_space],
    "codomain": [
        servicer_stake_status_space,
        modify_servicer_pokt_space,
        modify_servicer_pokt_space,
    ],
    "parameters_used": ["servicer_unbounding_period"],
}


burn_per_relay_policy = {
    "name": "Burn Per Relay Policy",
    "description": "The policy for determining the amount to be burned per relay. At current time there will be 0 burn but this may change in the future to move towards deflation.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_relay_space],
    "codomain": [burn_pokt_mechanism_space, modify_application_pokt_space],
    "parameters_used": ["app_burn_per_relay"],
}

jail_node_policy = {
    "name": "Jail Node Policy",
    "description": "The policy for determining both whether the node in fact should be jailed (any validations to ensure) and as well determine if any amount of stake burning should take place.",
    "constraints": [],
    "policy_options": [],
    "domain": [jail_node_space],
    "codomain": [
        servicer_pause_space2,
        modify_servicer_pokt_space,
        burn_pokt_mechanism_space,
    ],
    "parameters_used": [],
}

unjail_node_policy = {
    "name": "Unjail Node Policy",
    "description": "The policy for determining whether a node can be unjailed.",
    "constraints": [],
    "policy_options": [],
    "domain": [unjail_node_space],
    "codomain": [servicer_pause_space2],
    "parameters_used": ["downtime_jail_duration"],
}

servicer_forced_unstake_policy = {
    "name": "Servicer Forced Unstake Policy",
    "description": "The policy for doing a force unstake on a servicer. The stake will be slashed and they will be booted from the system. It is possible they receive some of their stake back if it is a partial slashing, hence the modify Servicer POKT Holdings.",
    "constraints": [],
    "policy_options": [],
    "domain": [servicer_forced_unstake_space],
    "codomain": [
        modify_servicer_pokt_space,
        burn_pokt_mechanism_space,
        remove_servicer_space,
        modify_servicer_pokt_space,
    ],
    "parameters_used": [],
}
