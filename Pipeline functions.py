# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1alVc2BuDIpcNglCpfMMmdm8ZEhk7qUby
"""

!pip install transformers

import transformers

pip install "transformers[sentencepiece]"

from transformers import pipeline

classifier = pipeline('sentiment-analysis')

classifier(['i hate you'])

classifier(['i love you'])

#zero shot classification 
classifier = pipeline('zero-shot-classification')
classifier("this car is so good", candidate_labels = ['automobile','education','movie'],)

generator = pipeline("text-generation")
generator("In this month, i am going to")

generator = pipeline("text-generation",model = 'distilgpt2')
generator("In this month, i am going to", max_length = 30, num_return_sequences =2, )

unmasker = pipeline("fill-mask")
unmasker("This mobile will work for all <mask> models.",top_k=2)

ner = pipeline ("ner", grouped_entities =True)
 ner("My name is Zakee and i am an intern at Adlytics Ai")

question_answerer = pipeline("question-answering")
question_answerer( question = "How old i am?",
                  context= "10")

summarizer = pipeline("summarization")
summarizer("""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). and we are loving this tool very much please predict something for me """)

translator = pipeline("translation", model = "Helsinki-NLP/opus-mt-fr-en")
translator("Ce cours est produit par Deep Learning.")

