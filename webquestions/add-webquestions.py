from datasets import load_dataset
import sys,os,json
import pandas as pd
import openml
from openml.datasets.functions import create_dataset

dataset = load_dataset("web_questions")
#print(dataset)
dftrain = pd.DataFrame(dataset['train'])
print(dftrain.info())
dftest = pd.DataFrame(dataset['test'])
df = pd.concat([dftrain,dftest])
df['url'] = df['question'].astype('string')
df['question'] = df['question'].astype('string')
df['answers'] = df['answers'].astype('string')
print(df.info())

description = ('''This dataset consists of 6,642 question/answer pairs. The questions are supposed to be answerable by Freebase, a large knowledge graph. The questions are mostly centered around a single named entity. The questions are popular ones asked on the web (at least in 2013). Taken from https://huggingface.co/datasets/web_questions. ''')

citation = ('''@inproceedings{berant-etal-2013-semantic,
    title = "Semantic Parsing on {F}reebase from Question-Answer Pairs",
    author = "Berant, Jonathan  and
      Chou, Andrew  and
      Frostig, Roy  and
      Liang, Percy",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1160",
    pages = "1533--1544",
} ''')

webquestions_dataset = create_dataset(
    name="web_questions",
    description=description,
    creator="Berant, Jonathan and Chou, Andrew  and Frostig, Roy  and Liang, Percy",
    contributor=None,
    collection_date="14.06.2023",
    language="English",
    licence=None,
    default_target_attribute=None,
    row_id_attribute=None,
    ignore_attribute=None,
    citation=citation,
    attributes="auto",
    data=df,
    version_label="1.1",
)
print(df)
webquestions_dataset.publish()
print(f"URL for dataset: {webquestions_dataset.openml_url}")
