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
class WalletAPI(key, rpc_host = '127.0.0.1', rpc_port = 8070, ssl = False)
```

Integrates with the JSON-PRC interface of Wallet-API.

      1. **`open_wallet(filename, password, daemon_host = '127.0.0.1', daemon_port = 11898)`** 

            Opens an already existing wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :--- | :--- | :---: | :--- | :--- |
| filename | Yes | - | The filename to store the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| daemon\_host | No  | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemon\_port | No | `11898` | The daemon port to sync the wallet with | int |

            `Return Type`  : _int_

**If the operation was successful, `200` is returned else a `ValueError` is raised, with the relevant error message.**

      2. **`import_wallet_key(filename, password, private_view_key, private_spend_key, daemon_host = None, daemon_port = None, scan_height = None)`**

           Imports a wallet with a private view and spend key.

| Argument | Mandatory | Default | Description | DataType |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| private\_view\_key | Yes | - | 64 char hex private view key | str |
| private\_spend\_key | Yes | - | 64 char hex private spend key | str |
| daemon\_host | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemon\_port | No | `11898` | The daemon port to sync the wallet with | int |
| scan\_height | No | - | The block height to start scanning from | int |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      3. **`import_wallet_seed(filename, password, seed, daemon_host = '127.0.0.1', daemon_port = 11898, scan_height  = None)`**

            Imports a wallet using a mnemonic seed. 

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| seed | Yes | - | The 25 words mnemonic seed | str |
| daemon\_host | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemon\_port | No | `11898` | The daemon port to sync the wallet with | int |
| scan\_height | No | - | The block height to start scanning from | int |

            `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      4. **`import_wallet_view(filename, password, private_view_key, address, daemon_host = 127.0.0.1, daemon_port = 11898, scan_height = None)`**

            Imports a view only wallet with a private view key and public address.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| private\_view\_key | Yes | - | 64 char hex private view key | str |
| address | Yes | - | 99 char public TRTL address | str |
| daemon\_host | No | `'127.0.0.1'` | The daemon host to sync the wallet with | str |
| daemon\_port | No | `11898` | The daemon port to sync the wallet with | int |
| scan\_height | No | - | The block height to start scanning from | int |

           `Return Type` : _None_

**If the operation was successful,  no value is returned else a `ValueError` is raised, with the relevant error message.**

      5. **`create_wallet(filename, password, daemon_host = None, daemon_port = None)`**

             Creates a new wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| filename | Yes | - | The filename to load the wallet from. | str |
| password | Yes | - | The password used to open the wallet | str |
| daemon\_host | No | `127.0.0.1` | The daemon host to sync the wallet with | str |
| daemon\_port | No | `11898` | The daemon port to sync the wallet with | int |

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

            Deletes the given sub-wallet from the container.

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

      10. **`create_address()`**

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

            Imports a sub-wallet with the given private spend key. It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the scan height given \(defaults to zero\) if the scan height is less than the height of the current wallet sync status.

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

            Imports a view only sub-wallet with the given `public_spend_key`. It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the `scan_height` given \(defaults to zero\) if the scan height is less than the height of the current wallet sync status.

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

      13. **`integrated_address(address, payment_id)`**

            Creates an integrated address from an address and payment ID.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |
| payment\_id | Yes | - | The payment ID to use for this operation. Should be a 64 char hex string. | str |

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

      15. **`set_node(daemon_host, daemon_port)`**

            Sets the node address and port.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| daemon\_host | Yes | - | The daemon host to sync the wallet with | str |
| daemon\_port | Yes | - | The daemon port to sync the wallet with | int |

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

      20. **`transaction_details(txn_hash)`**

            Returns details on the given transaction, if found.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| txn\_hash | Yes | - | The transaction hash to use for this operation. Should be a 64 char hex string. | str |

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

      23. **`transactions_height(start_height, end_height = None)`**

            Returns transactions for the wallet starting at start height for 1,000 blocks \(or until end height if specified\). Note that start height must be &lt; end height.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| start\_height | Yes | - | The starting block height to use for this operation. | int |
| end\_height | No | 0 | The ending block height to use for this operation. | int |

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

      24. **`transactions_height_address(address, start_height, end_height = None)`**

            Returns transactions for the wallet starting at start height for 1,000 blocks, that belong to the given address \(or until end height if specified\). Note that start height must be &lt; end height. Also note that the transfers list will still contain transfers to other addresses, if present.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to use for this operation. Should be a valid, 99 character TRTL address. | str |
| start\_height | Yes | - | The starting block height to use for this operation. | int |
| end\_height | No | 0 | The ending block height to use for this operation. | int |

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

      25. **`send_basic(address, amount, payment_id = None)`**

            Sends a transaction. This method will take funds from all sub-wallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. **If this is not acceptable, please use the send\_advanced method instead.**

| **Argument** | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| address | Yes | - | The address to send funds to. | str |
| amount | Yes | - | The amount of TRTL to send. | int |
| payment\_id | No | - | The payment ID to use. | str |

            `Return Type` : _dict_

