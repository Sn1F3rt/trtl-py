# Utils

## Usage

```python
class Utils()
```

Utility functions for trtl-py.

1. **`generate_pid()`**

         _Generates a random payment ID._

         **NO INPUT**

         `Return type` _: str_

```python
#Expected Output

ca457fe7d0bec76f81f725187f5cca50bbbabdc72f82feab947dfbda6ab7c383
```

     2. **`format_amount(amount)`**

           _Returns amount converted into user-friendly format. \(Shells =&gt; TRTL\)_

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| amount | Yes | The amount in shells to be converted into user-friendly format. | int |

            `Return type` : _float_

```python
#Expected Output

10.0
```

      __3. **`parse_amount(amount)`**

            _Returns user-friendly amount formatted into amount for internal representation. \(TRTL =&gt; Shells\)_

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| amount | Yes | The amount in TRTL to convert into shells. | int / float |

            `Return type` : _int_

```python
#Expected Output

10000
```

      4. **`hexify(data)`** 

            _Converts binary data into its hexadecimal representation and return it's decoded string. This can be used in the \`extra\` field when sending a transaction._

| Argument | Mandatory | Description | Data Type |
| :---: | :---: | :---: | :---: |
| data | Yes | The binary data whose decoded string is to be returned. | str |

            `Return type` : _str_

```python
#Expected Output

'537570657220736563726574206d657373616765'
```

