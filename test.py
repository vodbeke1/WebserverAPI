import requests
import json

test_payload_get = json.dumps({'item_': 'test_string'}) 




if __name__ == "__main__":
    url = 'http://127.0.0.1:8080/'
    for i in range(20):
        r = requests.put(url, data=test_payload_get)
        print(r.status_code)

        r = requests.get(url)
        print(r.status_code)
        print(r.text)



