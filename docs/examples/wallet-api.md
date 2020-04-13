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


```

