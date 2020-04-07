# Wallet-API

## Starting Wallet-API

Start _wallet-api_ like this:

```bash
./wallet-api --rpc-password somepassword
```

An RPC password is always required, and you should then provide this password as the `key` parameter while initializing the wrapper.

You can now use the Python Wrapper for Wallet-API.

## Usage

```python
class WalletAPI(key, RPC_Host = '127.0.0.1', RPC_Port = 8070, ssl = False)
```

Integrates with the JSON-PRC interface of Wallet-API.

      1. **`open_wallet(filename, password, daemonHost = '127.0.0.1', daemonPort = 11898)`** 

            Opens an already existing wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :--- | :--- | :---: | :--- | :--- |
| filename | Yes | - | The filename to store the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| daemonHost | No  | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemonPort | No | `11898` | The daemon port to sync the wallet with | int |

            `Return Type`  : _int_

**If the operation was successful, `200` is returned else a `ValueError` is raised, with the relevant error message.**

      2. **`import_wallet_key(filename, password, privateViewKey, privateSpendKey, daemonHost = None, daemonPort = None, scanHeight = None)`**

           Imports a wallet with a private view and spend key.

| Argument | Mandatory | Default | Description | DataType |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| privateViewKey | Yes | - | 64 char hex private view key | str |
| privateSpendKey | Yes | - | 64 char hex private spend key | str |
| daemonHost | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemonPort | No | `11898` | The daemon port to sync the wallet with | int |
| scanHeight | No | - | The block height to start scanning from | int |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      3. **`import_wallet_seed(filename, password, seed, daemonHost = '127.0.0.1', daemonPort = '11898', scanHeight  = None)`**

            Imports a wallet using a mnemonic seed. 

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| seed | Yes | - | The 25 words mnemonic seed | str |
| daemonHost | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemonPort | No | `11898` | The daemon port to sync the wallet with | int |
| scanHeight | No | - | The block height to start scanning from | int |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      4. **`import_wallet_view(filename, password, privateViewKey, address, daemonHost = 127.0.0.1, daemonPort = 11898, scanHeight = None)`**

            Imports a view only wallet with a private view key and public address.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| privateViewKey | Yes | - | 64 char hex private view key | str |
| address | Yes | - | 99 char public TRTL address | str |
| daemonHost | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemonPort | No | `11898` | The daemon port to sync the wallet with | int |
| scanHeight | No | - | The block height to start scanning from | int |

           `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      5. **`create_wallet(filename, password, daemonHost = None, daemonPort = None)`**

             Creates a new wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| daemonHost | No | `127.0.0.1` | The daemon host to sync the wallet with | str |
| daemonPort | No | `11898` | The daemon port to sync the wallet with | int |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      6. **`delete_wallet()`**

            Closes and saves the opened wallet.

            **NO INPUT**

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      7. **`addresses()`**

            Gets a list of all addresses in the wallet container.

            **NO INPUT**

            `Return Type`: _dict_

```python
#Expected Output

