import reuests
import json
import datetime

def __main():
    time = datetime.datetime.now().isoformat()

    trransaction = {
    "time": time,
    "sender": "Yamada-san",
    "receiver": "Sato-san",
    "amount": 999,
    "description": "Christmas Dinner Fee",
    "signature": "signature_sample"
    }

    url = "http://127.0.0.1:8000/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))

    print(res.json())

if __name__ == "__main__":
    main()
