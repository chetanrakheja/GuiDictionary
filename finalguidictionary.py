# author  : Chetan Rakheja	
# mail: rakhejachetan@gmail.com
# github: rakhejachetan


from tkinter import *
import urllib.request as req
from bs4 import BeautifulSoup
from gtts import gTTS	#text to speech	
import pyperclip #copy to clipboard 
import os	# to run speech file
import webbrowser	#to open web browser

ab =Tk()
ab.title('Dictionary')
ab.configure(highlightbackground="green", highlightcolor="green", highlightthickness=3)

def getHtmlData(URL):
	response = req.urlopen(URL)
	data = response.read()
	soup = BeautifulSoup(data, "html.parser")
	return soup

def GetWordOfTheDay():
	url="http://www.dictionary.com/wordoftheday/"
	HtmlData = getHtmlData(url)
	word_section = HtmlData.find_all("div", {"class" : "definition-header"})
	wordOfTheDay = word_section[0].strong.string
	wordenter.set(wordOfTheDay)

def getWordMeanings(HtmlData):
	# url="http://www.dictionary.com/browse/"+word
	# HtmlData = getHtmlData(url)
	allListOfDetails = HtmlData.find_all("ol")
	listOfDetails = allListOfDetails[0].find_all('li')
	index = 1
	result=""
	# print("Meanings of the word " + word +" is :")
	print()
	# result +="Meanings of the word " + word +" is :"+"\r\n"
	for ele in listOfDetails:
		result+= str(index) + ". " + ele.span.text +"\r\n"
		# print(str(index) + ". " + ele.span.text)
		index = index + 1
	return result

def getWordExamples(HtmlData):
	# url="http://www.dictionary.com/browse/"+word
	# HtmlData = getHtmlData(url)
	allListOfDetails = HtmlData.find_all("ul", {'class', 'css-o9b79t e15kc6du4'})
	if allListOfDetails==[]:
		result="NO EXAMPLES FOUND"
	#print(allListOfDetails)
	else:
		listOfDetails = allListOfDetails[0].find_all('h4')
		# print(listOfDetails)
		index = 1
		result=""
		for ele in listOfDetails:
			result+= str(index) + ". " + ele.text +"\r\n"
			# print(str(index) + ". " + ele.text)
			index = index + 1
	return result

def textToSpeech(convertText,word,use):
	#print("Generating text-to-speech for " + word + "\n ")
	if (convertText!=""):
		language = 'en'
		myobj = gTTS(text = convertText , lang = language)
		Filename = word +use
		print("Filename is "+ Filename +".mp3")# """instead of printing make a pop up of this"""
		myobj.save(Filename + ".mp3")
		os.system(Filename + ".mp3")
	else:
		pass
	
def getWordPronounce(HtmlData):
	# url="http://www.dictionary.com/browse/"+word
	# HtmlData = getHtmlData(url)
	allListOfDetails = HtmlData.find_all("span", {'class', 'css-1khtv86 e1rg2mtf2'})
	pronounce=allListOfDetails[0].text
	return pronounce

def detailedinfo():
	word=wordenter.get()
	if (word==""):
		url ="http://www.dictionary.com/"
	else:	
		url="http://www.dictionary.com/browse/"+word
	pyperclip.copy(url)
	webbrowser.open(url,new=2)

def OnSearchButtonClick():
    word1=wordenter.get()
    url = "http://www.dictionary.com/browse/"+word1
    HtmlData = getHtmlData(url)
	# print(HtmlData)
    wordPronounce = getWordPronounce(HtmlData)
    prolabel.set(wordPronounce)
    #print(wordPronounce) 
	#print("*************************************")
    wordMeaning=getWordMeanings(HtmlData)
    t1.insert('1.0',wordMeaning)
	#print(wordMeaning) #'''change msgBox in front of meaning'''
    WordExamples=getWordExamples(HtmlData)
    t2.insert('1.0',WordExamples)
	#print(WordExamples)  #'''change msgBox in front of example'''
	#print("*************************************")

def onSpeech1ButonClick():
	textToSpeech(wordenter.get(), entry.get(), 'Pronounciation')

def onSpeech2ButonClick():
	textToSpeech(t1.get('1.0','end'),entry.get(),'MEANING')
	
def onSpeech3ButonClick():
	textToSpeech(t2.get('1.0','end'),entry.get(),'SENTENCES')

def reset():
        entry.delete('0','end')
        t1.delete('1.0','end')
        t2.delete('1.0','end')
        prolabel.set('[pruh-nuhn-see-ey-shuh n]')