{
  "addresses": [
    "TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq"
  ]
}
```

      8. **`delete_address(address)`**

            Deletes the given subwallet from the container.

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| address | Yes | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      9. **`primary_address()`**

            Gets the 'primary' address.

            **NO INPUT**

            `Return Type` : _dict_

```python
{
  "address": "TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq"
}
```

      10. **`create_address`**

            Creates a new, random address in the wallet container.

            **NO INPUT**

            `Return Type` : _dict_

```python
{
  "address": "TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq",
  "privateSpendKey": "6d4a7c160cbd4c9de33eeb161ff30539d2e28b447eb5af73523cc3379c591c83",
  "publicSpendKey": "6d4a7c160cbd4c9de33eeb161ff30539d2e28b447eb5af73523cc3379c591c83"
}
```

      11. **`import_address(private_spend_key, scan_height = None)`**

            Imports a subwallet with the given private spend key. It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the scan height given \(defaults to zero\) if the scan height is less than the height of the current wallet sync status.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| private\_spend\_key | Yes | - | 64 char hex private spend key | str |
| scan\_height | No | 0 | The block height to start scanning from | int |

            `Return Type` : _dict_

```python
{
  "address": "TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq"
}
```

      12. **`import_address_view(public_spend_key, scan_height = None)`**

            Imports a view only subwallet with the given publicSpendKey. It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the scan height given \(defaults to zero\) if the scan height is less than the height of the current wallet sync status.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| public\_spend\_key | Yes | - | 64 char hex public spend key. | str |
| scan\_height | No | 0 | The block height to start scanning from. | int |

            `Return Type` : _dict_

```python
{
  "address": "TRTLv2cT32cZbF6KvnU69LNxptYFBMCKs3yqLmCAVjPW4rNTExpB7RpGKGJEkD1E9MVmM8SUUJfUh42Ajo1Hgz5wUN6budvzaq"
}
```

      13. **`integrated_address(address, paymentID)`**

            Creates an integrated address from an address and payment ID.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |
| paymentID | Yes | - | The payment ID to use for this operation. Should be a 64 char hex string. | str |

            `Return Type` : _dict_

```python
{
  "integratedAddress": "TRTLuxiNXhy96RNDkv2jx29jL7GdTWYBmA4r7K8KRpDWA4hJJnTZEgFHFzxqvmBLtz94oF4uPokQdHbV9j2g7S6LA4hKPvjZEFS2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3BoCpXD"
}
```

      14. **`get_node(private_spend_key, scan_height = None)`**

            Gets the node address, port, fee, and fee address.

            **NO INPUT**

            `Return Type` : _dict_

```python
{
  "daemonHost": "127.0.0.1",
  "daemonPort": 11898,
  "nodeFee": 1000,
  "nodeAddress": "TRTLv2Fyavy8CXG8BPEbNeCHFZ1fuDCYCZ3vW5H5LXN4K2M2MHUpTENip9bbavpHvvPwb4NDkBWrNgURAd5DB38FHXWZyoBh4wW"
}
```

      15. **`set_node(daemonHost, daemonPort)`**

            Sets the node address and port.

| Argument | Mandatory | Default | Description | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| daemonHost | Yes | - | The daemon host to sync the wallet with | str |
| daemonPort | Yes | - | The daemon port to sync the wallet with | int |

            **If the operation was successful, no value is returned. Otherwise, a `ValueError` is raised with the relevant error message.**

      16. **`wallet_keys()`**

            Gets the wallet containers shared private view key. 

            **NO INPUT** 

            `Return Type` : _dict_

```python
{
  "privateViewKey": "85baeb8ae23bf266c68a5845f1ff13af7ff221f46e4dfc1293eec9a3e211a90a"
}
```

      17. **`address_keys(address)`**

            Gets the public and private spend key for the given address. Note that this method cannot be used with a view only wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |

            `Return Type` : _dict_

```python
{
  "privateSpendKey": "85baeb8ae23bf266c68a5845f1ff13af7ff221f46e4dfc1293eec9a3e211a90a",
  "publicSpendKey": "85baeb8ae23bf266c68a5845f1ff13af7ff221f46e4dfc1293eec9a3e211a90a"
}
```

      18. **`mnemonic(address)`**

            Gets the mnemonic seed for the given address, if possible. Note that this method cannot be used with a view only wallet. 

| Argument | Mandatory | Default | Description | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |

             `Return type` : _dict_

```python
#Excepted Output

{
  "mnemonicSeed": "leech lifestyle newt tarnished vials weavers decay nerves buying taken sample after jailed cupcake token pavements welders gifts ferry keep humid abbey emails entrance leech"
}
```

      19. **`transactions()`**

            Returns a list of all transactions in the wallet container.

            **NO INPUT**

            `Return Type` : _dict_

```python
{
  "transactions": [
    {
      "blockHeight": 800000,
      "fee": 10,
      "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
      "isCoinbaseTransaction": false,
      "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
      "timestamp": 1543222082,
      "unlockTime": 0,
      "transfers": {
        "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
        "amount": 1234
      }
    }
  ]
}
```

      20. **`transaction_details(hash)`**

            Returns details on the given transaction, if found.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| hash | Yes | - | The transaction hash to use for this operation. Should be a 64 char hex string. | str |

            `Return Type` : _dict_

```python
{
  "transactions": {
    "blockHeight": 800000,
    "fee": 10,
    "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
    "isCoinbaseTransaction": false,
    "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
    "timestamp": 1543222082,
    "unlockTime": 0,
    "transfers": {
      "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
      "amount": 1234
    }
  }
}
```

      21. **`unconfirmed_transactions()`**

            Gets a list of all unconfirmed, outgoing transactions in the wallet container. Note that this DOES NOT include incoming transactions in the pool. This only applies to transactions that have been sent by this wallet file, and have not been added to a block yet.

            **NO INPUT**

          `Return Type` : _dict_

```python
{
  "transactions": [
    {
      "blockHeight": 800000,
      "fee": 10,
      "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
      "isCoinbaseTransaction": false,
      "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
      "timestamp": 1543222082,
      "unlockTime": 0,
      "transfers": {
        "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
        "amount": 1234
      }
    }
  ]
}
```

      22. **`unconfirmed_address(address)`**

            Returns a list of unconfirmed, outgoing transactions, for the given address. Note that this DOES NOT include incoming transactions in the pool. This only applies to transactions that have been sent by this wallet file, and have not been added to a block yet. 

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |

            `Return Type` : _dict_

```python
{
  "transactions": [
    {
      "blockHeight": 800000,
      "fee": 10,
      "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
      "isCoinbaseTransaction": false,
      "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
      "timestamp": 1543222082,
      "unlockTime": 0,
      "transfers": {
        "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
        "amount": 1234
      }
    }
  ]
}
```

      23. **`transactions_height(startHeight, endHeight = None)`**

            Returns transactions for the wallet starting at start height for 1,000 blocks \(or until end height if specified\). Note that start height must be &lt; end height.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| startHeight | Yes | - | The starting block height to use for this operation. | int |
| endHeight | No | 0 | The ending block height to use for this operation. | int |

            `Return Type` : _dict_

```python
#Expected Output

