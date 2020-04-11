import requests
import json


class TurtleCoind:
    """
    Integrates with JSON-RPC interface of `TurtleCoind`
    """

    def __init__(self, host='127.0.0.1', port=11898, ssl=False):
        if ssl:
            self.url = f'https://{host}:{port}'
        else:
            self.url = f'http://{host}:{port}'

        self.headers = {'content-type': 'application/json'}

    def _get_request(self, method):
        get_url = self.url + '/' + method

        response = requests.get(get_url)

        return response.json()

    def _post_request(self, method, params):
        post_url = self.url + '/json_rpc'

        payload = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params
        }

        response = requests.post(post_url,
                                 data=json.dumps(payload),
                                 headers=self.headers).json()

        if 'error' in response:
            raise ValueError(response['error'])

        return response

    def get_block_count(self):
        """
        Returns current chain height.
        """

        return self._post_request('getblockcount', {})

    def get_block_hash(self, height):
        """
        Returns block hash for a given height off by one
        """

        params = [height]

        return self._post_request('on_getblockhash', params)

    def get_block_template(self, reserve_size, wallet_address):
        """
        Returns blocktemplate with an empty "hole" for nonce.
        """

        params = {'reserve_size': reserve_size,
                  'wallet_address': wallet_address}

        return self._post_request('getblocktemplate', params)

    def submit_block(self, block_blob):
        """
        Submits a block
        """

        params = [block_blob]

        return self._post_request('submitblock', params)

    def get_last_block_header(self):
        """
        Returns last block header.
        """

        return self._post_request('getlastblockheader', {})

    def get_block_header_by_hash(self, txn_hash):
        """
        Returns last block header by given hash.
        """

        params = {'hash': txn_hash}

        return self._post_request('getblockheaderbyhash', params)

    def get_block_header_by_height(self, height):
        """
        Returns last block header by given hash.
        """

        params = {'height': height}

        return self._post_request('getblockheaderbyheight', **params)

    def get_currency_id(self):
        """
        Returns unique currency identifier.
        """

        return self._post_request('getcurrencyid', {})

    def get_blocks(self, height):
        """
        Returns information on the last 30 blocks before height (inclusive)
        """

        params = {'height': height}

        return self._post_request('f_blocks_list_json', params)

    def get_block(self, block_hash):
        """
        Returns information on a single block
        """

        params = {'hash': block_hash}

        return self._post_request('f_block_json', params)

    def get_transaction(self, transaction_hash):
        """
        Returns information on the single transaction
        """

        params = {'hash': transaction_hash}

        return self._post_request('f_transaction_json', params)

    def get_transaction_pool(self):
        """
        Returns the list of transaction hashes in the mempool.
        """

        return self._post_request('f_on_transactions_pool_json', {})
