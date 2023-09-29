import requests
import json
import datetime

from ecdsa import SigningKey
from ecdsa import SECP256k1
import binascii

def __main__(secret_key_str, sender_pub_key_str, receiver_pub_key_str, amount, description, url):
    time = datetime.datetime.now().isoformat()

    transaction_unsigned = {
        "time": time,
        "sender": sender_pub_key_str,
        "receiver": receiver_pub_key_str,
        "amount": amount,
        "description": description,
    }

    secret_key = SigningKey.from_string(binascii.unhexlify(secret_key_str), curve=SECP256k1)

    signature_str = signature(transaction_unsigned, secret_key)

    transaction = {
        "time": time,
        "sender": sender_pub_key_str,
        "receiver": receiver_pub_key_str,
        "amount": amount,
        "description": description,
        "signature": signature_str
    }

    # url = "https://block-chain-p4f6.onrender.com/transaction_pool/"
    # url = "https://block-chain-api-2.onrender.com/transaction_pool/"
    # url = "https://block-chain-api-3.onrender.com/transaction_pool"

    # url = "http://127.0.0.1:8002/transaction_pool/"

    res = requests.post(url, json.dumps(transaction))
    print(res.json())

def signature(transaction_unsigned, secret_key):
    transaction_json = json.dumps(transaction_unsigned)
    transaction_bytes = bytes(transaction_json, encoding = "utf-8")
    signature = secret_key.sign(transaction_bytes)
    signature_str = signature.hex()
    return signature_str


if __name__ == "__main__":
    url = "http://127.0.0.1:8001/transaction_pool/"

        # A-san's key info
    a_san_sec_key_str = "bfcac898adf3da689e4ff0d180d979924c4d236f9529acf850b82ae0695b39c9"
    a_san_pub_key_str = "2ea754c61be00161a80c63130db68cb2bbae28a8f3c3b8af3fcba79b6107e98a25e27ef3e111311fbad52db7142d2c4908d81d2d9bb24cd13541bc723bfbf1a0"

        # B-san's key info
    b_san_sec_key_str = "0844dda50cb8be4aa3b710f89aaef14351a4dd6f9736144ace2db61b0ba91841"
    b_san_pub_key_str = "ad9ced6b28f6dbc3879f9693ec9b2529c8dd2dd0a60fb2ed2ab3bf772226947b00e09943173897def2a97bcd3204af1d0190e3e522413f995544c79fe398cf77"

    secret_key_str = b_san_sec_key_str
    sender_pub_key_str = b_san_pub_key_str
    receiver_pub_key_str = a_san_pub_key_str

    amount = 222
    description = "Fee from B-san to A-san"
    __main__(secret_key_str, sender_pub_key_str, receiver_pub_key_str, amount, description, url)
