# 🖼️ Telegram OCR Screenshot Bot

A lightweight Python tool that captures your screen, extracts visible text using Tesseract OCR, and instantly sends it to your Telegram bot with a global hotkey.

---

## 🚀 Features

- 📸 Press `Ctrl+B` to instantly capture the screen  
- 🧠 Uses Tesseract OCR to extract readable text  
- 📲 Sends results to your Telegram chat using your bot  
- 🔐 Uses `.env` to keep your bot token and chat ID secure  

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/telegram-ocr-screenshot-bot.git
cd telegram-ocr-screenshot-bot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```env
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

⚠️ **Make sure Tesseract is installed and the path is correct.**

---

## ▶️ Usage

```bash
python main.py
```

Then press `Ctrl+B` to:

* Capture the current screen
* Extract text using OCR
* Send to your Telegram bot


