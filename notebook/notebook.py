import json
import sys
import  datetime
class note:
    lis=[]
    dic={}
    dictime={}
    def __init__(self,name,gish):
        self.name=name
        self.gish=gish
    def write(self,title,word):
        f=open(f'{self.name}.json','w')
        self.title=title
        self.word=word
        time=datetime.datetime.now()
        self.dic[self.title]=self.word
        self.dictime[self.title]=time
    def add(self):
        f=open(f'{self.name}.json','w')
        self.lis.append(self.dic)
        self.dump=json.dump(self.lis,f,indent = 4)
        self.lis.clear()
    def get (self):
        fr=open(f'{self.name}.json','r')
        try:
            self.load=json.load(fr)
            print(self.load)
        except json.decoder.JSONDecodeError:
            print([{}])
            print('add first')
    def getitem(self,key):
        fr=open(f'{self.name}.json','r')
        try:
            load=json.load(fr)
            for i in load:
                print(i[key])
        except json.decoder.JSONDecodeError:
            print([{}])
            print('add first')
    def time(self):
        try:
            key=input('title:')
            print(self.dictime[key])
        except KeyError:
            print('Not time for title')
        

x=True
while x:
    print('enter gish(file,write,add,quit,get,getitem,time):')
    gish=input('')
    if gish.lower() == 'quit' :
        x=False
        sys.exit()
    if gish.lower() == 'file':
        name=input('namefile:')
        n=note(name,gish)
    try:
        if gish.lower() == 'write':
            title=input('title:')
            word=input('word:')
            n.write(title,word)
        if gish.lower() =='add':
            n.add()
        if gish.lower() =='get':
            n.get()
        if gish.lower() =='getitem':
            try:
                key=input('title:')
                n.getitem(key)
            except KeyError:
                print('Not value for title')
        if gish.lower() == 'time':
            n.time()
    except NameError:
        print('Not file')
        print('enter file')
