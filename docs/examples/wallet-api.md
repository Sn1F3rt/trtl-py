---
description: Examples for usage of the wallet-api wrapper.
---

# Wallet-API

```python
from trtl import WalletAPI

password = 'mysupersecretpassword'
rpc_host = 'localhost'
rpc_port = 11898
ssl = False

#Inilialization
wallet_api = WalletAPI(key = password, host = rpc_host, port = rpc_port, ssl = False)

#open_wallet
file = 'wallet.turtle'
passwd = 'yourpassword'

wallet_api.open_wallet(file, passwd)

#import_wallet_key
file = 'wallet.turtle'
passwd = 'yourpassword'
view_key = '493f522e1f46b5c07f753ed28dc2db9da5f571f28c2fa54f4c9a0a7941b09d0b'
spend_key = '5c703d9bde0b7cd5ff3e19ea826a44066534661a7322c85e854e73f06e49cd06'

wallet_api.import_wallet_key(file, passwd, view_key, spend_key)

#import_wallet_seed
file = 'wallet.turtle'
passwd = 'yourpassword'
mnemonic_seed = 'cynical waveform sixteen husband zebra ritual vexed jaws eccentric jewels toenail having nabbing wept nozzle grunt tipsy flying pegs feel upright lower racetrack sapling sapling'

wallet_api.import_wallet_seed(file, passwd, mnemonic_seed)

#import_wallet_view
file = 'wallet.turtle'
passwd = 'yourpassword'
view_key = '493f522e1f46b5c07f753ed28dc2db9da5f571f28c2fa54f4c9a0a7941b09d0b'
addr = 'TRTLv2Fyavy8CXG8BPEbNeCHFZ1fuDCYCZ3vW5H5LXN4K2M2MHUpTENip9bbavpHvvPwb4NDkBWrNgURAd5DB38FHXWZyoBh4wW'

wallet_api.import_wallet_view(file, passwd, view_key, addr)

#create_wallet
file = 'wallet.turtle'
passwd = 'yourpassword'

wallet_api.create_wallet(file, passwd)

#delete_wallet

wallet_api.delete_wallet()

#addresses
addr = wallet-api.addresses()

print(addr)

#delete_address
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

wallet_api.delete_address(addr)

#primary address
addr = wallet_api.primary_address()

print(addr)

#create_address    
addr_details = wallet_api.create_address()

print(addr_details)

#import_address
spend_key = '5c703d9bde0b7cd5ff3e19ea826a44066534661a7322c85e854e73f06e49cd06'

wallet_api.import_address(spend_key, 300000)

#import_address_view
public_spend_key = '5c703d9bde0b7cd5ff3e19ea826a44066534661a7322c85e854e73f06e49cd06'

wallet_api.import_address_view(public_spend_key, 300000)

#integrated_address
payment_id = '38a8224a4c8bc5f060555cf9e89551dcd0cbb1c587a52b63e98f71280c362ee4'
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

integrated_addr = wallet_api.integrated_address(payment_id, addr)
print(integrated_addr)

#get_node
node_details = wallet_api.get_node()

print(node_details)

#set_node
daemon_host = 'localhost'
daemon_port = 11898

wallet_api.set_node(daemon_host, daemon_port)

#wallet_keys
keys = wallet_api.wallet_keys()

print(keys)

#address_keys
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

keys = wallet_api.address_keys(addr)
print(keys)

#mnemonic
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

mnemonic_seed = wallet_api.mnemonic(addr)
print(mnemonic_seed)

#transactions
response = wallet_api.transactions()

print(response) 
 
#transaction_details
hash = '396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f'

response = wallet_api.transaction_details(hash)
print(response)

#unconfirmed_transactions
response = wallet_api.transaction_details()

print(response)

#unconfirmed_address
addrs = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

response = wallet_api.unconfirmed_address(addr)
print(response)

#transactions_height
start = 300000
end = 1000000  #optional

response = wallet_api.transactions_height(start, end)

#transactions_height_address
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'
start = 300000
end = 1000000

response = wallet_api.transactions_height_address(addr, start, end)
print(response)

#send_basic
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'
amt = 1234
pay_id = '38a8224a4c8bc5f060555cf9e89551dcd0cbb1c587a52b63e98f71280c362ee4'

response = wallet_api.send_basic(addr, amt, pay_id)
print(response)

#prepare_basic
amt = 1234

response = wallet_api.prepare_basic(addr, amt, pay_id)
print(response)

#send_advanced
dest = [
    {
      "address": "TRTLv2Fyavy8CXG8BPEbNeCHFZ1fuDCYCZ3vW5H5LXN4K2M2MHUpTENip9bbavpHvvPwb4NDkBWrNgURAd5DB38FHXWZyoBh4wW",
      "amount": 1234
    },
    {
      "address": "TRTLv3r4N3Jbk7FApJXN3M66xWWr8FhbAiwGdEJC2wF1hTKGxnwUzhH8pFydrruvdtPSVTCMUKWGdSrAitgnEVFp8356HCkKHZG",
      "amount": 5000
    }
  ]
source_addr = ['TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq']
change_addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

response = wallet_api.send_advanced(destination = dest, source_addresses = source_addr, change_address = change_addr)
print(response)

#prepare_advanced
dest = [
    {
      "address": "TRTLv2Fyavy8CXG8BPEbNeCHFZ1fuDCYCZ3vW5H5LXN4K2M2MHUpTENip9bbavpHvvPwb4NDkBWrNgURAd5DB38FHXWZyoBh4wW",
      "amount": 1234
    },
    {
      "address": "TRTLv3r4N3Jbk7FApJXN3M66xWWr8FhbAiwGdEJC2wF1hTKGxnwUzhH8pFydrruvdtPSVTCMUKWGdSrAitgnEVFp8356HCkKHZG",
      "amount": 5000
    }
  ]
source_addr = ['TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq']

response = wallet_api.prepare_advanced(destination = dest, source_addresses = source_addr)
print(response)

#send_prepared
hash = '396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f'

response = wallet_api.send_prepared(hash)
print(response)

#cancel_prepared
hash = '396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f'

wallet_api.cancel_prepared(hash)

#send_fusion_basic
response = wallet_api.send_fusion_basic()
print(response)

#send_fusion_advanced
opt = 20000

response = wallet_api.send_fusion_advnaced(optimize_target = opt)
print(response)

#transactions_private_key
hash = ''

response = wallet_api.transactions_private_key(hash)
print(response)

#wallet_balance
response = wallet_api.balance()

print(response)

#address_balance
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

response = wallet_api.address_balance(addr)
print(response)

#balances
response = wallet_api.balances()

print(response)

#save
wallet_api.save()

#export
file = 'wallet.json'

wallet_api.export(file)

#reset
height = 300000

wallet_api.reset(height)

#validate
addr = 'TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq'

response = wallet_api.validate(addr)
print(response)

#status
response = wallet_api.status()

print(response)
```

