import pyttsx3,PyPDF2,os
pdfreader = PyPDF2.PdfFileReader(open('./file2/result2-2.pdf','rb'))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    cleaned_text = text.strip().replace('\n',' ')
    print(cleaned_text)
    speaker.save_to_file(cleaned_text,'story.mp3')
    speaker.runAndWait()
speaker.stop()
os.system('story.mp3')
