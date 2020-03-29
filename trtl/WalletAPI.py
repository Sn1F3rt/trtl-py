import json
import requests

class WalletAPI:
    """
    Integrates with WalletAPI RPC interface.

    Run wallet-api like:

        ./wallet-api --rpc-password "mypassword"
    """

    def __init__(self, key, RPC_Host = '127.0.0.1', RPC_Port = 8070, ssl = False):
        if ssl:
            self.url = f'https://{RPC_Host}:{RPC_Port}'
        else:
            self.url = f'http://{RPC_Host}:{RPC_Port}'
        self.headers = {'X-API-KEY': f'{key}'}
        self.errorMsg = {
            "401" : "API key is missing or invalid.",
            "403" : ["A wallet is already open. Call DELETE on /wallet first, to close it.", "This operation requires a wallet to be open, and one has not been opened."],
            "500" : "An exception was thrown whilst processing the request. See the console for logs."
        }

    def _get_request(self, method):
        get_url = self.url + '/' + method

        response = requests.get(get_url, headers = self.headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            errCd = dict(response.json())['errorCode']
            errMsg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{errCd} : {errMsg}')
        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])
        elif response.status_code == 403:
            raise ValueError(self.errorMsg[403])
        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])
        else:
            pass

    def _post_request(self, method, body):
        post_url = self.url + '/' + method

        response = requests.post(post_url, data=body, headers=self.headers)

        if response.status_code in [200, 201]:
            return response.json()
        elif response.status_code == 400:
            errCd = dict(response.json())['errorCode']
            errMsg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{errCd} : {errMsg}')
        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])
        elif response.status_code == 403:
            if method in ['wallet/open', 'wallet/import/key', 'wallet/import/seed', 'wallet/import/view', 'wallet/create']:
                raise ValueError(self.errorMsg[403][0])
            else:
                raise ValueError(self.errorMsg[403][1])
        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])
        else:
            pass

    def _delete_request(self, method):
        delete_url = self.url + '/' + method

        response = requests.get(delete_url, headers = self.headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            errCd = dict(response.json())['errorCode']
            errMsg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{errCd} : {errMsg}')
        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])
        elif response.status_code == 403:
            raise ValueError(self.errorMsg[403])
        elif response.status_code == 404:
            raise ValueError('Transaction hash not found.')
        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])
        else:
            pass

    def _put_request(self, method):
        put_url = self.url + '/' + method

        response = requests.put(put_url, headers = self.headers)

        if response.status_code == 202:
            return response.json()
        elif response.status_code == 400:
            errCd = dict(response.json())['errorCode']
            errMsg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{errCd} : {errMsg}')
        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])
        elif response.status_code == 403:
            raise ValueError(self.errorMsg[403])
        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])
        else:
            pass

    #Start `wallet` - Opening, creating, and closing wallets

    def open_wallet(self, filename, password, daemonHost = None, daemonPort = None):
        """
        Opens an already existing wallet
        """

        params = {"filename" : f'{filename}', "password" : f'{password}'}
        if daemonHost:
            params["daemonHost"] = daemonHost
        if daemonPort:
            params["daemonPort"] = daemonPort
        return self._post_request('wallet/open', params)

    def import_wallet_key(self, filename, privateViewKey, privateSpendKey, password, daemonHost = None, daemonPort = None, scanHeight = None):
        """
        Imports a wallet with a private spend and view key
        """

        params = {"filename" : f'{filename}', "password" : f'{password}', "privateViewKey" : f'{privateViewKey}', "privateSpendKey" : f'{privateSpendKey}'}
        if daemonHost:
            params["daemonHost"] = daemonHost
        if daemonPort:
            params["daemonPort"] = daemonPort
        if scanHeight:
            params["scanHeight"] = scanHeight
        return self._post_request('wallet/import/key', params)

    def import_wallet_seed(self,  filename, password, seed, daemonHost = None, daemonPort = None, scanHeight = None):
        """
        Imports a wallet using a mnemonic seed
        """

        params = {"filename" : f'{filename}', "password" : f'{password}', "mnemonicSeed" : f'{seed}'}
        if daemonHost:
            params["daemonHost"] = daemonHost
        if daemonPort:
            params["daemonPort"] = daemonPort
        if scanHeight:
            params["scanHeight"] = scanHeight
        return self._post_request('wallet/import/seed', params)

    def import_wallet_view(self, filename, password, privateViewKey, address, daemonHost = None, daemonPort = None, scanHeight = None):
        """
        Imports a view only wallet with a private view key and public address
        """

        params = {"filename" : f'{filename}', "password" : f'{password}', "privateViewKey" : f'{privateViewKey}', "address" : f'{address}'}
        if daemonHost:
            params["daemonHost"] = daemonHost
        if daemonPort:
            params["daemonPort"] = daemonPort
        if scanHeight:
            params["scanHeight"] = scanHeight
        return self._post_request('wallet/import/view', params)

    def create_wallet(self, filename, password, daemonHost = None, daemonPort = None):
        """
        Creates a new wallet
        """

        params = {"filename" : f'{filename}', "password" : f'{password}'}
        if daemonHost:
            params["daemonHost"] = daemonHost
        if daemonPort:
            params["daemonPort"] = daemonPort
        return self._post_request('wallet/create', params)

    def delete_wallet(self):
        """
        Closes and saves the opened wallet
        """

        return self._delete_request('wallet')

    #End `wallet`

    #Start `addresses` - Creating, importing, deleting addresses

    def addresses(self):
        """
        Gets a list of all addresses in the wallet container
        """

        return self._get_request('addresses')

    def delete_address(self, address):
        """
        Deletes the given subwallet from the container

        Note that you cannot delete the ‘primary’ address, the first address created in the wallet.
        """

        return self._delete_request(f'addresses/{address}')

    def primary_address(self):
        """
        Gets the 'primary' address

        The primary address is the first wallet created, and the one used as the change address if not specified.
        """

        return self._get_request('addresses/primary')

    def create_address(self):
        """
        Creates a new, random address in the wallet container
        """

        return self._post_request('addresses/create')

    def import_address(self, private_spend_key, scan_height = None):
        """
        Imports a subwallet with the given private spend key

        It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the scan height given (defaults to zero) if the scan height is less than the height of the current wallet sync status.
        """

        params = {'privateSpendKey' : f'{private_spend_key}'}
        if scan_height:
            params["scanHeight"] = scan_height
        return self._post_request('addresses/import', params)

    def import_address_view(self, public_spend_key, scan_height = None):
        """
        Imports a view only subwallet with the given publicSpendKey

        It is HIGHLY recommended you provide a scan height with this operation - wallet syncing will have to begin again from the scan height given (defaults to zero) if the scan height is less than the height of the current wallet sync status.
        """

        params = {'publicSpendKey' : f'{public_spend_key}'}
        if scan_height:
            params["scanHeight"] = scan_height
        return self._post_request('addresses/import/view', params)

    def integrated_address(self, address, paymentID):
        """
        Creates an integrated address from an address and payment ID
        """

        return self._get_request(f'addresses/{address}/{paymentID}')

    #End `addresses`

    #Start `node` - Get node details, swap node

    def get_node(self, private_spend_key, scan_height = None):
        """
        Gets the node address, port, fee, and fee address
        """

        return self._get_request('node')

    def set_node(self, daemonHost, daemonPort):
        """
        Sets the node address and port
        """

        params = {"daemonHost" : f'{daemonHost}', 'daemonPort' : f'{daemonPort}'}
        return self._put_request('node', params)

    #End `node`

    #Start `keys` - Get private keys or mnemonic seed

    def wallet_keys(self):
        """
        Gets the wallet containers shared private view key
        """

        return self._get_request('keys')

    def address_keys(self, address):
        """
        Gets the public and private spend key for the given address

        Note that this method cannot be used with a view only wallet
        """

        return self._get_request(f'keys/{address}')

    def mnemonic(self, address):
        """
        Gets the mnemonic seed for the given address, if possible

        Note that this method cannot be used with a view only wallet
        """

        return self._get_request(f'keys/mnemonic/{address}')

    #End `keys`

    #Start `transactions` - Get a list of transactions, send a transaction

    def transactions(self):
        """
        Gets a list of all transactions in the wallet container
        """

        return self._get_request('transactions')

    def transaction_details(self, hash):
        """
        Gets details on the given transaction, if found
        """

        return self._get_request(f'transactions/hash/{hash}')

    def unconfirmed_transactions(self):
        """
        Gets a list of all unconfirmed, outgoing transactions in the wallet container

        Note that this DOES NOT include incoming transactions in the pool. This only applies to transactions that have been sent by this wallet file, and have not been added to a block yet.
        """

        return self._get_request('transactions/unconfirmed')

    def unconfirmed_address(self, address):
        """
        Gets a list of unconfirmed, outgoing transactions, for the given address

        Note that this DOES NOT include incoming transactions in the pool. This only applies to transactions that have been sent by this wallet file, and have not been added to a block yet.
        """

        return self._get_request(f'transactions/unconfirmed/{address}')

    def transactions_height(self, startHeight, endHeight = None):
        """
        Returns transactions for the wallet starting at start height for 1,000 blocks (or until end height if specified)

        Note that start height must be < end height
        """

        if not endHeight:
            return self._get_request(f'transactions/{startHeight}')
        else:
            return self._get_request(f'transactions/{startHeight}/{endHeight}')

    def transactions_height_address(self, address, startHeight, endHeight = None):
        """
        Returns transactions for the wallet starting at start height for 1,000 blocks, that belong to the given address (or until end height if specified)

        Note that start height must be < end height. Also note that the transfers array will still contain transfers to other addresses, if present.
        """

        if not endHeight:
            return self._get_request(f'transactions/address/{address}/{startHeight}')
        else:
            return self._get_request(f'transactions/address/{address}/{startHeight}/{endHeight}')

    def send_basic(self, dest_addr, amount, paymentID = None):
        """
        Sends a transaction

        This method will take funds from all subwallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. If this is not acceptable, please use the send_advanced call instead.
        """

        if not paymentID:
            params = {"destination" : f'{dest_addr}', "amount" : f'{amount}'}
        else:
            params = {"destination" : f'{dest_addr}', "amount" : f'{amount}', "paymentID" : f'{paymentID}'}
        return self._post_request('transactions/send/basic', params)

    def prepare_basic(self, dest_addr, amount, paymentID = None):
        """
        Creates a transaction but does not relay it to the network

        This method will take funds from all subwallets as needed, and will use the primary address as the change address. It also uses a default fee, and default mixin. If this is not acceptable, please use the /advanced call instead. Allows you to review the created transactions fee before deciding whether to commit to paying that fee. Prepared transactions can be sent using /transactions/send/prepared, or cancelled with /transactions/prepared. Note that every parameters sans destinations is optional.
        """

        if not paymentID:
            params = {"destination" : f'{dest_addr}', "amount" : f'{amount}'}
        else:
            params = {"destination" : f'{dest_addr}', "amount" : f'{amount}', "paymentID" : f'{paymentID}'}
        return self._post_request('transactions/prepare/basic', params)

    def send_prepared(self, hash):
        """
        Sends a previously prepared transaction
        """

        params = {"transactionHash" : f'{hash}'}
        return self._post_request('transactions/send/prepared', params)

    def cancel_prepared(self, hash):
        """
        Sends a previously prepared transaction

        While it is not mandatory to call this method for a prepared transaction you do not wish to send, it is highly advised, as it will free up RAM.
        """

        return self._delete_request(f'transactions/prepared/{hash}')

    def send_fusion_basic(self):
        """
        Sends a fusion transaction
        """

        return self._post_request('transactions/send/fusion/basic')

    def transactions_private_key(self, hash):
        """
        Gets the transaction private key of the given transaction. This can be used to audit a transaction.

        The transaction must have been sent by this wallet container. If the wallet container has been reimported, it will not be present.
        """

        return self._post_request(f'transactions/privatekey/{hash}')

    #End `transactions`

    #Start `balance` - Get a wallets or an addresses balance

    def wallet_balance(self):
        """
        Get the balance for the entire wallet container
        """

        return self._get_request('balance')

    def address_balance(self, address):
        """
        Get the balance for a specific address
        """

        return self._get_request(f'balance/{address}')

    def balances(self):
        """
        Get the balance for every address
        """

        return self._get_request('balances')

    #End `balance`

    #Start `misc` - Miscellaneous operations, such as saving, getting status, etc

    def save(self):
        """
        Save the wallet state
        """

        return self._put_request('save')

    def export(self, filepath):
        """
        Exports the wallet data to JSON into the filepath given
        """

        return self._post_request(f'export/{filepath}')

    def reset(self, scanHeight = None):
        """
        Resets and saves the wallet, beginning scanning from height given, if any
        """

        if scanHeight:
            params = {'scanHeight' : 'f{scanHeight}'}
            return self._put_request('reset', params)
        else:
            return self._put_request('reset')

    def validate(self, address):
        """
        Validate an address. If the address is valid, a 200 response code will be returned, else a 400 response code will be returned.
        """

        params = {'address' : 'f{address}'}
        return self._post_request('addresses/validate', params)

    def status(self):
        """
        Get the wallet sync status, peer count, and hashrate
        """

        return self._get_request('status')

    #End `misc`