{
  "transactions": [
    {
      "blockHeight": 800000,
      "fee": 10,
      "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
      "isCoinbaseTransaction": false,
      "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
      "timestamp": 1543222082,
      "unlockTime": 0,
      "transfers": {
        "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
        "amount": 1234
      }
    }
  ]
}
```

      24. **`transactions_height_address(address, startHeight, endHeight = None)`**

            Returns transactions for the wallet starting at start height for 1,000 blocks, that belong to the given address \(or until end height if specified\). Note that start height must be &lt; end height. Also note that the transfers list will still contain transfers to other addresses, if present.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |
| startHeight | Yes | - | The starting block height to use for this operation. | int |
| endHeight | No | 0 | The ending block height to use for this operation. | int |

            `Return Type` : _dict_

```python
#Expected Output

{
  "transactions": [
    {
      "blockHeight": 800000,
      "fee": 10,
      "hash": "8e2dc89659409ea9c34a2e28f7350cefba304159c04cc4926acd12035a8b2379",
      "isCoinbaseTransaction": false,
      "paymentID": "7fe73bd90ef05dea0b5c15fc78696619c50dd5f2ba628f2fd16a2e3445b1922f",
      "timestamp": 1543222082,
      "unlockTime": 0,
      "transfers": {
        "address": "TRTLv3ErzkY2CiAj6DL8isYELmTec8Z9BK56oL1KMhjMRSMyfwYaogKg17hQKC23CHPBcHqrHHGzdRYUk3HGqkMwXbHg3Dy2rH",
        "amount": 1234
      }
    }
  ]
}
```

      25. **`send_basic(dest_addr, amount, paymentID = None)`**

            Sends a transaction. This method will take funds from all sub-wallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. **If this is not acceptable, please use the send\_advanced method instead.**

| **Argument** | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to send funds to. | str |
| amount | Yes | - | The amount of TRTL to send. | int |
| paymentID | No | - | The payment ID to use. | str |

            `Return Type` : _dict_

```python
#Expected Output

{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": true
}
```

      26. **`prepare_basic(amount, address = None, paymentID = None)`**

            Creates a transaction but does not relay it to the network. This method will take funds from all sub-wallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. **If this is not acceptable, please use the prepare\_advanced method instead**. Allows you to review the created transactions fee before deciding whether to commit to paying that fee. **Prepared transactions can be sent using send\_prepared method, or cancelled with cancel\_prepared method**. 

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| amount | Yes | - | The amount of TRTL to send. | int |
| address | No | - | The address to send funds to. | str |
| paymentID | No | - | The payment ID to use. | str |

            `Return Type` : _dict_ **\(Also note that the fee returned is in atomic units. Divide it by 100 to get the amount in TRTL\)**

```python
#Expected Output

{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": false
}
```

      27. 



      28. 



      29. **`send_prepared(hash)`**

            Sends a previously prepared transaction.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| hash  | Yes | - |  The transaction hash returned by a previous **prepare\_basic** or **prepare\_advanced** call | str |

            `Return Type` : _dict_

```python
{
  "transactionHash": "1982d8903c5e2b0914e6586e5b715758823e4903c2bacda7aa519ff6feb1476e"
}
```

      30. **`cancel_prepared(hash)`**

            Cancels a previously prepared transaction. While it is not mandatory to call this method for a prepared transaction you do not wish to send, it is highly advised, as it will free up RAM.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| hash | Yes | - |  The prepared transaction hash to cancel. This hash is returned from the `prepare_basic` or `prepare_advanced` methods. | str |

      `Return Type` : No value returned.

