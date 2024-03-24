import json
import random

# Diyalogları içeren JSON dosyasını yükle
with open('diyaloglar.json', 'r', encoding='utf-8') as f:
    dialoglar = json.load(f)

def chatbot_ile_sohbet(istem):
    """
    Kullanıcının isteğine göre chatbot'un yanıtını döndürür.
    """
    # Kullanıcı isteğini küçük harfe çevir
    istem = istem.lower()
    # Eğer istem dialoglar içindeyse, karşılık gelen yanıtı döndür
    if istem in dialoglar:
        return random.choice(dialoglar[istem])
    else:
        # Eğer istem bilinmiyorsa, genel bir yanıt ver
        return "Üzgünüm, bunun hakkında konuşacak bilgiye sahip değilim."

# Chatbot ile sohbet etmeyi deneyin
while True:
    istem = input("Sen: ")
    if istem == "çıkış":
        print("Chatbot: Görüşmek üzere!")
        break
    yanit = chatbot_ile_sohbet(istem)
    print(f"Chatbot: {yanit}")
