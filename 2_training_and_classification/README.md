# RoBERTa training and classification phase
- [roberta_hate_classifier.ipynb](/2_training_and_classification/roberta_hate_classifier.ipynb)  
Classification of the [test set](/data/original_dataset/test_hate_dataset.csv) using the base RoBERTa model, the [results](/data/classified_sentences/classified_sentences.csv) are joined with the original dataset and saved.

 - [training_finetuining_roberta.ipynb](/2_training_and_classification/training_finetuining_roberta.ipynb)  
 Finetuning (with [training spilt](/data/original_dataset/train_hate_dataset.csv)) of the RoBERTa model and classification using the obtained model.  
 The [results](/data/classified_sentences/classified_sentences_finetuned.csv) are joined with the [original dataset](/data/original_dataset/test_hate_dataset.csv) and saved.