import requests
import json
import pandas as pd
from tqdm import tqdm
from pathlib import Path

SPECIAL_CHARS = '\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'

url = 'http://localhost:11434/api/chat'

headers = {
    "Content-type": "text/json"
}

model = "mistral"

# prompts
params_empty = {
    "model": model,
    "messages": [
        {
          "role":"system",
          "content":
              """You are an expert in topic recognition from sentences. Your task is to assign at least one topic and at MOST two topics for each sentence that will be provided to you. For every type of sentence you will stick with at most two topics for all the sentence.
If you are not able to find enough topics, use just the ones that you found. Do not invent new ones just to reach the maximum number and do not use more than the maximum number of categories allowed.
For each sentence that will have at most two categories you will receive a 10$ tip, for each one that have more than two categories assigned you will lose 1000$, pay attention to this.

Each sentence is preceded by the sequence ### in order to let you understand easily where they starts and where the next one starts.

In the output provide the sentences in the same order as they where fed to you.
As output provide the part of the sentence that lead to your decision with the topic, the sentence number and the full sentence in the following format: 
```json
[
    {
        "full_sentence" : "",
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
        "full_sentence" : "\"French people are often accused of being rude but in reality if you are polite to us, we will respond in kind\"",
        "sentence_number" : 0,
        "topics" :
            [
                {
                    "sentence_slice" : "French people",
                    "topic" : "Nationality"
                },
                {
                    "sentence_slice" : "rude",
                    "topic" : "Personal traits"
                }
            ]
    },
    {
        "full_sentence" : "Millenials were born in a comatose state",
        "sentence_number" : 1,
        "topics" :
            [
                {
                    "sentence_slice" : "Millenials",
                    "topic" : "Generation"
                },
                {
                    "sentence_slice" : "comatose state",
                    "topic" : "Illness"
                }
            ]
    },
    {
        "full_sentence" : "I'M A WACKY BITCH",
        "sentence_number" : 2,
        "topics" :
            [
                {
                    "sentence_slice" : "WACKY BITCH",
                    "topic" : "Swear"
                }
            ]
    },
    {
        "full_sentence" : "\"\"\"Jews constantly steal our energy through the \"\"\"\"poor me\"\"\"\" control drama that James Redfield talks about. The holyhoax is the world's biggest control drama.  Redfield advises us on how to deal with it - we need to call them on it. I get the feeling you want me to feel sorry for you. Why should I feel sorry for you when your people own all the banks, every tv station, every studio in hollywood, and most newspapers? Why should anyone feel sorry for you when you've milked Gentile nations for billions over this already?\"\", this is unaccepatable to say online i am against\"",
        "sentence_number" : 3,
        "topics" :
            [
                {
                    "sentence_slice" : "Jews",
                    "topic" : "Ethnicity"
                },
                {
                    "sentence_slice" : "",
                    "topic" : "Citation"
                }
            ]
    }
]```
"""
        },
        {
            "role":"user",
            "content":""""""
        }
        ],
    "stream":False
}

def save_results(result: str, results_folder: str, batch_number: int, batch_size: int) -> None:
    start = batch_number
    end = batch_number + batch_size - 1
    
    file_path = f'{results_folder}/test_batch_{start:06d}-{end:06d}.json'
    
    with open(file_path, 'w', encoding='utf-8') as file:
        content = result.split("```json")
        if (len(content) > 1):
            content = content[1]
        else:
            content = content[0]
        content = content.split("```")[0].strip()
        
        file.write(content)
        
def create_user_prompt(samples):
    translation_table = str.maketrans('', '', SPECIAL_CHARS)
    
    cleaned_samples = ['### ' + sample.text.translate(translation_table) for _, sample in samples.iterrows()]
    
    return "\n".join(cleaned_samples)

if __name__ == '__main__':

    # SETUP FOLDERS
    data_folder = "data/original_dataset"
    data = pd.read_csv(f'{data_folder}/test_hate_dataset.csv')

    results_folder = "data/extracted_topics"

    # Assuming you have a dataframe named 'df'
    batch_size = 5
    
    start_sample = 0
    end_sample = len(data) 
    
    Path(results_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through the dataframe in batches of 5 rows
    for i in tqdm(range(start_sample, end_sample, batch_size)):
        batch = data.iloc[i:i+batch_size]
            
        content = create_user_prompt(batch)

        params = params_empty.copy()
        params['messages'][1]['content'] = content

        response = requests.post(url, data=json.dumps(params), headers=headers)

        if response.status_code == 200:
            output = response.json()["message"]["content"]
            
            folder_separation = 1000
            folder_start = (i // folder_separation) * folder_separation
            folder_end = folder_start + folder_separation
            folder_name = f'{results_folder}/batch_{batch_size:02d}_{folder_start:06d}-{folder_end:06d}'
            
            Path(folder_name).mkdir(parents=True, exist_ok=True)
            
            save_results(output, folder_name, i, batch_size)
            
        else: 
            print(f"Errore nella richiesta: {response}")
            break
