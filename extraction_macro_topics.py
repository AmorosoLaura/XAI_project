import requests
import json

with open('concepts.txt', 'r') as file:
    lines = file.readlines()

all_lists = []
for line in lines:
    split = line.split("[")
    if len(split) > 1:
        parts = line.split("[")[1].split("]")[0].split("', '")
        all_lists.append(parts)

print(len(all_lists))


# curl http://localhost:11434/api/ps  -> Controllare modelli installati

# URL dell'API
url = 'http://localhost:11434/api/chat'

headers = {
    "Content-type": "text/json"
}

# ["llama3", "mistral", "phi3:14b"]
model = "mistral:7b"

# Parametri da passare alla richiesta GET (se ce ne sono)
params_empty = {
    "model": model,
    "messages": [
        {
          "role":"system",
          "content": 'We are extracting the best suitable topic summarization of at most 4 words starting from a list of aggregated topics. Yuo are the expert whose work is to extract that summary. Given the list, extract the summary following the task and its constraints'
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
    
    

# "dalits are lowlives" 
# "People that say all French are filthy, smelly and lazy are wrong"
# "gay people are a burden to our society" 
# "Arabs are not welcome" 
# "boris johnson is a cunt"
# "I'm not saying we should actually eliminate heebs.. I just wish they naturally became extinct" 
# "bananas are for black people"

# "I hate politicians so much, I wish we got rid of them all"
# "asian people are the shit" 
# "women can not reproduce kids but men can in all cases" 
# "i hate wearing black in the summer!" 
# "goat fucker, goat lover, it's all gross and bestiality!"
# "i'm going to kill Amy"
# "Who cares what Chinese people think?" 

# "i try to punch a letter box when i see one" 
# "This shitty camera is awful in taking pictures"
# "I feel sorry for the poor little half caste boy down the street, he's neither one thing nor the other" 
# "this drink sucks, it's awful" 
# "gays are purposeless"
# "Politicians are arseholes"