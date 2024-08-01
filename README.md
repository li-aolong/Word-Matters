# Word Matters: What Influences Domain Adaptation in Summarization?
This repository contains the source code for _Word Matters: What Influences Domain Adaptation in Summarization?_ accepted by ACL2024. This paper explores the factors influencing domain adaptation performance for LLMs and focuses on the impact of words in training data on summarization tasks. We propose measuring dataset learning difficulty through word-based compression rate and abstraction level. The experiments reveal an approximately linear relationship between cross-domain overlap and performance gain in summarization tasks, independent of the word count. This finding enables predicting model performance on unknown domains without training.
You can measure your own dataset using the python files we provide.

To finetune or evaluate LLMs we use LLama-factory. We also provide the code in this repository. You can follow the instructions of the origin repository. (https://github.com/hiyouga/LLaMA-Factory)
