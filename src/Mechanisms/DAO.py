from ..Spaces import modify_dao_pokt_space

modify_dao_pokt_holdings = {"name": "Modify DAO POKT Holdings",
                           "description": "The mechanism to update the holdings of the DAO",
                           "constraints": [],
                           "logic": "The DAO has its holdings increased by the value",
                           "domain": [modify_dao_pokt_space],
                           "parameters_used": []}