guiframe=Frame(ab)
guiframe.grid(row=0,column=0,sticky=W)

logo=PhotoImage(file='dict.gif')
label=Label(guiframe,text='     DICTIONARY     ',font=("jokerman",32),padx=80,background='black',foreground='#ccff00')

sub_logo=logo.subsample(x=5,y=5)
label.img=sub_logo
label.config(image=label.img)
label.config(compound='left')
label.grid(row=0,column=0,sticky='w')

guiframe2=Frame(ab)
guiframe2.grid(row=1,column=0,sticky='w')

wordenter=StringVar()

label2 = Label(guiframe2,text='WORD',font=("arial",14),foreground='#73155F',width=10).grid(row=1,column=0)
entry=Entry(guiframe2,font=("arial",14),width=36,textvariable=wordenter,bd=3,foreground='#C93A97',bg='#f78967')
entry.grid(row=1,column=1)
logo1=PhotoImage(file='search.gif')
search_logo=logo1.subsample(x=10,y=10)
searchb=Button(guiframe2,image=search_logo,bd=2,command=OnSearchButtonClick).grid(row=1,column=5,padx=19)
wod=Button(guiframe2,text='Word of the day',bd=2,font=('arial',12,'bold'),fg='#076d27',command=GetWordOfTheDay).grid(row=1,column=6)

empr1=Label(ab).grid(row=2)

prolabel=StringVar()
prolabel.set('[pruh-nuhn-see-ey-shuh n]')
guiframep=Frame(ab)
guiframep.grid(row=3,column=0,sticky='w')
labelp=Label(guiframep,text='Pronounciation:',font=("arial",14),foreground='#73155F',width=15).grid(row=3,column=0)
labelp1=Label(guiframep,textvariable=prolabel,font=("arial",14),foreground='black',bg='pink').grid(row=3,column=1)

speaker=PhotoImage(file='speaker.gif')
smallsp=speaker.subsample(x=16,y=16)
s=Button(guiframep,image=smallsp,bd=1,command=onSpeech1ButonClick).grid(row=3,column=2,padx=10)

empr2=Label(ab).grid(row=4)

guiframe3=Frame(ab)
guiframe3.grid(row=5,column=0,sticky='w')

t1=Text(guiframe3,width=70,height=10,wrap='word',bd=3,bg='#67c2f7')
s1=Scrollbar(guiframe3,orient='vertical',bg='#137e84')
t1.configure(yscrollcommand=s1.set)
s1.configure(command=t1.yview)
t1.grid(row=5,column=1,sticky=N+S)
s1.grid(row=5,column=1,sticky=N+S+E)
label3=Label(guiframe3,text='Meaning',width=10,font=("arial",14),foreground='#73155F').grid(row=5,column=0)

searchb=Button(guiframe3,image=smallsp,bd=1,bg='pink',command=onSpeech2ButonClick).grid(row=5,column=2,sticky='s',padx=2)

empr3=Label(ab).grid(row=6)

guiframe4=Frame(ab)
guiframe4.grid(row=7,column=0,sticky='w')

t2=Text(guiframe4,width=70,height=10,wrap=WORD,bd=3,bg='#bb7cff')
s2=Scrollbar(guiframe4,orient='vertical',bg='#137e84')
t2.configure(yscrollcommand=s2.set)
s2.configure(command=t2.yview)
t2.grid(row=7,column=1,sticky=N+S)
s2.grid(row=7,column=1,sticky=N+S+E)
label3=Label(guiframe4,text='Sentences',width=10,font=("arial",14),foreground='#73155F').grid(row=7,column=0)
searchb1=Button(guiframe4,image=smallsp,bd=1,bg='pink',command=onSpeech3ButonClick).grid(row=7,column=2,sticky='s',padx=2)

empr4=Label(ab).grid(row=8)

guiframe5=Frame(ab)
guiframe5.grid(row=9,column=0,sticky='w')

resetb=Button(guiframe5,text='RESET',font=("arial",12,'bold'),fg='red',command=reset)
resetb.grid(row=9,column=0,padx=120)

detail=Button(guiframe5,text='DETAILED INFO',font=("arial",12,'bold'),fg='red',command=detailedinfo)
detail.grid(row=9,column=1,padx=20)

exitb=Button(guiframe5,text='EXIT',font=("arial",12,'bold'),fg='red',command=ab.destroy)
exitb.grid(row=9,column=2,padx=100)

empr5=Label(ab).grid(row=10)

ab.resizable(False, False)
ab.mainloop()
