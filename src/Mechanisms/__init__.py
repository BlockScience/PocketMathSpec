from .Dummy import dummy_mechanism
from .Servicer import modify_servicer_pokt_holdings, modify_servicer_stake

mechanism = {"Dummy Mechanism": dummy_mechanism,
             "Modify Servicer POKT Holdings": modify_servicer_pokt_holdings,
             "Modify Servicer Stake": modify_servicer_stake}

