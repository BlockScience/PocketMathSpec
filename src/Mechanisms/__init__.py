from .Dummy import dummy_mechanism
from .Servicer import (modify_servicer_pokt_holdings, modify_servicer_stake, update_servicer_params,
                       prune_servicer_qos, servicer_unpause_mechanism, servicer_update_pause_height)
from .Application import modify_application_pokt_holdings, modify_application_stake, update_application_params
from .Validator import modify_validator_pokt_holdings, modify_validator_stake, update_validator_params

mechanism = {"Dummy Mechanism": dummy_mechanism,
             "Modify Servicer POKT Holdings": modify_servicer_pokt_holdings,
             "Modify Servicer Stake": modify_servicer_stake,
"Update Servicer Params": update_servicer_params,
"Prune Servicer QoS": prune_servicer_qos,
"Servicer Unpause Mechanism": servicer_unpause_mechanism,
"Modify Application POKT Holdings": modify_application_pokt_holdings,
"Modify Application Stake": modify_application_stake,
"Update Application Params": update_application_params,
"Servicer Update Pause Height": servicer_update_pause_height,
"Modify Validator POKT Holdings": modify_validator_pokt_holdings,
"Modify Validator Stake": modify_validator_stake,
"Update Validator Params": update_validator_params,}