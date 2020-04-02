# TurtleCoind

## Running TurtleCoind

Start _TurtleCoind_ with the `--enable-blockexplorer` argument:

```bash
./TurtleCoind --enable-blockexplorer
```

After starting it make sure the block-chain is synchronized. This might take a while. The console log will show a message when it’s done:

```
Successfully synchronized with the TurtleCoin Network
```

The python wrapper can now be used.

## Usage

```python
class TurtleCoind(host = '127.0.0.1', port = 11898, ssl = False)
```

Integrates with the JSON-RPC interface of TurtleCoind.

1. **`get_block_count()`**

         Returns current chain height.

         **NO INPUT**

         _`Return type` : dict_

```python
{
    "jsonrpc":"2.0",
    "result":{
        "count":560915,
        "status":"OK"
    }
}
```

2. **`get_block_hash(height)`**

         Returns block hash for a given height off by one.

| Argument | Mandatory | Description | Data Type |
| :--- | :--- | :--- | :--- |
| height | Yes | The height of the block whose previous hash is to be retrieved. | int |

            `Return type` : _dict_

```python
{
    "jsonrpc":"2.0",
    "result":"4bd7d..."
}
```

3. **`get_block_template(reserve_size, wallet_address)`**

          Returns blocktemplate with an empty "hole" for nonce.

| Argument | Mandatory | Description | Data Type |
| :--- | :--- | :--- | :--- |
| reserve\_size | Yes | Size of the reserve to be specified. | int |
| wallet\_address | Yes | Valid TurtleCoin wallet address | string |

          `Return type` : _dict_

```python
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

          Submits mined block.

| Argument | Mandatory | Description | Data Type |
| :--- | :--- | :--- | :--- |
| block\_blob | Yes | Block blob of the mined block | string  |

          _`Return type`_ : _dict_

```python
{
    "jsonrpc": "2.0",
    "result": {
        "status" : "OK"
    }
} 
```

5. **`get_last_block_header()`** 

          Returns the block header of the last block.

            **NO INPUT**

          _`Return type`_ : _dict_

```python
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

