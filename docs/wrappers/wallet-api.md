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

            `Return Type` : _int_

**If the operation was successful, `200` is returned else a `ValueError` is raised, with the relevant error message.**

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

**If the operation was successful, `200` is returned else a `ValueError` is raised, with the relevant error message.**

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

           `Return Type` : _int_

**If the operation was successful, `200` is returned else a `ValueError` is raised, with the relevant error message.**

