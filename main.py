import os
import pytesseract
from PIL import ImageGrab
import keyboard
import requests
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Tesseract OCR path (ensure this matches your installation)
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

# ✅ Telegram Bot credentials from environment
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ✅ Send text to Telegram bot
def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN or CHAT_ID not set in .env file.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=data)
        return response.ok
    except Exception as e:
        print(f"❌ Failed to send message: {e}")
        return False

# ✅ Capture screen, extract text, and send
def capture_and_send():
    print("📸 Capturing screen...")
    screenshot = ImageGrab.grab()
    extracted_text = pytesseract.image_to_string(screenshot).strip()

    if not extracted_text:
        print("⚠️ No text found on screen.")
        return

    print("📤 Sending to Telegram...")
    success = send_to_telegram(extracted_text)
    if success:
        print("✅ Sent to Telegram!")
    else:
        print("❌ Failed to send to Telegram.")

# ✅ Register global hotkey
keyboard.add_hotkey('ctrl+b', capture_and_send)

print("🔁 Bot is running...")
print("💡 Press Ctrl+B to capture screen and send text to Telegram.")
keyboard.wait()
