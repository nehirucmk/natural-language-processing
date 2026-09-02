"""
önemsiz kelimeleri çıkarma yöntemleri
ingilizce stop words çıkarma (nltk)
türkçe stop words çıkarma (nltk)
manuel çıkarma, kütüphanesiz
"""

# pip install nltk
import nltk 
from nltk.corpus import stopwords

# ilk çalıştırmada stop words veri seti indiriliyor
nltk.download("stopwords")

stop_words_eng = set(stopwords.words("english"))

eng_text = "how to bake a brownie without sugar and eggs and how long do i have to wait for it to be ready to eat?"
eng_text_list = eng_text.split()
print(eng_text_list)

# kelime stop words listesinde yoksa onu yeni listeye ekle
filtered_words_eng = [word for word in eng_text_list if word.lower() not in stop_words_eng]
print(f"orijinal: {eng_text}")
print(f"stop word yok: {filtered_words_eng}")

# türkçe 
stop_words_tr = set(stopwords.words("turkish"))

tr_text = "şekersiz ve yumurtasız bir brownie nasıl yapabilirim ve yemek için hazır olmasına kadar ne kadar süre beklemem gerekiyor?"
tr_text_list = tr_text.split()

filtered_words_tr = [word for word in tr_text_list if word.lower() not in stop_words_tr]

print(f"orijinal: {tr_text}")
print(f"stop word yok: {filtered_words_tr}")

# manuel stop words çıkarma
custom_tr_stopwords = ["ve", "ile", "daha", "ancak", "için", "çünkü", "zaten", "veya"]
custom_text= "Şekersiz ve yumurtasız, içi ıslak ve yoğun bir brownie yapmak için rafine şeker yerine hurmadan, yumurta yerine ise püre haline getirilmiş malzemelerin bağlayıcılığından faydalanabilirsiniz. Ancak yumurta içermediği için fırından çıktıktan sonra kıvam alıp toparlanması adına en az 1 saat soğumasını beklemeniz gerekir."
custom_text_list = custom_text.split()
filtered_custom_words_tr = [word for word in custom_text_list if word.lower() not in custom_tr_stopwords]
print(f"orijinal: {custom_text}")
print(f"stop word yok: {filtered_custom_words_tr}")