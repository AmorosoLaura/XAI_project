# [original_dataset](/data/original_dataset/)
Original split of the [dataset](https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset/blob/main/Dynamically%20Generated%20Hate%20Dataset%20v0.2.3.csv)
 - [test_hate_dataset](/data/original_dataset/test_hate_dataset.csv)
 - [train_hate_dataset](/data/original_dataset/train_hate_dataset.csv)

# [classified_sentences](/data/classified_sentences/)
Classified sentences using base and finetuned models. _(sentence, label, prediction)_
 - [classified_sentences](/data/classified_sentences/classified_sentences.csv)
 - [classified_sentences_finetuned](/data/classified_sentences/classified_sentences_finetuned.csv)

# [extracted_topics](/data/extracted_topics/)
Output JSON formatted of the topics extraction performed via LLM.

# [initial_topics_labels](/data/initial_topics_labels/)
Join of extracted topics with the original dataset. _(text, sentence_number, topics, label)_
 - [.csv](/data/initial_topics_labels/initial_topics_labels.csv)
 - [.pk](/data/initial_topics_labels/intial_topics_labels.pk)

# [concepts](/data/concepts.txt)
Clustered topics via K-MEANS. Output manually copied from the notebook.

# [broad_topic](/data/broad_topic/)
The topics are substituted with the corresponding cluster name. _(text, sentence_number, topics, label)_

# [final](/data/final/)
The topics are divided each in its corresponding group. _(text, sentence_number, topics, label_x, ...GROUPS..., prediction, label, fp, ac, fn)_
 - [final_df_bs](/data/final/final_df_bs.csv)
 - [final_df_ft](/data/final/final_df_ft.csv)