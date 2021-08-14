# from pycoin.ecdsa import generator_secp256k1, public_pair_for_secret_exponent
# from pycoin.encoding import wif_to_secret_exponent, public_pair_to_sec
from pycoin.coins.bitcoin.Tx import Spendable
from pycoin.coins.tx_utils import create_tx
from pycoin.networks.bitcoinish import create_bitcoinish_network
from pycoin.coins.tx_utils import create_tx
from pycoin.encoding.hexbytes import h2b
import json
import requests

class BCS_net():
    def __init__(self, addr_sender: str, rpc_user: str, rpc_pass: str, NET_PARAMS: dict):
        self.secret_key = 'KzjBKPxkBkf3WBpaXFczP57x2cZpgLnebwRbR1xYmEaaq4FRvH1c'
        self.address_sender = addr_sender
        self.rpc_user = rpc_user
        self.rpc_pass = rpc_pass
        self.network = create_bitcoinish_network(symbol = NET_PARAMS['symbol'], network_name = NET_PARAMS['network_name'], 
            subnet_name = NET_PARAMS['subnet_name'], wif_prefix_hex=NET_PARAMS['wif_prefix_hex'], 
            address_prefix_hex=NET_PARAMS['address_prefix_hex'], pay_to_script_prefix_hex=NET_PARAMS['pay_to_script_prefix_hex'],
            bip32_prv_prefix_hex=NET_PARAMS['bip32_prv_prefix_hex'], bip32_pub_prefix_hex=NET_PARAMS['bip32_pub_prefix_hex'],
            bech32_hrp=NET_PARAMS['bech32_hrp'], bip49_prv_prefix_hex=NET_PARAMS['bip49_prv_prefix_hex'],
            bip49_pub_prefix_hex=NET_PARAMS['bip49_pub_prefix_hex'], bip84_prv_prefix_hex=NET_PARAMS['bip84_prv_prefix_hex'],
            bip84_pub_prefix_hex=NET_PARAMS['bip84_pub_prefix_hex'], magic_header_hex=NET_PARAMS['magic_header_hex'], default_port=NET_PARAMS['default_port'])
    
    def create_tx(self, satoshis:int, solver_f, generator):
        utxo = self.get_utxo(self)
        address_reciever = json.loads(self.send_rpc(self, 'getnewaddress').text)['result']
        spendables = Spendable(coin_value=int(utxo['value']), script = h2b(utxo['scriptPubKey']), tx_hash = h2b(utxo['transactionId']), tx_out_index=int(utxo['outputIndex']))
        self.unsigned_tx = create_tx(network=self.network, spendables=[spendables], payables=[tuple([address_reciever, satoshis])])
        self.unsigned_tx_hex = self.unsigned_tx.as_hex()
        key_wif = self.network.parse.wif(self.secret_key)
        exponent = key_wif.secret_exponent()
        solver = solver_f([exponent], [generator])

        self.signed_new_tx = self.unsigned_tx.sign(solver)
        self.signed_new_tx_hex = self.signed_new_tx.as_hex()

    @classmethod
    def get_utxo(cls ,self):
        utxo = requests.get(f'https://bcschain.info/api/address/{self.address_sender}/utxo')
        utxo = json.loads(utxo.text)[0]
        return utxo
    
    @classmethod
    def send_rpc(cls, self, method: str, params = []):
        address_reciever = requests.post(f'http://{self.rpc_user}:{self.rpc_pass}@140.82.36.227:3669/', json={'method': method})
        print(address_reciever.text)
        return address_reciever
