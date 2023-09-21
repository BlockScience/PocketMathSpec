from typing import TypedDict
from ..Types import uPOKTType

mint_pokt_mechanism_space = TypedDict("Mint POKT Mechanism Space", {"mint_amount": uPOKTType})

mint_block_rewards_space = TypedDict("Mint Block Rewards Space", {})
burn_pokt_space = TypedDict("Burn POKT Space", {})
jail_node_space = TypedDict("Jail Node Space", {})