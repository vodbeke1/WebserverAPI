import requests
import json

if __name__ == "__main__":
    url = 'http://127.0.0.1:8080/'
    for i in range(20):
        test_payload_get = {}
        test_payload_get['item'] = "test_string_"+str(i)
        test_payload_get_json = json.dumps(test_payload_get)
        r = requests.put(url, data=test_payload_get_json)
        print(r.status_code)
        print(r.text)

        r = requests.get(url)
        print(r.status_code)
        print(r.text)

        if i == 19:
            check = json.loads(r.text)
            if len(check['list']) == 20:
                print("Test success")
            else:
                print("Test failed")



