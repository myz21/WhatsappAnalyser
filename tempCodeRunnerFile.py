from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import re
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist('files[]')
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    words_to_count = request.form['words_to_count'].split(',')
    message_counts = []

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        message_count = count_messages(file_path, start_date, end_date, words_to_count)
        message_counts.append((filename, message_count))

    return render_template('result.html', message_counts=message_counts)

def count_messages(file_path, start_date, end_date, words_to_count):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the date format used in the WhatsApp export
    date_format = "%m/%d/%y, %H:%M %p"

    # Compile a regex to match dates and messages
    message_pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:AM|PM)) - (.*?): (.*)')

    # Initialize count dictionary for words
    word_counts = {word.lower().strip(): 0 for word in words_to_count}

    start_date = datetime.strptime(start_date, date_format.split(",")[0].strip())
    end_date = datetime.strptime(end_date, date_format.split(",")[0].strip())

    # Iterate over each line matching the pattern
    for match in message_pattern.finditer(content):
        message_date = datetime.strptime(match.group(1), date_format)
        if start_date <= message_date <= end_date:
            message_text = match.group(3).lower()
            for word in word_counts:
                word_counts[word] += message_text.count(word)

    return word_counts

if __name__ == '__main__':
    app.run(debug=True)