```python
#Expected Output

{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": true
}
```

      26. **`prepare_basic(amount, address = None, payment_is = None)`**

            Creates a transaction but does not relay it to the network. This method will take funds from all sub-wallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. **If this is not acceptable, please use the prepare\_advanced method instead**. Allows you to review the created transactions fee before deciding whether to commit to paying that fee. **Prepared transactions can be sent using send\_prepared method, or cancelled with cancel\_prepared method**. 

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| amount | Yes | - | The amount of TRTL to send. | int |
| address | No | - | The address to send funds to. | str |
| payment\_id | No | No payment ID. | The payment ID to use. | str |

            `Return Type` : _dict_ **\(Also note that the fee returned is in atomic units. Divide it by 100 to get the amount in TRTL\)**

```python
#Expected Output

{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": false
}
```

      27. **`send_advanced(destination, mixin=None, fee=None, fee_per_byte=None,payment_id=None, source_addresses=None, change_address=None, unlock_time=None, extra=None)`**

            Sends a transaction. Custom configurations for sending transactions are available here.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| destination | Yes | - | List of dictionaries with address and amount \(in atomic units\) as keys.  | list |
| mixin | No | The default mixin defined by the core software for the current height. | The mixin level to use. | int |
| fee | No | 0 | The fee in TRTL to use with this transaction. | int |
| fee\_per\_byte | No | 0 | The amount in TRTL to pay for each byte of the resulting transaction size. | int |
| payment\_id | No | - | The payment ID to use. | str |
| source\_addresses | No | Every address in the wallet container. | List of the addresses to draw funds for the transaction from \(must be  addresses in this container\), | list |
| change\_address | No | Primary address. | The address in this wallet to return any ‘change’ to if we have to spend more than the requested amount. | str |
| unlock\_time | No | 0 | When to unlock the transaction. A user cannot spend locked funds until the unlock time has been reached. Can use either a block height, or a unix timestamp. | int |
| extra | No | - |  Hex representation of any extra data to be included in the `tx_extra` field of the transaction. | str |

            `Return Type` : _dict_

```python
{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": true
}
```

      28. **`prepare_advanced(destination, mixin=None, fee=None, fee_per_byte=None, payment_id=None, source_addresses=None, change_address=None, unlock_time=None, extra=None)`**

            Creates a transaction but does not relay it to the network. Custom configurations for sending transactions are available here.

| Argument | Mandatory | Default | Description | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| destination | Yes | - | List of dictionaries with address and amount \(in atomic units\) as keys.  | list |
| mixin | No | The default mixin defined by the core software for the current height. | The mixin level to use.  | int |
| fee | No | 0 | The fee in TRTL to use with this transaction. | int |
| fee\_per\_byte | No | 0 | The amount in TRTL to pay for each byte of the resulting transaction size. | int |
| payment\_id | No | - | The payment ID to use.  | str |
| source\_addresses | No | Every address in the wallet container.  | List of the addresses to draw funds for the transaction from \(must be  addresses in this container\), | list |
| unlock\_time | No | 0 | When to unlock the transaction. A user cannot spend locked funds until the unlock time has been reached. Can use either a block height, or a unix timestamp. | int |
| extra | No | - | Hex representation of any extra data to be included in the `tx_extra` field of the transaction. | str |

            `Return Type` : _dict_

```python
{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f",
  "fee": 1000,
  "relayedToNetwork": false
}
```

      29. **`send_prepared(txn_hash)`**

            Sends a previously prepared transaction.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| txn\_hash  | Yes | - |  The transaction hash returned by a previous **prepare\_basic** or **prepare\_advanced** call | str |

            `Return Type` : _dict_

```python
{
  "transactionHash": "1982d8903c5e2b0914e6586e5b715758823e4903c2bacda7aa519ff6feb1476e"
}
```

      30. **`cancel_prepared(txn_hash)`**

            Cancels a previously prepared transaction. While it is not mandatory to call this method for a prepared transaction you do not wish to send, it is highly advised, as it will free up RAM.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| txn\_hash | Yes | - |  The prepared transaction hash to cancel. This hash is returned from the `prepare_basic` or `prepare_advanced` methods. | str |

      `Return Type` : No value returned.

      31. **`send_fusion_basic()`**

            Fusion transactions are zero fee, and seek to combine small inputs into larger ones, to allow for larger transactions. Many fusions may be required to fully optimize a wallet.  

            **NO INPUT**

            `Return Type`: _dict_

```python
{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f"
}
```

      32. **`send_fusion_advanced(mixin=None, destination=None, source_addresses=None, optimize_target=None)`**

            Fusion transactions are zero fee, and seek to combine small inputs into larger ones, to allow for larger transactions. Many fusions may be required to fully optimize a wallet.

| Argument | Mandatory | Default | Description | Data Type |
| :---: | :---: | :---: | :---: | :---: |
| mixin | No | - | The mixin level to use | int |
| destination | No | - | The destination address to send funds to. Must exist in this wallet. | str |
| source\_addresses | No | - | The addresses to draw funds for the transaction from \(must be addresses in this container\) | list |
| optimize\_target | No | - | If given, we will not fuse inputs larger than this value. Value given must be a valid input amount, i.e. only a single significant leading digit. For example, 20000 is fine, 23456 is not. | int |

            `Return Type` : _dict_

```python
{
  "transactionHash": "396e2a782c9ce9993982c6f93e305b05306d0e5794f57157fbac78581443c55f"
}
```

