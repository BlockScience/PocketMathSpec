# PocketMathSpec

## Specification Overview

The mathematical specification handles the following attributes of the system:

### Broad Behaviors Modeled

The following are broad behaviors that will be need to be modeled:

1. Mint and Burn: The behaviors associated with minting for rewards as well as fees and burning done to balance minting
2. Servicer Stake: Behaviors around staking for servicers
3. Servicer Relay Rewards: Rewards for servicers doing work
4. Servicer Stake Burn: Slashing for servicers who do not perform
5. Servicer Jailing: Behavior for additonal incentive to perform
6. Validator Staking: Behaviors for validators staking into the network
7. Validator Block Reward: Rewards allocated on a block basis
8. Validator Stake Burn: Slashing from bad behavior
9. Validator Jailing: The process of jailing a validator for bad behavior
10. Validator Transaction Fees: Provide validators with an additional incentive for producing blocks
11. Portal Security Stake: Staking for the security of the service
12. Portal App Stake: "Reduce transaction costs for the system by requiring portal's to bond POKT to guarantee the bandwith they expect from Pocket's servicers, and optimise the balance between accessibility of the service for applications, as well as the economic potential of POKT. "
13. Portal fee per relay: The fees earned by portals for relaying
14. Application app stake: The behavior for applications staking
15. Application fee per relay: The fees that applications get for relaying
16. DAO Transaction Fee: A percentage of the fee for every transaction goes to the DAO, with the remaining proportion going to the producer of the block containing such transaction fees. 
17. DAO Allocation: The DAO treasury earns this proportion of the total POKT block reward. Value is a percentage. 

### Entity Modeling

The following are the entities that need to be created within the spec:

1. Servicers
2. Validators
3. DAO Group
4. Portals
5. Applications

### Parameters

#### Mint and Burn

1. Relays per day
2. Relays to Tokens Multiplier
3. Fees (Gateway Fee Per Relay and Application Fee Per Relay) following a piece-wise linear function to match the bootstrapping limits of the ecosystem 
4. MaturityRelayCharge 
5. MaturityRelayCost
6. MinBootstrapGatewayFeePerRelay 
7. MaxBootstrapServicerCostPerRelay 
8. ServicersBootstrapUnwindStart 
9. ServicersBootstrapEnd 
10. GatewaysBootstrapUnwindStart 
11. GatewaysBootstrapEnd 
12. Price of POKT in USD
13. Infura's price per relay
14. DAO Allocation 
15. Servicer Relay rewards
16. Validator block reward

#### Servicer Stake

1. servicer_minimum_stake

#### Servicer Relay Rewards

1. Servicer share of block rewards
2. DAO Allocation
3. Validator block rewards
4. Relays
5. Number of servicers
6. Relay QoS

#### Servicer Stake Burn

1. SlashFractionDowntime: The % of a node’s stake that is burned for downtime, where 1 is 100%.
2. ReplayAttackBurnMultiplier: The multiplier slash factor for submitting a replay attack. The base slash is directly proportional to the amount of relays claimed.

#### Servicer Jailing

1. DowntimeJailDuration: The amount of time (in nanoseconds) before a node can unjail and resume service.
2. MaxJailedBlocks: The amount of time (in blocks) a node has to unjail before being force unstaked and slashed. Reaching MaxJailedBlocks will result in a node’s entire stake being slashed.


#### Validator Staking

Modeling the Validator Threshold would need to be a product of:

1. MaxValidators - currently 1,000 (expanding set will lower threshold)
2. ProposerAllocation - currently 5% (increasing will incentivize more competition to be a validator, which will increase threshold)

#### Validator Block Reward

1. Initial parameter = 5% as per current v0 value, proportion of total block reward

#### Validator Stake Burn

1. double_sign_burn_percentage, default 5%
2. missed_blocks_burn_percentage, default 1%

#### Validator Jailing

1. DowntimeJailDuration: The amount of time (in nanoseconds) before a node can unjail and resume service.
2. MaxJailedBlocks: The amount of time (in blocks) a node has to unjail before being force unstaked and slashed. Reaching MaxJailedBlocks will result in a node’s entire stake being slashed.

#### Validator Transaction Fees

1. Transaction Fee = 0.01 POKT
2. Proposer percentage of fees = 10%
3. DAO percentage of fees = 90%

#### Portal Security Stake

1. Portal Minimum Stake, starting parameter = 150,000 POKT

#### Portal App Stake

1. Token to Relays Multiplier, starting parameter = 100

#### Portal fee per relay

1. Portal Fee Per Relay

#### Application App Stake

1. Token to Relays Multiplier, starting parameter = 100


#### Application Fee Per Relay

1. Application Fee per Relay

#### DAO Transaction Fee

1. Transaction Fee = 0.01 POKT
2. Proposer percentage of fees = 10%
3. DAO percentage of fees = 90%

#### DAO Allocation

1. Initial Percentage = 10% as per current v0 value