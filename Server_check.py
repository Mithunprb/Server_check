#!usr/bin/python
import requests as req
import time
import threading
import webbrowser
import colorama
from colorama import Fore, Style
count = 0

website = 'https://www.google.co.in'

def notify():
    global cond
    while cond:

        try:
            import winsound
        except ImportError:
            import os

            def playsound(frequency, duration):
                os.system('beep -f%s -l %s' % (500, 500))
        else:
            def playsound(frequency, duration):
                winsound.Beep(500.500)
        finally:
            pass
        time.sleep(0.2)
        print(f"{Fore.GREEN}Checking...{Style.RESET_ALL}")


while True:
    try:
        cont = req.get(website)
        code = cont.status_code
        if code == 200:
            cond = True
            try:
                if count == 0:
                    count += 1
                    threading.Thread(target=notify).start()
                    check = webbrowser.open(website)

            except Exception as e:
                print(e)
                

        else:
            print(f"{Fore.RED}Server not responding....{Style.RESET_ALL}")
            cond = False
            count = 0

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass

