# Mappa olvasása 
# ellenőrzés a dat filokal 
# Ha nem egyeznek akkor generál
# re generálja a dat filokat 

import os
import fnmatch
import shutil

import random
import string



#<<< Def ek >>>

def listToString(s):   
    str1 = ""  
      
    for ele in s:  
        str1 += ele   
    return str1  

#<<< mappa útvonal >>>
vmo = 'static/Function/Video'
omo = 'static/Function/other'
zmo = 'static/Function/zene'
dmo = 'static/Function/Documents'

#<<< Mappák olvasása >>>

v = os.listdir(vmo)
o = os.listdir(omo)
z = os.listdir(zmo)
d = os.listdir(dmo)

#<<< HTML mappák elérése>>>

hvm = 'Video/'
hzm = 'Zene/'
hdm = 'Documents/'
hom = 'Other/'

#<<< HTML files name >>>

HNv = len(v)
HNo = len(o)
HNz = len(z)
HNd = len(d)

print("Videók:", HNv)
print("Zenék:", HNz)
print("Documentumok:", HNd)
print("Egyébb:", HNo)

#<<<Másodlagos tároló>>>
vmoe = 'static/Function_end/Video'
vmoz = 'static/Function_end/Zene'
vmod = 'static/Function_end/Documents'
vmoo = 'static/Function_end/Other'



#<<<Másodlagos tárhely olvasása>>>>
ve = os.listdir(vmoe)
ze = os.listdir(vmoz)
de = os.listdir(vmod)
oe = os.listdir(vmoo)

wve = open('dat/End_video.dat', 'w+')
for i in range(len(ve)):
    wve.write(ve[i])
wve.close()

woe = open('dat/End_other.dat', 'w+')
for i in range(len(oe)):
    woe.write(oe[i])
woe.close()

wde = open('dat/End_documents.dat', 'w+')
for i in range(len(de)):
    wde.write(de[i])
wde.close()



#<<< Server Conditional>>>
def serv_runner():
    tex = "\n"+ "if __name__ == '__main__': app.run(host='0.0.0.0', port=4555, debug=True)"
    mv = open('app.py', 'a')
    mvw = mv.write(tex)
    mv.close()
pass

