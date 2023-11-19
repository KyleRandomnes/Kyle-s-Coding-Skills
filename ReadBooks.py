import pyttsx3
from docx import Document

# Open the Word document
document_path = "The Panda and the Magical Taxi.docx"
doc = Document(document_path)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Read each paragraph and speak it
for paragraph in doc.paragraphs:
    text = paragraph.text
    engine.say(text)
    engine.runAndWait()