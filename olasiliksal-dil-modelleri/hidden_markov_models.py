"""

partof speech  (POS) sözcük türü etiketleme işleme
hidden markov model tabanlı bir etiketleyici:
1- küçük, elle tanımlanmış bir eğitim veri kümesi HMM eğitimi ve testleri yap
2- nltk'in conll2000 veri seti ile kapsamlı HMM eğitimi

"""

import nltk
from nltk.tag import hmm

# elle tanımlı küçük veri seti
"""
PRP: zamir
VBP: geniş zaman fiil
DT: belirteç
NN: isim
VBZ: üçüncü tekil şahıs fiil
"""
toy_train_data = [
    [("I", "PRP"), ("am", "VBP"), ("a", "DT"), ("developer", "NN")],
    [("You", "PRP"), ("are", "VBP"), ("a", "DT"), ("student", "NN")],
    [("He", "PRP"), ("is", "VBP"), ("an", "DT"), ("engineer", "NN")]
]

# hidden markov model eğiticisi oluştur
toy_trainer = hmm.HiddenMarkovModelTrainer()

# training
toy_hmm_tagger = toy_trainer.train(toy_train_data)
toy_test_sentence_1 = "I am an engineer".split() # tokenlara ayır
toy_tags_1 = toy_hmm_tagger.tag(toy_test_sentence_1) # her kelime için en olası POS etiketini döndürür
print(f"test cumlesi 1: {toy_test_sentence_1}")
print(f"etiketler: {toy_tags_1}")

from nltk.corpus import conll2000

nltk.download("conll2000") # eğitim ve test cümleleri için conll2000 veri seti indiriliyor

big_train_data =conll2000.tagged_sents("train.txt")
big_test_data = conll2000.tagged_sents("test.txt")

# hmm tanımla ve eğit
big_trainer = hmm.HiddenMarkovModelTrainer()
big_hmm_tagger = big_trainer.train(big_train_data)

# test
big_test_sentence_1 = "We enjoy learning machine learning concepts".split()
big_tags_1 = big_hmm_tagger.tag(big_test_sentence_1)
print(f"test cümlesi 1: {big_test_sentence_1}")
print(f"etiketler: {big_tags_1}")