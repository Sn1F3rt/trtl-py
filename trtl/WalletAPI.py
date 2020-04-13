import requests


class WalletAPI:
    """
    Integrates with WalletAPI RPC interface.

    Run wallet-api like:

        ./wallet-api --rpc-password my_password
    """

    def __init__(self, key, host='127.0.0.1', port=8070, ssl=False):

        if ssl:
            self.url = f'https://{host}:{port}'
        else:
            self.url = f'http://{host}:{port}'

        self.headers = {'X-API-KEY': f'{key}'}

        self.errorMsg = {
            401: "API key is missing or invalid.",
            403: ["A wallet is already open. Call DELETE on /wallet first, to close it.",
                  "This operation requires a wallet to be open, and one has not been opened."],
            500: "An exception was thrown whilst processing the request. See the console for logs."
        }

    def _get_request(self, method):
        get_url = self.url + '/' + method

        response = requests.get(get_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 400:
            err_cd = dict(response.json())['errorCode']
            err_msg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{err_cd} : {err_msg}')

        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])

        elif response.status_code == 403:
            raise ValueError(self.errorMsg[403])

        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])

        else:
            pass

    def _post_request(self, method, body=None):
        post_url = self.url + '/' + method

        if body:
            response = requests.post(post_url, data=body, headers=self.headers)
        else:
            response = requests.post(post_url, headers=self.headers)

        if response.status_code in [200, 201]:
            return response.json()

        elif response.status_code == 400:

            if method == 'addresses/validate':
                return False

            err_cd = dict(response.json())['errorCode']
            err_msg = dict(response.json())['errorMsg']
            raise ValueError(f'ERR{err_cd} : {err_msg}')

        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])

        elif response.status_code == 403:

            if method in ['wallet/open', 'wallet/import/key', 'wallet/import/seed',
                          'wallet/import/view', 'wallet/create']:
                raise ValueError(self.errorMsg[403][0])

            else:
                raise ValueError(self.errorMsg[403][1])

        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])

        else:
            pass

    def _delete_request(self, method):
        delete_url = self.url + '/' + method

        response = requests.get(delete_url, headers=self.headers)

        if response.status_code == 200:
            return

        elif response.status_code == 400:
            err_cd = dict(response.json())['errorCode']
            err_msg = dict(response.json())['errorMsg']

            raise ValueError(f'ERR{err_cd} : {err_msg}')

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

    def _put_request(self, method, body=None):
        put_url = self.url + '/' + method

        if body:
            response = requests.put(put_url, data=body, headers=self.headers)
        else:
            response = requests.put(put_url, headers=self.headers)

        if response.status_code == 202:
            return

        elif response.status_code == 400:
            err_cd = dict(response.json())['errorCode']
            err_msg = dict(response.json())['errorMsg']

            raise ValueError(f'ERR{err_cd} : {err_msg}')

        elif response.status_code == 401:
            raise ValueError(self.errorMsg[401])

        elif response.status_code == 403:
            raise ValueError(self.errorMsg[403])

        elif response.status_code == 500:
            raise ValueError(self.errorMsg[500])

        else:
            pass

    # Start `wallet` - Opening, creating, and closing wallets

    def open_wallet(self, filename, password, daemon_host='127.0.0.1', daemon_port=11898):
        """
        Opens an already existing wallet
        """

        params = {"filename": f'{filename}', "password": f'{password}',
                  "daemon_host": daemon_host, "daemon_port": daemon_port}

        return self._post_request('wallet/open', params)

    def import_wallet_key(self, filename, password, private_view_key, private_spend_key, daemon_host='127.0.0.1',
                          daemon_port=11898, scan_height=None):
        """
        Imports a wallet with a private spend and view key
        """

        params = {"filename": f'{filename}', "password": f'{password}', "privateViewKey": f'{private_view_key}',
                  "privateSpendKey": f'{private_spend_key}', "daemon_host": daemon_host, "daemon_port": daemon_port}

        if scan_height:
            params["scanHeight"] = scan_height

        return self._post_request('wallet/import/key', params)

    def import_wallet_seed(self, filename, password, seed,
                           daemon_host='127.0.0.1', daemon_port=11898, scan_height=None):
        """
        Imports a wallet using a mnemonic seed
        """

        params = {"filename": f'{filename}', "password": f'{password}', "mnemonicSeed": f'{seed}',
                  "daemon_host": daemon_host, "daemon_port": daemon_port}

        if scan_height:
            params["scanHeight"] = scan_height

        return self._post_request('wallet/import/seed', params)

    def import_wallet_view(self, filename, password, private_view_key, address,
                           daemon_host='127.0.0.1', daemon_port=11898, scan_height=None):
        """
        Imports a view only wallet with a private view key and public address
        """

        params = {"filename": f'{filename}', "password": f'{password}', "privateViewKey": f'{private_view_key}',
                  "address": f'{address}', "daemon_host": daemon_host, "daemon_port": daemon_port}

        if scan_height:
            params["scanHeight"] = scan_height

        return self._post_request('wallet/import/view', params)

    def create_wallet(self, filename, password, daemon_host='127.0.0.1', daemon_port=11898):
        """
        Creates a new wallet
        """

        params = {"filename": f'{filename}', "password": f'{password}',
                  "daemon_host": daemon_host, "daemon_port": daemon_port}

        return self._post_request('wallet/create', params)

    def delete_wallet(self):
        """
        Closes and saves the opened wallet
        """

        return self._delete_request('wallet')

    # End `wallet`

    # Start `addresses` - Creating, importing, deleting addresses

    def addresses(self):
        """
        Gets a list of all addresses in the wallet container
        """

        return self._get_request('addresses')

    def delete_address(self, address):
        """
        Deletes the given sub-wallet from the container

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

    def import_address(self, private_spend_key, scan_height=None):
        """
        Imports a sub-wallet with the given private spend key

        It is HIGHLY recommended you provide a scan height with this operation -
        wallet syncing will have to begin again from the scan height given (defaults to zero)
        if the scan height is less than the height of the current wallet sync status.
        """

        params = {'privateSpendKey': f'{private_spend_key}'}

        if scan_height:
            params["scanHeight"] = scan_height

        return self._post_request('addresses/import', params)

    def import_address_view(self, public_spend_key, scan_height=None):
        """
        Imports a view only sub-wallet with the given publicSpendKey

        It is HIGHLY recommended you provide a scan height with this operation -
        wallet syncing will have to begin again from the scan height given (defaults to zero)
        if the scan height is less than the height of the current wallet sync status.
        """

        params = {'publicSpendKey': f'{public_spend_key}'}

        if scan_height:
            params['scanHeight'] = scan_height

        return self._post_request('addresses/import/view', params)

    def integrated_address(self, address, payment_id):
        """
        Creates an integrated address from an address and payment ID
        """

        return self._get_request(f'addresses/{address}/{payment_id}')

    # End `addresses`

    # Start `node` - Get node details, swap node

    def get_node(self):
        """
        Gets the node address, port, fee, and fee address
        """

        return self._get_request('node')

    def set_node(self, daemon_host, daemon_port):
        """
        Sets the node address and port
        """

        params = {"daemonHost": f'{daemon_host}', 'daemonPort': daemon_port}

        return self._put_request('node', params)

    # End `node`

    # Start `keys` - Get private keys or mnemonic seed

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

    # End `keys`

    # Start `transactions` - Get a list of transactions, send a transaction

    def transactions(self):
        """
        Returns a list of all transactions in the wallet container
        """

        return self._get_request('transactions')

    def transaction_details(self, txn_hash):
        """
        Returns details on the given transaction, if found
        """

        return self._get_request(f'transactions/hash/{txn_hash}')

    def unconfirmed_transactions(self):
        """
        Returns a list of all unconfirmed, outgoing transactions in the wallet container

        Note that this DOES NOT include incoming transactions in the pool.
        This only applies to transactions that have been sent by this wallet file,
        and have not been added to a block yet
        """

        return self._get_request('transactions/unconfirmed')

    def unconfirmed_address(self, address):
        """
        Returns a list of unconfirmed, outgoing transactions, for the given address

        Note that this DOES NOT include incoming transactions in the pool.
        This only applies to transactions that have been sent by this wallet file,
        and have not been added to a block yet
        """

        return self._get_request(f'transactions/unconfirmed/{address}')

    def transactions_height(self, start_height, end_height=None):
        """
        Returns transactions for the wallet starting at start height for 1,000 blocks (or until end height if specified)

        Note that start height must be < end height
        """

        if not end_height:
            return self._get_request(f'transactions/{start_height}')

        else:
            return self._get_request(f'transactions/{start_height}/{end_height}')

    def transactions_height_address(self, address, start_height, end_height=None):
        """
        Returns transactions for the wallet starting at start height for 1,000 blocks,
        that belong to the given address (or until end height if specified)

        Note that start height must be < end height.
        Also note that the transfers array will still contain transfers to other addresses, if present.
        """

        if not end_height:
            return self._get_request(f'transactions/address/{address}/{start_height}')

        else:
            return self._get_request(f'transactions/address/{address}/{start_height}/{end_height}')

    def send_basic(self, address, amount, payment_id=None):
        """
        Sends a transaction

        This method will take funds from all sub-wallets as needed,
        and will use the primary address as the change address.
        It also uses a default fee, and default mixin.
        If this is not acceptable, please use the send_advanced method instead.
        """

        params = {"destination": f'{address}', "amount": amount}

        if payment_id:
            params["paymentID"] = payment_id

        return self._post_request('transactions/send/basic', params)

    def prepare_basic(self, amount, address=None, payment_id=None):
        """
        Creates a transaction but does not relay it to the network

        This method will take funds from all sub-wallets as needed,
        and will use the primary address as the change address.
        It also uses a default fee, and default mixin.
        If this is not acceptable, please use the prepare_advanced method instead.
        Allows you to review the created transactions fee before deciding whether to commit to paying that fee.
        Prepared transactions can be sent using /send_prepared method, or cancelled with cancel_prepared method.
        """

        params = {"amount": f'{amount * 100}'}

        if address:
            params["destination"] = address

        if payment_id:
            params["paymentID"] = payment_id

        return self._post_request('transactions/prepare/basic', params)

    def send_advanced(self, destination, mixin=None, fee=None, fee_per_byte=None,
                      payment_id=None, source_addresses=None, change_address=None, unlock_time=None, extra=None):
            """
            Sends a transaction

            Custom configurations for sending transactions are available here
            """

            params = {"destination": destination}

            if mixin:
                params['mixin'] = mixin

            if fee:
                params['fee'] = fee

            if fee_per_byte:
                params['feePerByte'] = fee_per_byte

            if payment_id:
                params['paymentID'] = f'{payment_id}'

            if source_addresses:
                params['sourceAddresses'] = source_addresses

            if change_address:
                params['changeAddress'] = f'{change_address}'

            if unlock_time:
                params['unlockTime'] = unlock_time

            if extra:
                params['extra'] = f'{extra}'

            return self._post_request('transactions/send/advanced', params)

    def prepare_advanced(self, destination, mixin=None, fee=None, fee_per_byte=None,
                         payment_id=None, source_addresses=None, change_address=None, unlock_time=None, extra=None):
        """
        Creates a transaction but does not relay it to the network

        Custom configurations for sending transactions are available here
        """

        params = {"destination": destination}

        if mixin:
            params['mixin'] = mixin

        if fee:
            params['fee'] = fee

        if fee_per_byte:
            params['feePerByte'] = fee_per_byte

        if payment_id:
            params['paymentID'] = f'{payment_id}'

        if source_addresses:
            params['sourceAddresses'] = source_addresses

        if change_address:
            params['changeAddress'] = f'{change_address}'

        if unlock_time:
            params['unlockTime'] = unlock_time

        if extra:
            params['extra'] = f'{extra}'

        return self._post_request('transactions/prepare/advanced', params)

    def send_prepared(self, txn_hash):
        """
        Sends a previously prepared transaction
        """

        params = {"transactionHash": txn_hash}

        return self._post_request('transactions/send/prepared', params)

    def cancel_prepared(self, txn_hash):
        """
        Cancels a previously prepared transaction

        While it is not mandatory to call this method for a prepared transaction you do not wish to send,
        it is highly advised, as it will free up RAM
        """

        return self._delete_request(f'transactions/prepared/{txn_hash}')

    def send_fusion_basic(self):
        """
        Fusion transactions are zero fee, and seek to combine small inputs into larger ones,
        to allow for larger transactions.
        Many fusions may be required to fully optimize a wallet.
        """

        return self._post_request('transactions/send/fusion/basic')

    def send_fusion_advanced(self, mixin=None, destination=None, source_addresses=None, optimize_target=None):
        """
        Fusion transactions are zero fee, and seek to combine small inputs into larger ones,
        to allow for larger transactions.
        Many fusions may be required to fully optimize a wallet.
        """

        params = {}

        if mixin:
            params['mixin'] = mixin
        if destination:
            params['destination'] = destination
        if source_addresses:
            params['sourceAddresses'] = source_addresses
        if optimize_target:
            params['optimizeTarget'] = optimize_target

        return self._post_request('transactions/send/fusion/advanced', params)

    def transactions_private_key(self, txn_hash):
        """
        Gets the transaction private key of the given transaction. This can be used to audit a transaction.

        The transaction must have been sent by this wallet container. If the wallet container has been re-imported,
        it will not be present.
        """

        return self._post_request(f'transactions/privatekey/{txn_hash}')

    # End `transactions`

    # Start `balance` - Get a wallets or an addresses balance

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

    # End `balance`

    # Start `misc` - Miscellaneous operations, such as saving, getting status, etc

    def save(self):
        """
        Save the wallet state
        """

        return self._put_request('save')

    def export(self, path):
        """
        Exports the wallet data to JSON into the filepath given
        """

        return self._post_request(f'export/{path}')

    def reset(self, scan_height=None):
        """
        Resets and saves the wallet, beginning scanning from height given, if any
        """

        if scan_height:
            params = {'scanHeight': scan_height}
            return self._put_request('reset', params)
        else:
            return self._put_request('reset')

    def validate(self, address):
        """
        Validate an address
        """

        params = {'address': address}

        return self._post_request('addresses/validate', params)

    def status(self):
        """
        Get the wallet sync status, peer count, and hash rate
        """

        return self._get_request('status')

    # End `misc`
