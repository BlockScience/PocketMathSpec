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

### Entity Modeling

The following are the entities that need to be created within the spec:

1. Servicers
2. Validators
3. DAO Group

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


