import json, request

response = request.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