def searchv(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            os.remove(vmo+'/'+list[i])
            return True
    return False

def searchz(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            os.remove(zmo+'/'+list[i])
            return True
    return False

def searchd(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            os.remove(dmo+'/'+list[i])
            return True
    return False

def searcho(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            os.remove(omo+'/'+list[i])
            return True
    return False
    
def SERCON():
    counter = 0
    with open('app.py', 'r') as read_obj:
        for line in read_obj:
            counter += 1
    print(counter)
    x = counter-1
    y = counter-2

    original_file = 'app.py'
    line_numbers = [x, y]
    is_skipped = False
    counter = 0
    dummy_file = original_file + '.mcs'

    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        for line in read_obj:
            if counter not in line_numbers:
                write_obj.write(line)
            else:
                is_skipped = True
            counter += 1

    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)
pass

#<<< Ellenőrzés a dat filokal >>>
filv_end_place = 'static/Function_end/Video'
filz_end_place = 'static/Function_end/Zene'
fild_end_place = 'static/Function_end/Documents'
filo_end_place = 'static/Function_end/Other'
#<<< Videók  >>>
rv = open('dat/Video.dat', 'r')
rvc = rv.read()

vc = (listToString(v))

if vc == rvc:
    print('Video: end')
elif vc != rvc:

    SERCON()
    for i in range(len(ve)):
        if searchv(v, ve[i]):
            print('ez az')
    print('Video: Generál')
    
    for i in range(len(v)):
	

        #html file name general
        name_v = v[i]
        kiter = '.html'
        fname = (name_v + kiter)

		

        if listToString(v) != fname:
            #html file generálás
            #html töredékek olvasása
            #<1>
            h1m = open('Html_minták/Video/1v.hmint', 'r')
            h1m_o = h1m.read()
            #<2>
            h2m = open('Html_minták/Video/2v.hmint', 'r')
            h2m_o = h2m.read()
            #code össze ilesztése
            code = h1m_o + '../../' + filv_end_place + '/' + v[i] + h2m_o
            #code mentése 
            codem = open('templates/Video/'+fname, 'x')
            codem.write(code)
            codem.close()
            #python code generálás 
            p1m = open('Python_minták/1.pmint', 'r')
            p1m_o = p1m.read()

            p2m = open('Python_minták/2.pmint', 'r')
            p2m_o = p2m.read()

            p3m = open('Python_minták/3.pmint', 'r')
            p3m_o = p3m.read()

            p4m = open('Python_minták/4.pmint', 'r')
            p4m_o = p4m.read()

            m = HNv + i
            sz=str(m)
            defek = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            codep = p1m_o + "\"/" + name_v + "\"" + p2m_o + 'v' + defek + p3m_o + "\"" + hvm + fname + "\"" + p4m_o + "\n"*3

            codepm = open('app.py', 'a')
            codepm.write(codep)
            codepm.close()
            k = vmo+ '/' + v[i]
            shutil.move(k, filv_end_place)

            #<<< Makro >>>
            

    serv_runner()
        

if v != []:
    for i in range(len(v)):
        q = v[i]
        e = vmo+'/'+q
        try:
            os.remove(e)
        except:
            pass
wv = open('dat/Video.dat', 'w')
wv.write(vc)

#<<< Zenék >>>
rz = open('dat/zene.dat', 'r')
rzc = rz.read()

zc = (listToString(z))

if zc == rzc:
    print('Zene: end')
elif zc != rzc:
    print('Zene: Generál')
    #wz = open('dat/zene.dat', 'w')
    #wz.write(zc)
    for i in range(len(z)):
        for i in range(len(ze)):
            if searchz(z, ze[i]):
                e = zmo + '/' +z[i] 
                os.remove(e)
    
    for i in range(len(z)):
        k = zmo + '/' + z[i]
        shutil.move(k, filz_end_place)
    zh = 'static/Function_end/Zene/'
    jse = 'static/Js/'
    z = os.listdir(zh)
    j = os.listdir(jse)

    for i in range(len(j)):
        if j[i] == 'zene_dat.json':
            os.remove(jse+j[i])
        if j[i] == 'Zene.Js':
            os.remove(jse+j[i])

    sz1 = open('Html_minták/Zene/1.töredékjs', 'r')
    sz1_o = sz1.read()

    sz2 = open('Html_minták/Zene/2.töredékjs', 'r')
    sz2_o = sz2.read()

    f = open('static/Js/zene_dat.json', 'x')

    for i in range(len(z)):
        print(z[i])
        name = z[i]
        macs = str()
        code = "\t"+ '{' + "\n" +  "\t" +'name: ' + "\"" + name + "\"" + ',' + "\n" + "\t" +'url: ' + "\"" +"../"*2+  zh + name + "\"" + "\n" + "\t" +'},' + "\n"
        f.write(code)

    f.close()

    sz_data_bank =open('static/Js/zene_dat.json', 'r')
    sz_o = sz_data_bank.read()

    htmlcod = sz1_o + sz_o + sz2_o

    zene_js = open('static/Js/Zene.Js', 'x')
    zene_m = zene_js.write(htmlcod)

        #html file name general
        

        #html file generálás

    if z != []:
        for i in range(len(z)):
            q = z[i]
            e = zmo+'/'+q
            try:
                os.remove(e)
            except:
                pass

#<<< Other >>>
ro = open('dat/other.dat', 'r')
roc = ro.read()

oc = (listToString(o))

if oc == roc:
    print('Other: end')
elif oc != roc:
    print('Other: Generál')
    # wo = open('dat/other.dat', 'w')
    # wo.write(oc)
    for i in range(len(o)):
    	

        #html file name general
        name_o = o[i]
        kiter = '.html'
        fname = (name_o+kiter)
        

        if o != fname:
            SERCON()
            #html file generálás
            #html töredékek olvasása 
            #<1>
            h1m = open('Html_minták/Other/1.hmint', 'r')
            h1m_o = h1m.read()
            #<2>
            h2m = open('Html_minták/Other/2.hmint', 'r')
            h2m_o = h2m.read()
            #<3>
            h3m = open('Html_minták/Other/3.hmint', 'r')
            h3m_o= h3m.read()
            #code össze ilesztése
            code = h1m_o + '../../' + filo_end_place + '/' + o[i] + h2m_o + '../../' + fild_end_place + '/' + o[i] + h3m_o
            #code mentése 
            codem = open('templates/Other/'+fname, 'x')
            codem.write(code)
            codem.close()

            p1m = open('Python_minták/1.pmint', 'r')
            p1m_o = p1m.read()

            p2m = open('Python_minták/2.pmint', 'r')
            p2m_o = p2m.read()

            p3m = open('Python_minták/3.pmint', 'r')
            p3m_o = p3m.read()

            p4m = open('Python_minták/4.pmint', 'r')
            p4m_o = p4m.read()

            m = HNo + i 
            sz = str(m)
            defek = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            codep = p1m_o + "'/" + name_o  + "'" + p2m_o + defek  + p3m_o + "'" + hom + fname +  "'" + p4m_o + "\n"*3

            codepm = open('app.py', 'a')
            codepm.write(codep)
            codepm.close()

            k = omo + '/' + name_o 
            shutil.move(k, filo_end_place)
    serv_runner()


#<<<Documentumok>>>
rd = open('dat/Documents.dat', 'r')
rdc = rd.read()

dc = (listToString(d))

print(dc, rdc)

if dc == rdc:
    print('Document:End')
elif dc != rdc:
    SERCON()
    for i in range(len(de)):
        if searchd(d, de[i]):
            print('ez az')
    print('Document:Generat')
    wd = open('dat/Documents.dat', 'w')
    wd.write(dc)
    for i in range(len(d)):
	
        name_d = d[i]
        kiter ='.html'
        fname = (name_d+kiter)
        
        

        if name_d == listToString(fnmatch.filter(os.listdir('static/Function/Documents'), "*.pdf")):
            print('pdf')
            SERCON()

            h0m = open('Html_minták/Documents/Pdf/0.hmint')
            h0m_o = h0m.read()

            h1m = open('Html_minták/Documents/Pdf/1.hmint')
            h1m_o = h1m.read()

            h2m = open('Html_minták/Documents/Pdf/2.hmint')
            h2m_o = h2m.read()

            code = h0m_o + name_d + h1m_o + '../../' + fild_end_place + '/' + d[i] + h2m_o

            codem = open('templates/Documents/'+fname, 'x')
            codem.write(code)
            codem.close()

            p1m = open('Python_minták/1.pmint', 'r')
            p1m_o = p1m.read()

            p2m = open('Python_minták/2.pmint', 'r')
            p2m_o = p2m.read()

            p3m = open('Python_minták/3.pmint', 'r')
            p3m_o = p3m.read()

            p4m = open('Python_minták/4.pmint', 'r')
            p4m_o = p4m.read()

            m = HNd + i 
            sz = str(m)
            defek = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            codep = p1m_o + "\"/" + name_d + "\"" + p2m_o + defek + p3m_o + "\"" + hdm + fname + "\"" + p4m_o + "\n"*3

            codepm = open('app.py', 'a')
            codepm.write(codep)
            codepm.close()

            k = dmo+ '/' + name_d
            shutil.move(k, fild_end_place)

            


        elif name_d != listToString(fnmatch.filter(os.listdir('static/Function/Documents'), "*.pdf")): 

            SERCON()

            h0m = open('Html_minták/Other/0.hmint', 'r')
            h0m_o = h0m.read()

            h1m = open('Html_minták/Other/1.hmint')
            h1m_o = h1m.read()

            h2m = open('Html_minták/Other/2.hmint')
            h2m_o = h2m.read()

            h3m = open('Html_minták/Other/3.hmint')
            h3m_o = h3m.read()

            code = h0m_o + name_d + h1m_o + '../../' + fild_end_place + '/' + d[i] + h2m_o + '../../' + fild_end_place + '/' + d[i] + h3m_o
            
            codem = open('templates/Documents/'+fname, 'x')
            codem.write(code)
            codem.close()

            p1m = open('Python_minták/1.pmint', 'r')
            p1m_o = p1m.read()

            p2m = open('Python_minták/2.pmint', 'r')
            p2m_o = p2m.read()

            p3m = open('Python_minták/3.pmint', 'r')
            p3m_o = p3m.read()

            p4m = open('Python_minták/4.pmint', 'r')
            p4m_o = p4m.read()

            m = HNd + i
            sz = str(m)
            defek = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            codep = p1m_o + "\"/" + name_d + "\"" + p2m_o +  defek + p3m_o + "\"" + hdm + fname + "\"" + p4m_o + "\n"*3

            codepm = open('app.py', 'a')
            codepm.write(codep)
            codepm.close()

            k = dmo + '/' + name_d
            shutil.move(k, fild_end_place)

    serv_runner()

#<<<Macro>>>
#<<<Video>>>
wven = open('dat/End_video.dat', 'r')
wven_o = wven.read()

rv = open('dat/Video.dat', 'r')
rvc = rv.read()

if wven_o != rvc:
    q = 'static/Function_end/Video'
    ede = 'templates/Video/'
    edee = os.listdir(q)
    edem = os.listdir('Html_minták/Makro/Video/dat/')

    direc = 'templates/Video/'
    vm = os.listdir(direc)

    f1 = open('Html_minták/Makro/Video/main_videó_1.htmltöredék', 'r')
    f1_o = f1.read()
    f1.close()

    f2 = open('Html_minták/Makro/Video/main_videó_2.htmltöredék', 'r')
    f2_o = f2.read()
    f2.close()

    m = open('Html_minták/Makro/Video/dat/generalt_methode.tmcs', 'w+')
    for i in range(len(edee)):
        hname = edee[i]
        dcode = f1_o + "/" + hname + "\">" + hname + f2_o + "\n"
        m.write(dcode)

    m.close()

    h1 = open('Html_minták/Makro/Video/htmltöredék1.mcs', 'r')
    h1_o = h1.read()
    h1.close()

    h2 = open('Html_minták/Makro/Video/dat/generalt_methode.tmcs', 'r')
    h2_o = h2.read()
    h2.close()

    h3 = open('Html_minták/Makro/Video/htmltöredék2.mcs', 'r')
    h3_o = h3.read()
    h3.close 

    html_w = open('templates/Main/Video/Video.html', 'w')
    hcode = h1_o + h2_o + h3_o
    html_w.write(hcode)
    html_w.close()

    wv = open('dat/Video.dat', 'w')
    wv.write(vc)
    wv.close()

#<<<other>>>

woen = open('dat/End_other.dat', 'r')
woen_o = woen.read()

ro = open('dat/other.dat', 'r')
roc = rv.read()

if woen_o != roc:
    q = 'static/Function_end/Other'
    ede = 'templates/Other/'
    edee = os.listdir(q)
    edem = os.listdir('Html_minták/Makro/other/dat/')

    direc = 'templates/Other/'
    vm = os.listdir(direc)

    f1 = open('Html_minták/Makro/other/main_videó_1.htmltöredék', 'r')
    f1_o = f1.read()
    f1.close()

    f2 = open('Html_minták/Makro/other/main_videó_2.htmltöredék', 'r')
    f2_o = f2.read()
    f2.close()

    m = open('Html_minták/Makro/other/dat/generalt_methode.tmcs', 'w+')
    for i in range(len(edee)):
        hname = edee[i]
        dcode = f1_o + "/" + hname + "\">" + hname + f2_o + "\n"
        m.write(dcode)

    m.close()

    h1 = open('Html_minták/Makro/other/htmltöredék1.mcs', 'r')
    h1_o = h1.read()
    h1.close()

    h2 = open('Html_minták/Makro/other/dat/generalt_methode.tmcs', 'r')
    h2_o = h2.read()
    h2.close()

    h3 = open('Html_minták/Makro/other/htmltöredék2.mcs', 'r')
    h3_o = h3.read()
    h3.close 

    html_w = open('templates/Main/Other/Index.html', 'w')
    hcode = h1_o + h2_o + h3_o
    html_w.write(hcode)
    html_w.close()

    wv = open('dat/Other.dat', 'w')
    wv.write(oc)
    wv.close()

#<<Docments>>
wden = open('dat/End_documents.dat', 'r')
wden_o = wden.read()
wden.close()


rd = open('dat/Documents.dat', 'r')
rdc = rd.read()
rd.close()


if (wden_o != rdc):
    q = 'static/Function_end/Documents'
    ede = 'templates/Documents/'
    edee = os.listdir(q)
    edem = os.listdir('Html_minták/Makro/documents/dat/')

    direc = 'templates/Documents/'
    vm = os.listdir(direc)

    f1 = open('Html_minták/Makro/documents/main_videó_1.htmltöredék', 'r')
    f1_o = f1.read()
    f1.close()

    f2 = open('Html_minták/Makro/documents/main_videó_2.htmltöredék', 'r')
    f2_o = f2.read()
    f2.close()
    
    

    m = open('Html_minták/Makro/documents/dat/general_methode.tmcs', 'w+')
    for i in range(len(edee)):
        hname = edee[i]
        dcode = f1_o + "/" + hname + "\">" + hname + f2_o + "\n"
        m.write(dcode)

    m.close()

    h1 = open('Html_minták/Makro/documents/htmltöredék1.mcs', 'r')
    h1_o = h1.read()
    h1.close()

    h2 = open('Html_minták/Makro/documents/dat/general_methode.tmcs', 'r')
    h2_o = h2.read()
    h2.close()

    h3 = open('Html_minták/Makro/documents/htmltöredék2.mcs', 'r')
    h3_o = h3.read()
    h3.close 

    html_w = open('templates/Main/Documents/Index.html', 'w')
    hcode = h1_o + h2_o + h3_o
    html_w.write(hcode)
    html_w.close()

    wv = open('dat/Documents.dat', 'w')
    wv.write(dc)
    wv.close()
    print(dc)