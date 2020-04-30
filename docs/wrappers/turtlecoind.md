# TurtleCoind

## Running TurtleCoind

Start _TurtleCoind_ with the `--enable-blockexplorer` cli argument:

```
./TurtleCoind --enable-blockexplorer
```

After starting it make sure the block-chain is synchronized. This might take a while. The console log will show a message when it’s done:

```bash
Successfully synchronized with the TurtleCoin Network
```

You can now use the wrapper for TurtleCoind. 

## Usage

```python
class TurtleCoind(host = '127.0.0.1', port = 11898, ssl = False, timeout=5)
```

Integrates with the JSON-RPC interface of TurtleCoind.

1. **`get_block_count()`**

         _Returns current chain height._

         **NO INPUT**

         `Return type` _: dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "count":560915,
        "status":"OK"
    }
}
```

     2. **`get_block_hash(height)`**

           _Returns block hash for a given height off by one._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| height | Yes | The height of the block whose previous hash is to be retrieved. | int |

            `Return type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":"4bd7d..."
}
```

      __3. **`get_block_template(reserve_size, wallet_address)`**

            _Returns blocktemplate with an empty "hole" for nonce._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| reserve\_size | Yes | Size of the reserve to be specified. | int |
| wallet\_address | Yes | Valid TurtleCoin wallet address | str |

            `Return type` : _dict_

```python
#Expected Output

{
    "jsonrpc": "2.0",
    "result": {
        "blocktemplate_blob": "0100de...",
        "difficulty": 65563,
        "height": 123456,
        "reserved_offset": 395,
        "status": "OK"
    }
}
```

      4. **`submit_block(block_blob)`** 

            _Submits mined block._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| block\_blob | Yes | Block blob of the mined block | str |

            `Return type` : _dict_

```python
#Expected Output

{
    "jsonrpc": "2.0",
    "result": {
        "status" : "OK"
    }
} 
```

      5. **`get_last_block_header()`** 

            _Returns the block header of the last block._

            **NO INPUT**

            `Return type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "block_header":{
            "block_size":86171,
            "depth":0,
            "difficulty":431119113,
            "hash":"b746b...",
            "height":561342,
            "major_version":4,
            "minor_version":0,
            "nonce":715846563,
            "num_txes":4,
            "orphan_status":false,
            "prev_hash":"b8e02...",
            "reward":2930801,
            "timestamp":1529750993
        },
        "status":"OK"
    }
}
```

      6. **`get_block_header_by_hash(hash)`**

            _Returns block header by given block hash._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| hash | Yes | Hash of the block | str |

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "block_header":{
            "block_size":11640,
            "depth":437898,
            "difficulty":70050782,
            "hash":"30706...",
            "height":123456,
            "major_version":3,
            "minor_version":0,
            "nonce":3177228614,
            "num_txes":3,
            "orphan_status":false,
            "prev_hash":"4bd7d...",
            "reward":2969487,
            "timestamp":1516631879
        },
    "status":"OK"
    }
}
```

      7. **`get_block_header_by_height(height)`**

            _Returns block header by given block height._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| height | Yes | Height of the block | int |

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "block_header":{
            "block_size":11640,
            "depth":437898,
            "difficulty":70050782,
            "hash":"30706...",
            "height":123456,
            "major_version":3,
            "minor_version":0,
            "nonce":3177228614,
            "num_txes":3,
            "orphan_status":false,
            "prev_hash":"4bd7d...",
            "reward":2969487,
            "timestamp":1516631879
        },
    "status":"OK"
    }
}
```

      8. **`get_currency_id()`**

            _Returns unique currency identifier._

            **NO INPUT**

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "currency_id_blob":"7fb97..."
    }
}
```

      9. **`get_blocks(height)`**

            _Returns information on the last 30 blocks before height \(inclusive\)_

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| height | Yes | Height of the last block to be included in the result | int |

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc": "2.0",
    "result": {
        "blocks":[
            {
                "cumul_size": 22041,
                "difficulty": 285124963,
                "hash": "62f00...",
                "height": 500000,
                "timestamp": 1527834137,
                "tx_count": 4
            }
        ],
        "status": "OK"
    }
}
```

      10. **`get_block(hash)`**

            _Returns information on a single block_

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| hash | Yes | Hash of the block | str |

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "block":{
            "alreadyGeneratedCoins":"1659188157030",
            "alreadyGeneratedTransactions":1097221,
            "baseReward":2930784,
            "blockSize":384,
            "depth":1,
            "difficulty":264289473,
            "effectiveSizeMedian":100000,
            "hash":"980ff...",
            "height":561537,
            "major_version":4,
            "minor_version":0,
            "nonce":60779,
            "orphan_status":false,
            "penalty":0.0,
            "prev_hash":"c37f8...",
            "reward":2930784,
            "sizeMedian":265,
            "timestamp":1529757254,
            "totalFeeAmount":0,
            "transactions":[
                {
                    "amount_out":2930784,
                    "fee":0,
                    "hash":"c0a2d...",
                    "size":265
                }
            ],
            "transactionsCumulativeSize":265
        },
        "status":"OK"
    }
}
```

      11. **`get_transaction(hash)`**

            _Returns information on the single transaction._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| hash  | Yes  | Hash of the transaction | str |

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "block":{
            "cumul_size":22041,
            "difficulty":106780143,
            "hash":"62f00...",
            "height":500000,
            "timestamp":1527834137,
            "tx_count":4
        },
        "status":"OK",
        "tx":{
            "extra":"019e4...",
            "unlock_time":500040,
            "version":1,
            "vin":[
                {
                    "type":"ff",
                    "value":{
                        "height":500000
                    }
                }
            ],
            "vout":[
                {
                    "amount":80,
                    "target":{
                        "data":{
                            "key":"5ce69..."
                        },
                        "type":"02"
                    }
                }
            ]
        },
        "txDetails":{
            "amount_out":2936280,
            "fee":0,
            "hash":"702ad...",
            "mixin":0,
            "paymentId":"",
            "size":266
        }
    }
}
```

      12. **`get_transaction_pool()`**

            _Returns the list of transaction hashes in the mempool._

            **NO INPUT**

            `Return Type` : _dict_

```python
#Expected Output

{
    "jsonrpc":"2.0",
    "result":{
        "status":"OK",
        "transactions":[
            {
                "amount_out":8990,
                "fee":10,
                "hash":"a5e88...",
                "size":541
            }
        ]
    }
}
```

