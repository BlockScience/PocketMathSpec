# PocketMathSpec

## Specification Overview

The mathematical specification handles the following attributes of the system:

### Broad Behaviors Modeled

The following are broad behaviors that will be need to be modeled:

1. Mint and Burn: The behaviors associated with minting for rewards as well as fees and burning done to balance minting
2. 

### Entity Modeling

The following are the entities that need to be created within the spec:

1. Servicers
2. Validators
3. DAO Group

### Parameters

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