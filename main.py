import json
import random

def load_dialogs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Dialog dosyası bulunamadı!")
        return {}
    except json.JSONDecodeError:
        print("Dialog dosyası hatalı formatta!")
        return {}

def save_dialogs(file_path, dialogs):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(dialogs, f, ensure_ascii=False, indent=4)

def chatbot_ile_sohbet(istem, dialoglar):
    istem = istem.lower().strip()
    if istem in dialoglar:
        return random.choice(dialoglar[istem])
    else:
        return "Üzgünüm, bunun hakkında konuşacak bilgiye sahip değilim."

dialoglar = load_dialogs('diyaloglar.json')

print("Chatbot'a hoş geldiniz! Çıkış yapmak için 'çıkış' yazın.")
while True:
    istem = input("Sen: ")
    if istem.lower().strip() == "çıkış":
        print("Chatbot: Görüşmek üzere!")
        break
    yanit = chatbot_ile_sohbet(istem, dialoglar)
    print(f"Chatbot: {yanit}")

    # Yeni dialog eklemek için
    if istem.lower().strip() == "yeni dialog ekle":
        yeni_istem = input("Yeni istem: ").lower().strip()
        yeni_yanit = input("Yeni yanıt: ").strip()
        if yeni_istem in dialoglar:
            dialoglar[yeni_istem].append(y
