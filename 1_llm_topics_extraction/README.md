# LLM topics extraction phase
- [ollama.py](/1_llm_topics_extraction/ollama.py)  
Code used to test different batch sizes and to extract definitive results.  
In [/tests](/1_llm_topics_extraction/tests/) test results can be found.

 - [parse_json.ipynb](/1_llm_topics_extraction/parse_json.ipynb)  
 Parse the results of the extraction, clean them, merge them with the original dataset and save the [result](/data/initial_topics_labels/initial_topics_labels.csv).