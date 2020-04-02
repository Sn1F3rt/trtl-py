---
description: Examples for usage of the TurtleCoind API Wrapper.
---

# TurtleCoind

```python
from trtl import TurtleCoind

daemon_host = 'localhost'
daemon_port = 11898
ssl = False

#Inilialization
turtlecoind = TurtleCoind(daemon_host, daemon_port, ssl)

#getblockcount
response = turtlecoind.get_block_count()
print(response)

#getblockhash
height = 123456
response = turtlecoind.get_block_hash(height)
print(response)

#getblocktemplate
reserve_size = 200
wallet_address = 'TRTLxxxx...'

response = turtlecoind.get_block_template(reserve_size, wallet_address)
print(response)

#submitblock
block_blob = '0100b...'
response = turtlecoind.submit_block(block_blob)
print(response)

#getlastblockheader
response = turtlecoind.get_last_block_header()
print(response)

#getblockheaderbyhash
hash = '30706...'
response = turtlecoind.get_block_header_by_hash(hash)
print(response)

#getblockheaderbyheight
height = 123456
response = turtlecoind.get_block_header_by_height(height)
print(response)

#getcurrencyid
response = turtlecoind.get_currency_id()
print(response)

#getblocks
height = 500000
response = turtlecoind.get_blocks(height)
print(response)

#getblock
hash = '980ff...'
response = turtlecoind.get_block(hash)
print(response)

#gettransaction
hash = '702ad...'
response = turtlecoind.get_transaction(hash)
print(response)

#gettransactionpool
response = turtlecoind.get_transaction_pool()
print(response)
```

