import pyttsx3
import PyPDF2

engine=pyttsx3.init()
book= open('rich dad poor dad.pdf','rb')
pdfReader= PyPDF2.PdfReader(book)
pages= len(pdfReader.pages)
print("Total pages:", pages)

mySpeaker= pyttsx3.init()
page= pdfReader.pages[9]
text= page.extract_text()

engine.setProperty('volume', 2.0)
#rate= engine.getProperty('rate')
engine.setProperty('rate', 150)
mySpeaker.say(text)
mySpeaker.runAndWait()

