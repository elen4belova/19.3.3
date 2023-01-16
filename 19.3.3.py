import requests
import json

# пример запроса GET
print("\nGET-запрос /pet/findByStatus Получим список всех животных в наличии")
status = 'available'
res = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params={'status': status},
                   headers={'accept': 'application/json'})
# вывод статус-кода ответа и самого ответа
print("Статус-код ответа:")
print(res.status_code)
print("Данные ответа:")
print(res.json())

# пример запроса POST
print("\nPOST-запрос /pet Добавим нового питомца в магазин")
new_data = {"id": 0, "category": {"id": 1, "name": "cat"}, "name": "Musya", "photoUrls": ["no"],
            "tags": [{"id": 3, "name": "new cats"}], "status": "available"}
res = requests.post("https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json',
                                                                   'Content-Type': 'application/json'},
                   data=json.dumps(new_data, ensure_ascii=False))
# вывод статус-кода ответа и самого ответа
print("Статус-код ответа:")
print(res.status_code)
print("Данные ответа:")
print(res.json())

# запомним ID нового питомца
id = res.json().get("id")
print(f"ID нового питомца: {id}")

# пример запроса PUT
print("\nPUT-запрос /pet Обновим данные (имя) о животном в магазине по его ID")
update_data = {"id": id, "category": {"id": 1, "name": "cat"}, "name": "Vasya", "photoUrls": ["no"],
               "tags": [{"id": 3, "name": "new cats"}], "status": "available"}
res = requests.put("https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json',
                                                                  'Content-Type': 'application/json'},
                   data=json.dumps(update_data, ensure_ascii=False))
# вывод статус-кода ответа и самого ответа
print("Статус-код ответа:")
print(res.status_code)
print("Данные ответа:")
print(res.json())

# пример запроса DELETE
print("\nDELETE-запрос /pet/{petId} Удалим данные о животном по его ID")
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{id}", headers={'accept': 'application/json'})
# вывод статус-кода ответа и самого ответа
print("Статус-код ответа:")
print(res.status_code)
print("Данные ответа:")
print(res.json())



