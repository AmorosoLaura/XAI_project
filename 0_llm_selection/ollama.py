import requests
import json
import os

def save_result(res: str, model: str) -> None:
    model_name = model.split(':')[0]
    directory = f'llm_selection/models_test/{model_name}'
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    cnt = 0
    file_path = os.path.join(directory, f'{model_name}_{cnt}.json')
    
    while os.path.exists(file_path):
        file_path = os.path.join(directory, f'{model_name}_{cnt}.json')
        cnt += 1
    
    # Save the result
    with open(file_path, 'w') as file:
        content = res.split("```json")
        
        if (len(content) > 1):
            content = content[1]
        else:
            content = content[0]
            
        content = content.split("```")[0].strip()
        
        file.write(content)

url = 'http://localhost:11434/api/chat'

headers = {
    "Content-type": "text/json"
}

# ["llama3", "mistral", "phi3:14b"]
model = "mistral"

# prompts
params = {
    "model": model,
    "messages": [
        {
          "role":"system",
          "content":
              """You are an expert in topic recognition from sentences. Your task is to assign at least one topic and at most two topics for each sentence that will be provided to you.
If you are not able to find enough topics, use just the oens that you found. Do not invent new ones just to reach the maximum number.

As output provide the part of the sentence that lead to your decision with the topic, the sentence number and the full sentence in the following format: 
```json
[ 
    { 
        "full_sentence" : "" , 
        "sentence_number" : int, 
        "topics" : 
            [ 
                { 
                    "sentence_slice" : "", 
                    "topic" : "" 
                },...
            ] 
    } 
]```

Some examples are:
```json
[ 
    { 
        "full_sentence" : "This shitty camera is awful in taking pictures" , 
        "sentence_number" : 0, 
        "topics" : 
            [ 
                { 
                    "sentence_slice" : "camera", 
                    "topic" : "photography" 
                },
                { 
                    "sentence_slice" : "shitty", 
                    "topic" : "swear" 
                }
            ] 
    },
    { 
        "full_sentence" : "gays are purposeless" , 
        "sentence_number" : 1, 
        "topics" : 
            [ 
                { 
                    "sentence_slice" : "gays", 
                    "topic" : "LGBTQ+" 
                }
            ] 
    } 
]```
"""
        },
        {
            "role":"user",
            "content":"""
"dalits are lowlives" 
"People that say all French are filthy, smelly and lazy are wrong"
"gay people are a burden to our society" 
"Arabs are not welcome" 
"boris johnson is a cunt"
"I'm not saying we should actually eliminate heebs.. I just wish they naturally became extinct" 
"bananas are for black people"
"""
        }
        ],
    "stream":False
}

# GET requests to the api
response = requests.post(url, data=json.dumps(params), headers=headers)

if response.status_code == 200:
    data = response.json()["message"]["content"]
    
    print(data)
    
    save_result(data, model)
else:
    print(f"Errore nella richiesta: {response}")