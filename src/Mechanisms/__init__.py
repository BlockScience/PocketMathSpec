from .Servicer import (modify_servicer_pokt_holdings, modify_servicer_stake, update_servicer_params,
                       prune_servicer_qos, servicer_unpause_mechanism, servicer_update_pause_height,
                       update_servicer_stake_status, remove_session)
from .Application import (modify_application_pokt_holdings, modify_application_stake,
                          update_application_params, update_application_stake_status,
                          update_application_delegate, create_new_session)
#from .Validator import modify_validator_pokt_holdings, modify_validator_stake, update_validator_params
from .Validator import modify_validator_pokt_holdings
from .Treasury import mint_pokt_mechanism, burn_pokt_mechanism, increase_relay_fees, decrease_relay_fees
from .DAO import (modify_dao_pokt_holdings)
from .Service import (add_new_service, remove_service)
from .Portal import (add_portal_delegator, remove_portal_delegator, modify_portal_pokt_holdings, modify_portal_stake,
                     add_new_portal, update_portal_stake_status)

mechanism = {"Modify Servicer POKT Holdings": modify_servicer_pokt_holdings,
             "Modify Servicer Stake": modify_servicer_stake,
"Update Servicer Params": update_servicer_params,
"Prune Servicer QoS": prune_servicer_qos,
"Servicer Unpause Mechanism": servicer_unpause_mechanism,
"Modify Application POKT Holdings": modify_application_pokt_holdings,
"Modify Application Stake": modify_application_stake,
"Update Application Params": update_application_params,
"Servicer Update Pause Height": servicer_update_pause_height,
"Modify Validator POKT Holdings": modify_validator_pokt_holdings,
#"Modify Validator Stake": modify_validator_stake,
#"Update Validator Params": update_validator_params,
"Mint POKT Mechanism": mint_pokt_mechanism,
"Burn POKT Mechanism": burn_pokt_mechanism,
"Modify DAO POKT Holdings": modify_dao_pokt_holdings,
"Update Servicer Stake Status": update_servicer_stake_status,
"Update Application Stake Status": update_application_stake_status,
"Add New Service": add_new_service,
 "Remove Service": remove_service,
 "Add Portal Delegator": add_portal_delegator,
"Update Application Delegate": update_application_delegate,
"Remove Portal Delegator": remove_portal_delegator,
"Modify Portal POKT Holdings": modify_portal_pokt_holdings,
"Modify Portal Stake": modify_portal_stake,
"Add New Portal": add_new_portal,
"Update Portal Stake Status": update_portal_stake_status,
"Create New Session": create_new_session,
"Increase Relay Fees": increase_relay_fees,
"Remove Session": remove_session,
"Decrease Relay Fees": decrease_relay_fees}