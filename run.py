import os

try:
    os.system("gnome-terminal -e 'bash -c \"python3.9 app.py; exec bash\"'")
    os.system("gnome-terminal -e 'bash -c \"python3.9 select_runer.py; exec bash\"'")
    os.system("python3 app.py")
    os.system("start cmd /c python app.py")
    os.system("start cmd /c python select_runer.py")
    
except:
    print('A cortex File Selectation & a server not start')
pass 
