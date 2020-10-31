###Importe festlegen und Codierung, sowie Variablen
# -*- coding: utf-8 -*-
from appJar import gui
from isbnlib import *
from isbnlib.registry import bibformatters
bibtex = bibformatters['bibtex']
l=[]

###gui ausführen und sich daraus ergebende Variablen festlegen
l.append(execfile("./bellSCAN.py"))
try:
	directory=l[0]
	#directory="/home/mika/Musik/test.bib" #--> test
	isbn=l[1]
	#isbn="978-3551080158" #-->test
	bibtexkey=l[2]
except:
	exit()


###Metadaten finden und in Bibtex bei Variable "matatext" speichern
if bibtex(meta(isbn, service="goob"))==None:
	try:
		metatext = bibtex(meta(isbn, service="openl"))
		###Metatext in Utf-8 codieren, da sonst Fehler auftreten könnten.
		metatext = metatext.encode("utf-8")
	except:
		try:
			metatext = bibtex(meta(isbn, service="wiki"))
			metatext = metatext.encode("utf-8")
		except:
			metatext="Fehler!"
else:
	metatext=bibtex(meta(isbn, service="goob"))
	metatext = metatext.encode("utf-8")

#Metatext modifizieren, so dass bibtexkey, der von Nutzer angegeben wurde verwendet werden kann.
if len(isbn)==10:
	isbn=to_isbn13(isbn)

metatext=metatext.replace(canonical(isbn), bibtexkey, 1) 



#wenn Infos empfangen wurden, werden sie der vom Nutzer angegebenen Bibdatei angehängt.
if metatext !=	"Fehler!":
	bibdatei=open(directory, mode = "a+")
	bibdatei.write(metatext + "\n")
else:
	print metatext
