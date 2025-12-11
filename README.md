# WhatsApp Chat Analyzer

![WhatsApp Chat Analyzer](https://img.shields.io/badge/WhatsApp-Chat%20Analyzer-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-1.x-orange.svg)
![Windows Forms](https://img.shields.io/badge/Windows%20Forms-Designer-brightgreen.svg)

A Python + Flask API paired with a C# Windows Forms client for analyzing exported WhatsApp chats: upload one or many files, filter by date range, and count keywords with a quick, guided UI.

---

## 📂 Directory Structure
```
WhatsAppChatAnalyzer/
├── flask_api/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── uploads/        # auto-created by Flask
├── windows_forms/
│   ├── WhatsAppChatAnalyzer.sln
│   ├── WhatsAppChatAnalyzer/
│   │   ├── MainForm.cs
│   │   ├── MainForm.Designer.cs
│   │   ├── Program.cs
│   │   └── app.config
├── build/
├── dist/
├── static/
├── requirements.txt
└── README.md
```

## 🛠️ Technologies
- Python + Flask for the web API
- C# + Windows Forms for the desktop UI
- Optional AI-assisted development

## 🚀 Setup and Usage

### 1) Flask API
```bash
pip install -r requirements.txt
cd flask_api
python app.py
```
Flask runs at `http://127.0.0.1:5000`.

### 2) Windows Forms App
1. Open `WhatsAppChatAnalyzer.sln` in Visual Studio.
2. Build and run.
3. Use the UI to select chat files, set date ranges, and enter keywords.

## ✨ Features
- Multi-file upload
- Date range filtering
- Keyword counting
- Simple web+desktop flow

## 📸 Screenshot
![Main Screen](https://github.com/myz21/WhatsappAnalyser/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-11%20122311.png)

## 🤝 Contributing
PRs and issues are welcome. Feel free to suggest improvements or new analytics.

## 📄 License
MIT
