import PyPDF2
from gtts import gTTS
import os
import pygame

FILEINPUT = 'pdf.mp3'

pdfReader = PyPDF2.PdfFileReader(open('secure_property.pdf','rb'))
language = 'en'
long_text = ''




# this loops whole pdf, api takes too long
'''
for page_num in range(pdfReader.numPages):
	text = pdfReader.getPage(page_num).extractText()
	#print(text)
	long_text += text
'''

for page_num in range(1):
	text = pdfReader.getPage(page_num).extractText()
	#print(text)
	long_text += text
	print('____________',page_num)

print(long_text[0:100])
myobj = gTTS(text=long_text, lang = language, slow = False)
myobj.save(FILEINPUT)

#FILEINPUT = 'bacon.wav'





#plasy the mp3 in pygame 
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.init()
pygame.mixer.music.load(FILEINPUT)
pygame.mixer.music.play(loops=0, start=0.0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)




print("after playing")
