from tx_creation import BCS_net
from pycoin.solve.utils import build_hash160_lookup, build_p2sh_lookup, build_sec_lookup
from pycoin.ecdsa.secp256k1 import secp256k1_generator
from bitcoinrpc.authproxy import AuthServiceProxy
import sys
from conf import NET_PARAMS 
# method = 'getnewaddress'
# method_send = 'sendrawtransaction'
addr_to_spend = 'BM3WwFWYvz7TdvvEp9EGUB6mSg2jiM5fW6'

Bcs_network = BCS_net(addr_to_spend, rpc_user = 'bcs_tester', rpc_pass='iLoveBCS', NET_PARAMS=NET_PARAMS)
Bcs_network.create_tx(satoshis = 1000000, solver_f = build_hash160_lookup, generator = secp256k1_generator)
print(Bcs_network.signed_new_tx)
print(Bcs_network.signed_new_tx_hex)
conn = AuthServiceProxy('http://bcs_tester:iLoveBCS@140.82.36.227:3669/')
print(conn.decoderawtransaction(Bcs_network.signed_new_tx_hex))

# !!!bitcoinrpc.authproxy.JSONRPCException: -25: Missing inputs
print(conn.sendrawtransaction(Bcs_network.signed_new_tx_hex))

url = 'https://bcschain.info/api/tx/send'