"""
max entropi ile duygu analizi

adımlar:
    veri seti
    nltk max ent classifier model
    yeni cümlelerden öznitelik çıkarımı ve sınıflandırma
    ayırt edici özellikleri incele
"""

from nltk.classify import MaxentClassifier

train_data = [
    ({"love": True, "amazing": True, "great": True, "terrible": False, "bad": False}, "positive"),
    ({"hate": True, "terrible": True, "awful": True, "love": False}, "negative"),
    ({"happy": True, "joy": True, "good": True, "sad": False}, "positive"),
    ({"sad": True, "depressed": True, "bad": True, "happy": False, "amazing": False}, "negative"),
    ({"wonderful": True, "pleasant": True, "nice": True, "awful": False}, "positive"),
    ({"angry": True, "hate": True, "upset": True, "good": False, "great": False}, "negative"),
]

classifier = MaxentClassifier.train(train_data, max_iter = 15)

classifier.show_most_informative_features(5) # en ayırt edici özellikleri göster

# öznitelik için yardımcı fonksiyon
def extract_features(sentence: str, vocab=None):
    tokens= sentence.lower().split() # basit tokenizasyon
    if vocab is None:
        vocab = ["love", "amazing", "great", "good", "happy", "joy", "wonderful", "pleasant", "nice",
        "hate", "terrible", "awful", "bad", "sad", "depressed", "angry", "upset"]

    return {word: (word in tokens) for word in vocab}

text_sentences = [
    "I love this product it is amazing and wonderful",
    "This is bad I hate the design it is awful",
    "The movie was good and pleasant overall"
]

for i, sent in enumerate(text_sentences, 1):
    feats = extract_features(sent)
    label = classifier.classify(feats)
    prob_dist = classifier.prob_classify(feats) # sınıfın olasılık dağılımı
    p_pos = prob_dist.prob("positive")
    p_neg = prob_dist.prob("negative")
    print(f"test {i} {sent}")
    print(f"predicted: {label}, P(pos)= {p_pos}, P(neg)= {p_neg}")
