from typing import TypedDict
from ..Types import uPOKTType, BlockHeightType, PublicKeyType

mint_pokt_mechanism_space = TypedDict("Mint POKT Mechanism Space", {"mint_amount": uPOKTType})

mint_block_rewards_space = TypedDict("Mint Block Rewards Space", {"current_height": BlockHeightType, # Height of the block
                                                                  "block_producer": PublicKeyType, # The address of the validator which created the block
                                                                  })
burn_pokt_space = TypedDict("Burn POKT Space", {})
jail_node_space = TypedDict("Jail Node Space", {})