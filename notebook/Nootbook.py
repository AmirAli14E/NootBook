import json
import sys
import  datetime
class Note:
    lis=[]
    dic={}
    dictime={}
    def __init__(self,name,gish):
        self.name=name
        self.gish=gish
class Write(Note):
    def __init__(self,title,word):
        super().__init__(name,gish)
        f=open(f'{self.name}.json','w')
        self.title=title
        self.word=word
        time=datetime.datetime.now()
        self.dic[self.title]=self.word
        self.dictime[self.title]=time
class Add (Note) :
    def __init__(self):
        super().__init__(name,gish)
        f=open(f'{self.name}.json','w')
        self.lis.append(self.dic)
        self.dump=json.dump(self.lis,f,indent = 4)
        self.lis.clear()
class Get(Note):
    def __init__ (self):
        super().__init__(name,gish)
        fr=open(f'{self.name}.json','r')
        try:
            self.load=json.load(fr)
            print(self.load)
        except json.decoder.JSONDecodeError:
            print([{}])
            print('add first')
class Getitem(Note) :
    def __init__ ( self, key):
        super().__init__(name,gish)
        fr=open(f'{self.name}.json','r')
        try:
            load=json.load(fr)
            for i in load:
                print(i[key])
        except json.decoder.JSONDecodeError:
            print([{}])
            print('add first')
class Time (Note):
    def __init__(self):
        super().__init__(name,gish)
        try:
            key=input('title:')
            print(self.dictime[key])
        except KeyError:
            print('Not time for title')
    

x=True       
if __name__ == "__main__":
    while x:
        print('enter gish(file,write,add,quit,get,getitem,time):')
        gish=input('')
        if gish.lower() == 'quit' :
            x=False
            sys.exit()
        if gish.lower() == 'file':
            name=input('namefile:')
            n=Note(name,gish)
        try:
            if gish.lower() == 'write':
                    title=input('title:')
                    word=input('word:')
                    w=Write(title,word)
            if gish.lower() =='add':
                a=Add()
            if gish.lower() =='get':
                g=Get()
            if gish.lower() =='getitem':
                try:
                    key=input('title:')
                    gt=Getitem(key)
                except KeyError:
                    print('Not value for title')
            if gish.lower() == 'time':
                t=Time()
        except NameError:
            print('Not file')
            print('enter file')
