"""
kök veya temel form (lemma) bulma
stemming: porter stemmer
lemmatization: word net lemmatizer
"""
# pip install nltk

import nltk 
nltk.download("wordnet") # lemmatization için gerekli wordnet veritabanı
nltk.download("omw-1.4") # wordnet için ek dil desteği

# stemming
from nltk.stem import PorterStemmer # ingilizce için popüler stemmer algoritması

stemmer = PorterStemmer()

word_stem = ["walking", "walked", "walks", "furiously", "better", "swims", "swimming"] # örnek kelimeler

stems = [stemmer.stem(w) for w in word_stem] # kökler
print(f"orijinal: {word_stem}")
print(f"kökler: {stems}")

# bazılarında hata yapıyor tam doğruluk yok comparativeleri yok sayıyor

# lemmatization
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer() 

words_lemma = ["sleeping", "sleep", "observation", "children", "cheaper"]

lemmas = [lemmatizer.lemmatize(w) for w in words_lemma]
print(f"orijinal: {words_lemma}")
print(f"lemmas: {lemmas}")