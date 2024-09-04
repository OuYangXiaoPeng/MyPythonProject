import os

import PyPDF2
import pyttsx3
from docx2pdf import convert


word_path = 'file'
word_to_pdf = 'file2'
for i, j, name in os.walk(word_path):
    for word_name in name:
        convert(word_path + "/" + word_name, word_to_pdf + "/" + word_name.replace("docx", "pdf"))

pdfreader = PyPDF2.PdfFileReader(open('./file2/result2-2.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    cleaned_text = text.strip().replace('\n', ' ')
    print(cleaned_text)
    speaker.save_to_file(cleaned_text, 'story.mp3')
    speaker.runAndWait()
speaker.stop()
os.system('story.mp3')
