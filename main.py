from eth_account import Account
from web3 import Web3
import time

address = '交易所地址'
# gas乘基数，后面会/100，如果设置1.05 就写105
mul = 110
web3 = Web3(Web3.HTTPProvider("https://mainnet.era.zksync.io"))

with open('account.txt', mode='r') as file:
    privates = file.read().splitlines()

if __name__ == '__main__':
    for i, pk in enumerate(privates):
        try:
            print(pk)
            ac = Account.from_key(pk.strip())
            bal = web3.eth.get_balance(ac.address)
            eth_bal = web3.from_wei(bal, 'ether')
            print(ac.address + "，余额" + str(eth_bal))
            gas_price = web3.eth.gas_price
            tx = {
                'from': ac.address,
                'to': web3.to_checksum_address(address),
                'gasPrice': gas_price,
                'data': '0x',
                'nonce': web3.eth.get_transaction_count(ac.address),
                'chainId': 324,
                'value': 0
            }
            gas_limit = web3.eth.estimate_gas(tx)
            if gas_limit is None:
                raise Exception("Unable to estimate the gas limit.")
            tx.update({
                'gas': gas_limit,
                'value': bal - int((gas_price * gas_limit) * mul / 100)
            })
            signed_tx = ac.sign_transaction(tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f'Transaction sent: {tx_hash.hex()}')
            print(tx)
        except Exception as e:
            print(e)
            print("error -----------")
            time.sleep(1)
