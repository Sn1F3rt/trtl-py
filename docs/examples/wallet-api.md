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

 
```

