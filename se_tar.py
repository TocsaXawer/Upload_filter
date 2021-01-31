#mappa olvasása 
#addatok csoportosítás formátum szerint 
#adatok áthelyezése a formátum szerinti mappába

import shutil
import fnmatch
import os

start_path = 'UPLOAD/'
end_path_video = "static/Function/Video"
end_path_zene = "static/Function/zene"
end_path_other = "static/Function/other"

#<<<<<<<<Data Filter>>>>>>>>>
class video_select():
    filles_video = fnmatch.filter(os.listdir(start_path), "*.mp4")

    vide_db = len(filles_video) 
pass

class music_select():
    filles_zene = fnmatch.filter(os.listdir(start_path), "*.mp3")
    filles_zene1 = fnmatch.filter(os.listdir(start_path), "*.wav")
    filles_zene2 = fnmatch.filter(os.listdir(start_path), "*.m4a")
    filles_zene3 = fnmatch.filter(os.listdir(start_path), "*.ap3")
    filles_zene4 = fnmatch.filter(os.listdir(start_path), "*.wma")
    filles_zene5 = fnmatch.filter(os.listdir(start_path), "*.ogg")
    zene_db = len(filles_zene) + len(filles_zene1) + len(filles_zene2) + len(filles_zene3) + len(filles_zene4)
pass

#<<<<<<A datok olvasása a start mapából>>>>>>>>>
class read():
    import os
    mapa = os.listdir(start_path)
pass



#<<<<<<<<<<<<<Futató folyam>>>>>>>>>>
def folyam():
    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = video_select.filles_video
        for i in range(len(x)):
            k = (x[i])
            if m  == k:
                x = start_path + m
                shutil.move(x, end_path_video)


    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene5
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)

    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)

    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene1
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)
                
    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene2
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)

    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene3
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)

    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = music_select.filles_zene4
        for i in range(len(x)):
            y = (x[i])
            if m  == y:
                x = start_path + m
                shutil.move(x, end_path_zene)

    for i in range(len(read.mapa)):
        m = read.mapa[i]
        x = start_path + m
        shutil.move(x, end_path_other)
pass

def end():
    try:
        folyam()
    except:
        pass 
pass 
end()
