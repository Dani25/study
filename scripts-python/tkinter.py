"""
import sys
sys.stderr.write('test\n')
sys.stderr.flush()
sys.stdout.write('test\n')

print(sys.argv)

if (len(sys.argv))>1:
    print(float(sys.argv)+5)
"""

#import urllib.request
#import urllib.parse
"""
#x = urllib.request.urlopen("http://www.google.com")
#print (x.read())

url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}
data =  urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

"""
#import re
#exempleString =
'''
Jessica is 15 years old and Daniel is 27 years old.
Edward is 97 years old and he`s grandfather, Oscar, is 102 years old.

'''
'''
print (exempleString)

ages = re.findall(r'\d{1,3}', exempleString)
names = re.findall(r'[A-Z][a-z]*', exempleString)

print(ages)
print(names)

ageDict={}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)

'''
'''
import urllib.parse
import urllib.request
import re
url = 'http://pythonprogramming.net'
values =  {'s':'basic',
            'submit':'search'
           } 
data =  urllib.parse.urlencode(values)
data =  data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)

'''
from Tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master =  master

        self.init_window()

    def init_window(self):

        self.master.title('GUI')
        
        self.pack(fill=BOTH, expand=1)

        #quitButton = Button(self, text = 'Quit',command = self.client_exit)
        #quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        
        edit = Menu(menu)
        edit.add_command(label='Show image', command=self.showImg)
        edit.add_command(label='Show text', command=self.showText)
        menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        exit()
    def showImg(self):
        load = Image.open('Capture.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.image = render
        img.place(x=0, y=0)
    def showText(self):
        text = Label(self, text='hi. nice to meet you!')
        text.pack()
        
        
root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()
    
