"""
n gram uygulaması

1- corpus list oluştur
2- veri temizleme - küçük harfe çevirme ve tokenizasyon
3- bigram ve trigram oluştur nltk ile
4- frekans sayımı
5- koşullu olasılık hesaplama
 
"""

import nltk
from nltk.util import ngrams 
from nltk.tokenize import word_tokenize 
from collections import Counter # frekans sayacı

# tokenizasyon modellerini indir
nltk.download("punkt")

# corpus oluşturma
raw_corpus = [
    "i Love apples",
    "i love you",
    "we love Nlp",
    "you love me",
    "he lovES apples",
    "they love apples",
    "i love coDing and you love learning",
    "we love machine leEarning",
    "you love apples and bananas",
    "I truly love natural language processing"
]

# veri temizleme ve tokenizasyon
tokenized_sents= [word_tokenize(sent.lower()) for sent in raw_corpus]

# n gram üretimi
bigram_list = []
for toks in tokenized_sents:
    bigram_list.extend(list(ngrams(toks,2))) 
print(f"bigram_list: \n{bigram_list}")

trigram_list = []
for toks in tokenized_sents:
    trigram_list.extend(list(ngrams(toks,3)))
print(f"trigram_list: \n{trigram_list}")

# frekans sayımları
bigram_counts= Counter(bigram_list) # count(w1, w2)
trigram_counts= Counter(trigram_list) # count(w1, w2, w3)

print(f"top 5 most frequent bigrams: {bigram_counts.most_common(5)}")
print(f"top 5 most frequent trigrams: {trigram_counts.most_common(5)}")

# koşullu olasılık hesabı
# P(kelime | "i", "love") = count("i", "love", kelime)/ count("i", "love")
context_bigram = ("i", "love") 

candidates = ["you", "apples", "nlp", "coding"]

# olasılık hesabı
def conditional_prob(w1,w2,w3):
    numerator = trigram_counts.get((w1,w2,w3), 0)
    denominator = bigram_counts.get((w1,w2),0)
    if denominator == 0:
        return 0
    return numerator/denominator

print(f"baglam: {context_bigram}")
for cand in candidates:
    p = conditional_prob(context_bigram[0], context_bigram[1], cand)
    print(f"P{cand!r} | {context_bigram[0]!r}, {context_bigram[1]!r} = {p:4f}")