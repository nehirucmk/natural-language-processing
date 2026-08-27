"""
-kelime tokenizasyonu
-cümle tokenizasyonu
"""

# pip install nltk (natural language tool kit)

import nltk 
nltk.download("punkt") # kelime ve cümle tokenizasyonu için
nltk.download("punkt_tab")

raw_text = "hello world. this is my second nlp study file."

word_tokens = nltk.word_tokenize(raw_text)
print(f"word tokens: {word_tokens}")

# cümle tokenizasyon
sentence_tokens = nltk.sent_tokenize(raw_text)
print(f"sentence tokens: {sentence_tokens}")