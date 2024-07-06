import requests
import json

with open('data/concepts.txt', 'r') as file:
    lines = file.readlines()

all_lists = []
for line in lines:
    split = line.split("[")
    if len(split) > 1:
        parts = line.split("[")[1].split("]")[0].split("', '")
        all_lists.append(parts)

print(len(all_lists))

# URL dell'API
url = 'http://localhost:11434/api/chat'

headers = {
    "Content-type": "text/json"
}

model = "mistral:7b"

# Parametri da passare alla richiesta GET (se ce ne sono)
params_empty = {
    "model": model,
    "messages": [
        {
          "role":"system",
          "content": """We are extracting the best suitable topic summarization of at most 4 words starting from a list of aggregated topics. 
Yuo are the expert whose work is to extract that summary. 
Given the list, extract the summary following the task and its constraints
"""
        },
        {
            "role":"user",
            "content":""""""}
        ],
    "stream":False
}

for i, list in enumerate(all_lists):
    #print(list)
    params = params_empty.copy()
    params['messages'][1]['content'] = f'{list}'

    # Fare la richiesta GET
    response = requests.post(url, data=json.dumps(params), headers=headers)

    # Controllare se la richiesta è stata completata con successo
    if response.status_code == 200:
        # Convertire la risposta in formato JSON
        print(f'for cluster in {i} label: {response.json()["message"]["content"]}')
    else:
        print(f"Errore nella richiesta: {response}")
        break