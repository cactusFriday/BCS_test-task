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
# print(Bcs_network.send_rpc(method='sendrawtransaction', params=Bcs_network.signed_new_tx_hex))
conn = AuthServiceProxy('http://bcs_tester:iLoveBCS@140.82.36.227:3669/')
# print(conn.decoderawtransaction(Bcs_network.signed_new_tx_hex))
print(conn.sendrawtransaction(Bcs_network.signed_new_tx_hex))

# секретный ключ кошелька
secret_key = 'KzjBKPxkBkf3WBpaXFczP57x2cZpgLnebwRbR1xYmEaaq4FRvH1c'

# trx = network.Tx
# src_tx_hex = "278b82624e255539c67011b46cadd57fe92bfd079d002fd428ad1f18a8a00bbd"
# src_tx_hex = '0200000001ae2e375fe76f30e3451e2f5fd7441c66ce884a189886abe1e6eccbeff6b6cda8000000006a473044022010ce551c1f7e1f8fa4a4a9d4d67c1acf9581ede52e0b1030c6974b798721c0ff02203191b63e3a19de477f30034c749056afce104d8d0e5365e95edc1aaa34392b360121037ca1f015fbaf30ca61d9a9e555c5fb35cb8ee63c6a5c4b28f6f1194ce289e408feffffff02f8ff43b3650000001976a91418022dedf153d20b8bf10adae95c12eb6deb8de488ac4eb62c060000000017a91418c1047730048de078cf35649aa6ef2b6827a07187c9a41400'
# print(len(src_tx_hex))
# src_tx = trx.
# src_tx = Tx1.from_hex(src_tx_hex)
# src_tx = Tx.from_hex(src_tx_hex)
# print('[TX_HEX]:', src_tx)
# spendable = src_tx.tx_outs_as_spendable()[0]


# solver = build_hash160_lookup([exponent], [secp256k1_generator])
# signed_new_tx = unsigned_tx.sign(solver)

# print(signed_new_tx.bad_signature_count())

# raw_data = 'rawtx={'+str(signed_new_tx_hex)+'}'
# raw_rpc_data = '{"'+str(signed_new_tx_hex)+'"}'
# rawtx='rawtx={02000000014727d9d3560b94b0cf1c10daea43920c24fa8451a75f2d5f69f6f585726fcb15000000006a47304402202ac3b7fd62837722fd4ab1dfdfe7d069dcaad348c7a039ed3cfc473ef435a167022033ae815fbcd8c04b2fb98d611a395dd96da757cae94bca780010bd9db6bda7230121027f2fac6638798fe79696bffba971976b325753541d24fc0a920b617b5f23815bfeffffff02c00064f6070000001976a9140588712645b0c536d59c9d7198f492cf6d2eb3cf88ac263f61e9030000001976a91421b92d11d3b7cbe5e76252eab7db8bd5ac47a0ae88ac781a0600}'

# print(raw_data)
url = 'https://bcschain.info/api/tx/send'
# response = requests.post(url, data = str(rawtx))
# {"jsonrpc":"1.0","id":"curltext","method":"getblockchaininfo","params":[]}

# TODO: {"result":null,"error":{"code":-22,"message":"TX decode failed"},"id":"curltext"}
# TODO: DECODE FAILED)))


# print(conn.sendrawtransaction(signed_new_tx_hex))
# response = requests.post('http://bcs_tester:iLoveBCS@140.82.36.227:3669/', json={"jsonrpc":"1.0", "id":"curltext", 'method': method_send, "params":[signed_new_tx_hex]})
# print()
# print(response.text)