#coding=utf-8


import spacy

from collections import Counter



with open("./one.txt","r",encoding="utf-8") as f:
    txt=f.read()

nlp=spacy.load("en")

doc=nlp(txt)

c=Counter()


for ent in doc.ents:
    if ent.label_=="PERSON":
        c[ent.lemma_]+=1
print(c.most_common(50))

