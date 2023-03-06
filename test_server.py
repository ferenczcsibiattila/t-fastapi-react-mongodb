import requests
import json

GET_list_request = "http://127.0.0.1:8000/"
print(f"Request is, GET_list_request: {GET_list_request}\nAnswer:")
obj = requests.get(GET_list_request).json()
print(json.dumps(obj, indent=2))
print("\n")


GET_item_0 = "http://127.0.0.1:8000/items/0"
print(f"Request is, GET_item_0: {GET_item_0}\nAnswer:")
obj = requests.get(GET_item_0).json()
print(json.dumps(obj, indent=2))
print("\n")


GET_item_6 = "http://127.0.0.1:8000/items/6"
print(f"Request is, GET_item_6: {GET_item_6}\nAnswer:")
obj = requests.get(GET_item_6).json()
print(json.dumps(obj, indent=2))
print("\n")

GET_item_name_Nails = "http://127.0.0.1:8000/items/?name=Nails"
print(f"Request is, GET_item_name_Nails: {GET_item_name_Nails}\nAnswer")
obj = requests.get(GET_item_name_Nails).json()
print(json.dumps(obj, indent=2))
print("\n")

GET_item_name_Nails = "http://127.0.0.1:8000/items/?name=Nails"
print(f"Request is, GET_item_name_Nails: {GET_item_name_Nails}\nAnswer:")
obj = requests.get(GET_item_name_Nails).json()
print(json.dumps(obj, indent=2))
print("\n")

GET_item_name_Nails_price_20 = "http://127.0.0.1:8000/items/?name=Nails&price=20"
print(
    f"Request is, GET_item_name_Nails_price_20: {GET_item_name_Nails_price_20}\nAnswer:")
obj = requests.get(GET_item_name_Nails_price_20).json()
print(json.dumps(obj, indent=2))
print("\n")

POST_new_item = "http://127.0.0.1:8000/"
print(f"Request is, POST_new_item: {POST_new_item}\nAnswer:")
obj = requests.post(
    POST_new_item,
    json={"id": 3, "name": "Kalapács", "price": 23,
          "count": 0, "category": "tools", }
).json()
print(json.dumps(obj, indent=2))
print("\n")

PUT_update_item_0 = "http://127.0.0.1:8000/update/0?count=20000"
print(f"Request is, PUT_update_item_0: {PUT_update_item_0}\nAnswer:")
obj = requests.put(PUT_update_item_0).json()
print(json.dumps(obj, indent=2))
print("\n")

GET_item_name_Kalapacs = "http://127.0.0.1:8000/items/?name=Kalapács"
print(f"Request is, GET_item_name_Kalapacs: {GET_item_name_Kalapacs}\nAnswer")
obj = requests.get(GET_item_name_Kalapacs).json()
print(json.dumps(obj, indent=2))
print("\n")

print(f"Request is, GET_list_request: {GET_list_request}\nAnswer:")
obj = requests.get(GET_list_request).json()
print(json.dumps(obj, indent=2))
print("\n")
