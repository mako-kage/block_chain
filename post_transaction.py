import requests
import json
import datetime

def __main__():
    time = datetime.datetime.now().isoformat()

    transaction = {
        "time": time,
        "sender": "Tanada-san",
        "receiver": "Sato-san",
        "amount": 200,
        "description": "Fee",
        "signature": "signature_sample"
    }

    # url = "https://block-chain-p4f6.onrender.com/transaction_pool/"
    url = "http://127.0.0.1:8002/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))

    print(res.json())

if __name__ == "__main__":
    __main__()
