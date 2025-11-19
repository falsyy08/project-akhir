import google.generativeai as genai
import os
import time

# API Key Anda sudah benar diapit kutip.
API_KEY = 'AIzaSyB3O4Btig_KmXtntLXk316nq8ocR6Ym2YI' # Ini harus kunci ASLI Anda
genai.configure(api_key=API_KEY)

# --- Pilih Model Gemini ---
model = genai.GenerativeModel('gemini-pro')

print("AI Percakapan siap! Ketik 'exit' untuk keluar.")
print("---")

# --- Loop Percakapan ---
while True:
    user_input = input("Anda: ")

    if user_input.lower() == 'exit':
        print("AI: Sampai jumpa!")
        break

    try:
        # Mengirim pesan pengguna ke model Gemini
        response = model.generate_content(user_input)

        # Menampilkan respons dari AI
        print(f"AI: {response.text}")

    except Exception as e:
        print(f"AI: Maaf, terjadi kesalahan atau saya tidak bisa memproses permintaan itu. ({e})")
        time.sleep(1)