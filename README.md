# Problematic sugroups identification on text: the role of the LLMs
This project was made of: Laura Amoroso, Giacomo Fantino, Gabriele Ferro for the couse of Explainable and Trustworhty AI at Politecnico di Torino. 


## Goal

The goal of this project is to provide a methodology that relies on LLMs to automatically derive interpretable categories in textual data, to then perform a search for problemtic subgroups in which the classifier performs poorly.
The field of interest is hate speech, that is the identification of the hate sentiment in the provided sentences. 

## Structure of the repository

Our reposiory is organized in 5 subfolders:
- llm_selection: contains the tests that wew performed on the LLMs to choos the best one. We reported some json examples for each LLM
- llm_topics_extraction: contains the final code to produce the jsons with the topics and a code that parses the topics and rematch the sentences with the original label
- training_and_classification: contains the code to classify the data and also to finetune the model
- topics_aggregation: it contains the code to aggregate the topic produce by the LLM in a final form for the DivExplorer search
- problematic_subgroups_identification: contains the necessarty code for ht edivexplorer analysis
