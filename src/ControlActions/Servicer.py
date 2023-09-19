from ..Spaces import assign_servicer_salary_space

assign_servicer_salary = {
    "name": "Assign Servicer Salary",
    "description": """A ServicerSalary is assigned to each individual Servicer based on their specific ReportCard, and is distributed every SalaryBlockFrequency. Salaries are distributed from the TotalAvailableReward pool, whose inflation is governed by Application volume of each (RelayChain, GeoZone) pair and scaled by the UsageToRewardCoefficient governance parameter.

A Servicer must accumulate MinimumTestScoreThreshold TestScores before it is eligible for salary distribution. A ReportCard can be viewed as a rolling average of the Servicer's performance, where TestScores are removed when either TestScoreExpiration is passed or the TestScore FIFO queue exceeds MaxTestScores.

Salary distribution is accomplished by aggregating the total volume estimated (see above) for a specific (RelayChain, GeoZone) pair (i.e. TotalVolumeUsage), multiplied by UsageToRewardCoefficient, and evenly divided into buckets per Servicer that exceed the minimum threshold (i.e. the MinimumReportCardThreshold). Each Servicer's reward is scaled proportionally to both their stake and their ReportCard. Tokens that are not allocated to a servicer are burnt.

For example, a 100% ReportCard results in zero burning of the maxServicerReward, while a 80% ReportCard results in 20% burning of the maxServicerReward. The rate of decrease continues linearly until the MinimumReportCardThreshold is reached. Below the MinimumReportCardThreshold no reward is given to prevent cheap Sybil attacks and freeloading nodes. Unstaking causes the Servicer's ReportCard to be cleared and start from scratch.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [assign_servicer_salary_space],
    "parameters_used": ["salary_block_frequency"],
}


