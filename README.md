# WhatsApp Chat Analyzer

![WhatsApp Chat Analyzer](https://img.shields.io/badge/WhatsApp-Chat%20Analyzer-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-1.x-orange.svg)
![Windows Forms](https://img.shields.io/badge/Windows%20Forms-Designer-brightgreen.svg)

## 🚀 About the Project

**WhatsApp Chat Analyzer** is a powerful tool for analyzing your WhatsApp chat history. This project consists of a web API built with Python and Flask, and a Windows Forms interface created with C#. By leveraging AI tools, we aimed to make the analysis process as seamless and efficient as possible.

## 📂 Directory Structure

WhatsAppChatAnalyzer/
├── flask_api/
│ ├── app.py
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ └── uploads/ (This folder will be automatically created by the Flask app)
├── windows_forms/
│ ├── WhatsAppChatAnalyzer.sln
│ ├── WhatsAppChatAnalyzer/
│ │ ├── MainForm.cs
│ │ ├── MainForm.Designer.cs
│ │ ├── Program.cs
│ │ └── app.config
├── build/
├── dist/
├── static/
├── requirements.txt
└── README.md


## 🛠️ Technologies Used

- **Python**: For data analysis and the Flask web API.
- **Flask**: For building the web API.
- **C# and Windows Forms**: For creating the user interface.
- **AI Tools**: For aiding in the code writing process and project structure definition.

## 🔧 Setup and Usage

### 1. Setting Up the Flask API

1. **Install Python and Flask**: Ensure Python 3.x and Flask are installed on your system.
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Flask API Project**:
    ```bash
    cd flask_api
    python app.py
    ```
    This command will start the Flask server at `http://127.0.0.1:5000`.

### 2. Setting Up the Windows Forms Application

1. **Open Visual Studio**: Open `WhatsAppChatAnalyzer.sln` in Visual Studio.
2. **Build and Run the Project**: Build and run the project. Once the application starts, you can upload your WhatsApp chat files and analyze them through the interface.

## 📸 Screenshots

### Main Screen
![Main Screen](https://github.com/myz21/WhatsappAnalyser/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-11%20122311.png)


## ✨ Features

- **Multi-file Upload**: Upload multiple WhatsApp chat files at once.
- **Date Range Filtering**: Filter chats within a specific date range.
- **Keyword Counting**: Count how many times specified keywords appear in the chats.

## 📚 Usage

1. **File Selection**: Click the `Browse` button to select the WhatsApp chat files you want to analyze.
2. **Enter Date Range**: Enter the start and end dates.
3. **Keywords**: Enter the keywords you want to count.
4. **Upload and Analyze**: Click the `Upload` button to upload your files and view the analysis results.

## 🤝 Contributing

If you would like to contribute to this project, please create a pull request or open an issue.


This project was developed with the help of AI tools. Leveraging AI in the code writing process and project structuring has been an incredible experience, making development faster and more efficient.

If you have any questions, feel free to reach out.

Happy analyzing! 😊
