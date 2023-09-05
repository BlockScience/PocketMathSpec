from .Dummy import dummy_mechanism
from .Servicer import modify_servicer_pokt_holdings, modify_servicer_stake, update_servicer_params, prune_servicer_qos, servicer_unpause_mechanism

mechanism = {"Dummy Mechanism": dummy_mechanism,
             "Modify Servicer POKT Holdings": modify_servicer_pokt_holdings,
             "Modify Servicer Stake": modify_servicer_stake,
"Update Servicer Params": update_servicer_params,
"Prune Servicer QoS": prune_servicer_qos,
"Servicer Unpause Mechanism": servicer_unpause_mechanism}

