# GuiDictionary
It is a dictionary with gui made using python,uses web scrapping to get the data from dictionary.com , have option to listen to the meaning,example sentences,pronunciation, increase vocabulary by seeing word of the day(from dictionary.com)


dependencies :<br>
BeautifulSoup(bs4)  (for web scrapping)<br>
urllib (for web scrapping)<br>
gTTS(for text to speech)<br>
pyperclip(Copy To clipboard)<br>

<h3>About the project</h3>

it get data(meaning, sentences,pronunciation,etc) from dictionary.com,

uses BeautifulSoup (bs4 is to be downloaded),

uses google text to speech (gtts) to conver meaning, sentences,pronunciation to speech

File which Contains the speech will be saved in the directory(path of cmd)

clicking Detailed info will open webpage of dictionary.com where user can see full details, url of the webpage will be copied to clipboard as well

<h3>Things to be taken care</h3>
<hr>
while running the code make sure you have all the dependencies,your cmd must be in the same directory as your code as not doing so may generate error as gif files(clipart for search,speech button) will not be loaded properly, make sure you have a working internet connection, mp3 player to listen to speech

<hr>
<h2>ScreenShots</h2>
<h4>
Blank Default interface
</h4>

![github-small](https://github.com/rakhejachetan/GuiDictionary/blob/5978962b19ca4bf5316add9b1d907c8b6a5a78e6/DictionarySS/DictBlank.PNG)

<h4>
Word to be searched entered(in this case it is the word of the day) 
</h4>

![github-small](https://github.com/rakhejachetan/GuiDictionary/blob/5978962b19ca4bf5316add9b1d907c8b6a5a78e6/DictionarySS/DictWithWord.PNG)

<h4>
When you click the search button
</h4>

![github-small](https://github.com/rakhejachetan/GuiDictionary/blob/5978962b19ca4bf5316add9b1d907c8b6a5a78e6/DictionarySS/DictSearchBtnClick.PNG)

<h4>
when all the meaning, sentences,pronunciation is found
</h4>

![github-small](https://github.com/rakhejachetan/GuiDictionary/blob/5978962b19ca4bf5316add9b1d907c8b6a5a78e6/DictionarySS/DictWithMeanings.PNG)



