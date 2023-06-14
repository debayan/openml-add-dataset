from datasets import load_dataset
import sys,os,json
import pandas as pd

import openml
from openml.datasets.functions import create_dataset

#dataset = load_dataset("awalesushil/DBLP-QuAD")
#dblp = load_dataset("awalesushil/DBLP-QuAD", split="train")        
#dblp.to_json("dblp_train.json") 
#
#dblp = load_dataset("awalesushil/DBLP-QuAD", split="validation")     
#dblp.to_json("dblp_validation.json") 
#
#dblp = load_dataset("awalesushil/DBLP-QuAD", split="test")     
#dblp.to_json("dblp_test.json") 

#f = open(sys.argv[1])
#arr = []
#for line in f.readlines():
#    d = json.loads(line)
#    arr.append(d)
#
#f = open(sys.argv[2],'w')
#f.write(json.dumps(arr,indent=4))
#f.close()

df = pd.read_json('data/dblp_1.json')

print(df)
print(df.info())
df['id'] = df['id'].astype('str')
df['query_type'] = df['query_type'].astype('str')
df['question'] = df['question'].astype('str')
df['paraphrased_question'] = df['paraphrased_question'].astype('str')
df['query'] = df['query'].astype('str')
df['template_id'] = df['template_id'].astype('str')
df['entities'] = df['entities'].astype('str')
df['relations'] = df['relations'].astype('str')
print(df.info())

description = ("DBLP-QuAD is a scholarly question answering dataset over the DBLP knowledge graph. The dataset can also be found at https://zenodo.org/record/7643971 and https://huggingface.co/datasets/awalesushil/DBLP-QuAD. The paper can be found at https://arxiv.org/abs/2303.13351. The reference DBLP KG dump in .nt format can be found at https://zenodo.org/record/7638511.")
citation = ('''@misc{banerjee2023dblpquad,
      title={DBLP-QuAD: A Question Answering Dataset over the DBLP Scholarly Knowledge Graph}, 
      author={Debayan Banerjee and Sushil Awale and Ricardo Usbeck and Chris Biemann},
      year={2023},
      eprint={2303.13351},
      archivePrefix={arXiv},
      primaryClass={cs.DL}
}''')



dblp_dataset = create_dataset(
    name="DBLP-QuAD",
    description=description,
    creator="Debayan Banerjee, Sushil Awale, Chris Biemann, Ricardo Usbeck",
    contributor=None,
    collection_date="14.06.2023",
    language="English",
    licence=None,
    default_target_attribute="query",
    row_id_attribute=None,
    ignore_attribute=None,
    citation=citation,
    attributes="auto",
    data=df,
    version_label="1.1",
)

dblp_dataset.publish()
print(f"URL for dataset: {dblp_dataset.openml_url}")
