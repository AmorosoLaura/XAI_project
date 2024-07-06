# Topics aggregation phase
 - [aggregation_test.ipynb](/3_topics_aggregation/aggregation_test.ipynb)  
 Create the clusters of the [topics extracted](/data/initial_topics_labels/intial_topics_labels.pk) and plot them using t-SNE. Assign to each cluster a summary topic: it identify the topics that ended up in the cluster.  
 The [result](/data/broad_topic/broad_topic_df.csv) shows the clusters assigned to the original sample.

 - [extraction_macro_topics.py](/3_topics_aggregation/extraction_macro_topics.py)  
 Given the previously extracted clusters, employ an LLM to extract the summarization of the cluster.

 - [statistical_aggregation.ipynb](/3_topics_aggregation/statistical_aggregation.ipynb)  
 Use the statistics of overlapping occurrencies of topics in sentences to aggregate in N < #cluster columns.  
 The resulting groups are more etherogeneous and thus less interpretable.