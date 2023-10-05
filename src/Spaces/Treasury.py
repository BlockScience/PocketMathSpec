from typing import TypedDict
from ..Types import uPOKTType, BlockHeightType, PublicKeyType

mint_pokt_mechanism_space = TypedDict("Mint POKT Mechanism Space", {"mint_amount": uPOKTType})
burn_pokt_mechanism_space = TypedDict("Burn POKT Mechanism Space", {"burn_amount": uPOKTType})

mint_block_rewards_space = TypedDict("Mint Block Rewards Space", {"current_height": BlockHeightType, # Height of the block
                                                                  "block_producer": PublicKeyType, # The address of the validator which created the block
                                                                  })
burn_pokt_space = TypedDict("Burn POKT Space", {"burn_amount": uPOKTType,
                                                "block_height": BlockHeightType})
jail_node_space = TypedDict("Jail Node Space", {"node_address": PublicKeyType,
                                                "block_height": BlockHeightType,
                                                "jailer_address": PublicKeyType})

increase_relay_fees_space =  TypedDict("Increase Relay Fees Space", {"POKT Amount": uPOKTType,})