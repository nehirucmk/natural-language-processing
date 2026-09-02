"""
dogal dil isleme calisma dosyasi 1

fazla bosluklari kaldirma
buyuk harfleri kucuk harflere cevirme
noktalama isaretlerini kaldirma
ozel karakterleri kaldirma
yazim hatalarini duzeltme
duz metin elde etme

"""

# pip install textblob beautifulsoup4

# fazla boşlukların temizlenmesi
raw_text = "merhaba      dunya"
print(raw_text.split())
normalized_text_1 = " ".join(raw_text.split())
print(f"temizlenmis metin: {normalized_text_1}")

# büyük küçük harf dönüşümü
raw_text = "mErhaBa dUnya"
normalized_text_2= raw_text.lower()
print(f"{normalized_text_2}")

# noktalama işaretlerini çıkar 
import string
raw_text = "hello, world!!"
normalized_text_3 = raw_text.translate(str.maketrans("","",string.punctuation))
print(f"{normalized_text_3}")

# özel karakterleri çıkar
import re # duzenli ifadeler kütüphanesi
raw_text = "hello@world#2026%~~"
normalized_text_4 = re.sub(r"[^A-Za-z0-9\s]", " ", raw_text) # rakam ve harf dışında her şey gider
print(f"{normalized_text_4}")

# yazım hatalarını düzelt 
from textblob import TextBlob # ingilizce metine uygula bunu kullanacaksan
raw_text = "machien laerning is exhuasting"
normalized_text_5 = TextBlob(raw_text).correct()
print(f"{normalized_text_5}")

# html etiketlerinden düz metin
from bs4 import BeautifulSoup
raw_html = "<div>hello world </div>"
normalized_text_6 = BeautifulSoup(raw_html, "html.parser").get_text()
print(f"{normalized_text_6}")