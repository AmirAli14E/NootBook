
import json

def dec(file):

    def json_txt():
        try:
            json_file = json.load(file())
        except Exception:
            try:
                text_file = file()
                text_file_read=text_file.read()
            except Exception:
                print('enter file(json or txt)')
            else:
                print(text_file_read)
        else:
            print(json_file)

    return json_txt
f=input(':')
@dec
def fun_file():
    global f
    file = open(f,'r')
    return file
fun_file()