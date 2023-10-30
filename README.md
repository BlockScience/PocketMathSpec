# PocketMathSpec

## Specification Overview

The mathematical specification presented here follows the specification from the [Mathematical Specification Mapping Library](https://github.com/BlockScience/MSML). The framework allows for dynamic viewing of different aspects of the system such as:

- What parameters have an impact on different policies, mechanisms, etc.
- All the chains of actions that can modify different entities and their state variables
- Reports specifically generated for action chains which detail all the different components

## Current Version

- The current version is still a work in progress but the action chains present in reports/actions are in a rough draft form and undergoing review.
- The testing notebook allows for creation of the reports, viewing of the entire tree of the spec and parameter impact functions to zero in on what parameters are impacting the system
- Github issues are being used to track the work in progress
- Explanations of the terminologies used can be found in the [MSML documentation folder](https://github.com/BlockScience/MSML/tree/main/docs) 

## Reports

There are three types of reports currently shown in the repository which are automatically generated:

1. The Basic Report: All pieces of the system and action chains present are presented here (please note some are still WIP)
2. Actions: Specific reporting for each action chain which is in a rough draft form
3. Entity: All relevant action chains either called by a given entity and/or impacting a given entity (please note some are still WIP)

## Specification Tree

The tree below is all the components of the current specification.

```
├──Entities
│   ├──Servicer
│   ├──Watcher
│   ├──Application
│   ├──Validator
│   ├──Portal
│   ├──Treasury
│   ├──Service
│   ├──Global
│   ├──DAO
├──State
│   ├──Global
│   │   ├──Services
│   │   ├──Sessions
│   │   ├──Portals
│   │   ├──Servicers
│   ├──Servicer
│   │   ├──Public key
│   │   ├──Servicer Salary
│   │   ├──Report Card
│   │   ├──Test Scores
│   │   ├──POKT Holdings
│   │   ├──Staked POKT
│   │   ├──Service URL
│   │   ├──Services
│   │   ├──GeoZone
│   │   ├──Operator Public Key
│   │   ├──Pause Height
│   │   ├──Stake Status
│   │   ├──Unstaking Height
│   ├──Watcher
│   │   ├──Stake Status
│   ├──Application
│   │   ├──Public key
│   │   ├──POKT Holdings
│   │   ├──Staked POKT
│   │   ├──Services
│   │   ├──GeoZone
│   │   ├──Number of Servicers
│   │   ├──Stake Status
│   │   ├──Unstaking Height
│   │   ├──Delegate
│   ├──Validator
│   │   ├──Public key
│   │   ├──POKT Holdings
│   │   ├──Staked POKT
│   │   ├──Service URL
│   │   ├──Operator Public Key
│   │   ├──Stake Status
│   ├──Portal
│   │   ├──Stake Status
│   │   ├──Delegators
│   │   ├──POKT Holdings
│   │   ├──Staked POKT
│   ├──Treasury
│   │   ├──Floating Supply
│   │   ├──Relay Fees
│   ├──Service
│   │   ├──Name
│   │   ├──Portal API Prefix
│   │   ├──Service ID
│   ├──DAO
│   │   ├──POKT Holdings
├──Spaces
│   ├──Servicer Stake Space
│   ├──Servicer Pause Space
│   ├──Servicer Pause Space 2
│   ├──Servicer Unpause Space
│   ├──Assign Servicer Salary Space
│   ├──Modify Servicer POKT Space
│   ├──Servicer Param Update Space
│   ├──Servicer Unstake Space
│   ├──Application Stake Space
│   ├──Servicer Unpause Space 2
│   ├──Modify Application POKT Space
│   ├──Application Param Update Space
│   ├──Application Unstake Space
│   ├──Application Delegate to Portal Space
│   ├──Validator Stake Space
│   ├──Modify Validator POKT Space
│   ├──Validator Param Update Space
│   ├──Portal Registration Space
│   ├──Portal Unregistration Space
│   ├──Application Undelegation Space
│   ├──Validator Pause Space
│   ├──Validator Stake Burning Space
│   ├──Validator Block Reward Space
│   ├──Submit Relay Request Space
│   ├──Servicer Relay Space
│   ├──Mint Block Rewards Space
│   ├──Burn POKT Space
│   ├──Jail Node Space
│   ├──Unjail Node Space
│   ├──Return Servicer Stake Space
│   ├──Service Join Space
│   ├──Service Leave Space
│   ├──Return Application Stake Space
│   ├──Servicer Block Reward Space
│   ├──Mint POKT Mechanism Space
│   ├──Burn POKT Mechanism Space
│   ├──DAO Block Reward Space
│   ├──Modify DAO POKT Space
│   ├──Portal Relay Request Space
│   ├──Servicer Stake Burn Space
│   ├──Servicer Forced Unstake Space
│   ├──Servicer Stake Status Space
│   ├──Application Stake Status Space
│   ├──Modify Portal POKT Space
│   ├──Portal Stake Status Space
│   ├──Return Portal Stake Space
│   ├──Increase Relay Fees Space
│   ├──Distribute Fees Space
│   ├──Decrease Relay Fees Space
│   ├──Remove Servicer Space
├──Parameters
│   ├──Servicer
│   │   ├──minimum_stake_servicer
│   │   ├──minimum_stake_period_servicer
│   │   ├──minimum_pause_time
│   │   ├──max_chains_servicer
│   │   ├──salary_block_frequency
│   │   ├──minimum_test_score_threshold
│   │   ├──minimum_report_card_threshold
│   │   ├──servicer_unbounding_period
│   │   ├──relays_to_tokens_multiplier
│   │   ├──slash_fraction_downtime
│   │   ├──replay_attack_burn_multiplier
│   │   ├──max_jailed_blocks
│   │   ├──downtime_jail_duration
│   ├──Application
│   │   ├──minimum_servicers_per_session
│   │   ├──maximum_servicers_per_session
│   │   ├──application_unstaking_time
│   │   ├──application_fee_per_relay
│   │   ├──minimum_application_stake
│   │   ├──app_burn_per_session
│   │   ├──app_burn_per_relay
│   ├──Validator
│   │   ├──block_proposer_allocation
│   ├──Portal
│   │   ├──stake_per_app_delegation
│   │   ├──portal_fee_per_relay
│   │   ├──portal_minimum_stake
│   │   ├──portal_unstaking_time
│   ├──Session
│   │   ├──session_block_frequency
│   │   ├──session_token_bucket_coefficient
│   ├──Treasury
│   │   ├──dao_fee_percentage
│   │   ├──validator_fee_percentage
│   │   ├──maturity_relay_cost
│   │   ├──maturity_relay_charge
│   │   ├──min_bootstrap_gateway_fee_per_relay
│   │   ├──max_bootstrap_servicer_cost_per_relay
│   │   ├──servicer_bootstrap_unwind_start
│   │   ├──servicer_bootstrap_end
│   │   ├──gateway_bootstrap_unwind_start
│   │   ├──gateway_bootstrap_unwind_end
│   │   ├──transaction_fee
│   ├──Service
│   │   ├──supported_services
├──Boundary Actions
│   ├──Servicer Stake
│   ├──Servicer Pause
│   ├──Servicer Unpause
│   ├──Servicer Unstake
│   ├──Application Stake
│   ├──Application Unstake
│   ├──Application Delegate to Portal
│   ├──Portal Registration
│   ├──Portal Unregistration
│   ├──Application Undelegation
│   ├──Submit Relay Request
│   ├──Servicer Relay
│   ├──Burn POKT
│   ├──Unjail Node
│   ├──Service Join
│   ├──Service Leave
│   ├──Submit Relay Request (Portal)
├──Control Actions
│   ├──Mint Block Rewards
│   ├──Jail Node
│   ├──Return Servicer Stake
│   ├──Return Application Stake
│   ├──Servicer Stake Burn
│   ├──Servicer Forced Unstake
│   ├──Return Portal Stake
│   ├──Distribute Fees
├──Policies
│   ├──Servicer Stake Policy
│   ├──Set Servicer Parameters Policy
│   ├──Servicer Unpause Policy
│   ├──Application Stake Policy
│   ├──Set Application Parameters Policy
│   ├──Servicer Pause Policy
│   ├──Assign Servicer Salary Policy
│   ├──Application Delegate to Portal Policy
│   ├──Block Reward Policy Aggregate
│   ├──Validator Block Reward Policy
│   ├──DAO Block Reward Policy
│   ├──Submit Relay Request (Portal) Policy
│   ├──Servicer Relay Policy
│   ├──Servicer Stake Burn Policy
│   ├──Portal Registration Policy
│   ├──Servicer Unstake Policy
│   ├──Application Unstake Policy
│   ├──Submit Relay Request Policy
│   ├──Service Join Policy
│   ├──Service Leave Policy
│   ├──Application Undelegate to Portal Policy
│   ├──Portal Unregistration Policy
│   ├──Return Servicer Stake Policy
│   ├──Return Application Stake Policy
│   ├──Return Portal Stake Policy
│   ├──Burn POKT Policy
│   ├──Burn Per Session Policy
│   ├──Burn Per Relay Policy
│   ├──Distribute Fees Policy
│   ├──Jail Node Policy
│   ├──Unjail Node Policy
│   ├──Servicer Forced Unstake Policy
├──Mechanisms
│   ├──Modify Servicer POKT Holdings
│   ├──Modify Servicer Stake
│   ├──Update Servicer Params
│   ├──Prune Servicer QoS
│   ├──Servicer Unpause Mechanism
│   ├──Modify Application POKT Holdings
│   ├──Modify Application Stake
│   ├──Update Application Params
│   ├──Servicer Update Pause Height
│   ├──Modify Validator POKT Holdings
│   ├──Mint POKT Mechanism
│   ├──Burn POKT Mechanism
│   ├──Modify DAO POKT Holdings
│   ├──Update Servicer Stake Status
│   ├──Update Application Stake Status
│   ├──Add New Service
│   ├──Remove Service
│   ├──Add Portal Delegator
│   ├──Update Application Delegate
│   ├──Remove Portal Delegator
│   ├──Modify Portal POKT Holdings
│   ├──Modify Portal Stake
│   ├──Add New Portal
│   ├──Update Portal Stake Status
│   ├──Create New Session
│   ├──Increase Relay Fees
│   ├──Remove Session
│   ├──Decrease Relay Fees
│   ├──Remove Servicer
```