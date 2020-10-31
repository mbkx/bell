# -*- coding: utf-8 -*-
from isbnlib import *
from appJar import gui
import serial.tools.list_ports 
import serial
from configparser import ConfigParser
l=[]
standardverzeichnis=[]
#INI-Datei
ini='scan.ini'
config = ConfigParser()
config.read(ini)

#Scannerliste
scannerliste=([comport.device for comport in serial.tools.list_ports.comports()])

#Scanner
if (config['scannerklasse']['scanner'] in scannerliste) == True:	
	scanner=config['scannerklasse']['scanner']
else:
	scanner="---"
print scanner


#Buttons
#Hauptmenübutton
def pressHauptmenu(btn):
	if btn=="Abbrechen":
		bell.stop()
	if btn=="Bibliotheksdatei":
		bell.hide("Hauptmenu")
		bell.showSubWindow("Bib")	
	if btn=="ISBN":
		#schauen, ob Scanner verbunden ist
		if scanner=="---":	
			bell.hide("Hauptmenu")
			bell.showSubWindow("Isbn")
		else:
			bell.hide("Hauptmenu")
			bell.showSubWindow("IsbnScan")
	if btn=="Fortfahren":
		if bell.yesNoBox("Fortfahren", "Wollen Sie diese Daten übermitteln?", parent=None)==True:
			l.append(bell.stringBox("Bibtexkey eingeben", "Bitte geben Sie den Bibtexkey ein. Dieser wird in Latex verwendet um das Werk zu ziteren."))
			bell.infoBox("Erfolgreich", "Sie haben Ihre Daten erfolgreich übermittelt. Ihr Buch wurde im Literaturverzeichnis hinzugefügt", parent=None)
			bell.stop() 
	if btn=="Einstellungen":
		bell.hide("Hauptmenu")
		bell.showSubWindow("Einstellungen")

#Einstellungen
def pressEinstellungen(btn):
	if btn=="Standardverzeichnis":
		standardverzeichnis=[]
		standardverzeichnis.append(str((bell.directoryBox("Standardverzeichnisauswählen", parent="Einstellungen"))))
		if standardverzeichnis[-1]== "None" or standardverzeichnis[-1]== "()":
			standardverzeichnis=[]
	if btn=="ZurückEinstellungen":
		bell.hideSubWindow("Einstellungen")
		bell.show("Hauptmenu")
	if btn=="Credits":
		bell.hideSubWindow("Einstellungen")
		bell.showSubWindow("Credits")
	if btn=="Hilfe":
		bell.hideSubWindow("Einstellungen")
		bell.showSubWindow("Hilfe")
	if btn=="ZurückEinstellungen":
		bell.hideSubWindow("Einstellungen")
		bell.show("Hauptmenu")
	if btn=="Scanner":
		bell.hideSubWindow("Einstellungen")
		bell.showSubWindow("Scanner")
		
		
		
#Bib-Button
def pressBib(btn):
	if btn=="Zurück":
		bell.hideSubWindow("Bib")
		bell.show("Hauptmenu")
	elif btn=="Datei hinzufügen":

		#noch keine Datei
			if l==[] or str(l[0])=='' or str(l[0])==(): 
				if len(l)>0:
					if l[0]==u'' or l[0]==():
						del l[0]
				#Schauen, ob standardverzeichnis in Einstellungen festgelegt ist
				if standardverzeichnis != []:	
					l.insert(0, bell.openBox("Bibliothek waehlen", dirName=standardverzeichnis[-1], fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
				else:
					l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
				if len(l[0])>=4:	
					bell.hideSubWindow("Bib")
					bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt", parent="Bib")
					bell.show("Hauptmenu")
				else:
					del l[0]
		#noch keine Bib-Datei, aber ISBN
			elif str(l[0])[-1]!="b" and str(l[0])[-2]!="i" and str(l[0])[-3]!="b" and str(l[0])[-4]!=".":
				#Schauen, ob standardverzeichnis in Einstellungen festgelegt ist
				if standardverzeichnis != []:	
					l.insert(0, bell.openBox("Bibliothek waehlen", dirName=standardverzeichnis[-1], fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
				else:
					l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
				if len(l[0])>=4:	
					bell.hideSubWindow("Bib")
					bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt", parent="Bib")
					bell.enableButton("Fortfahren")
					bell.show("Hauptmenu")
				else:
					del l[0]


		#Wenn NUR Bib-Datei angefügt		
			elif str(l[0])[-1]=="b" and str(l[0])[-2]=="i" and str(l[0])[-3]=="b" and str(l[0])[-4]=="." and len(l)==1:
				if bell.yesNoBox("Bibliotheksdatei überschreiben", "Wollen Sie die Bibliotheksdatei überschreiben?", parent="Bib")==True:
					#Schauen, ob standardverzeichnis in Einstellungen festgelegt ist
					if standardverzeichnis != []:	
						l.insert(0, bell.openBox("Bibliothek waehlen", dirName=standardverzeichnis[-1], fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
					else:
						l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
					del l[1]
					bell.hideSubWindow("Bib")
					bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt.", parent="Bib")
					bell.show("Hauptmenu")
				else:
					bell.showSubWindow("Bib")

		#Wenn schon ISBN UND Bib-Datei:
			#elif str(l[0])[-1]=="b" and str(l[0])[-2]=="i" and str(l[0])[-3]=="b" and str(l[0])[-4]=="." and len(l)==2:
			elif len(l)==2:
				if bell.yesNoBox("Bibliotheksdatei überschreiben", "Wollen Sie die Bibliotheksdatei überschreiben?", parent="Bib")==True:
					#Schauen, ob standardverzeichnis in Einstellungen festgelegt ist
					if standardverzeichnis != []:	
						l.insert(0, bell.openBox("Bibliothek waehlen", dirName=standardverzeichnis[-1], fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
					else:
						l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))	
					del l[1]
					bell.hideSubWindow("Bib")
					bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt.", parent="Bib")
					bell.enableButton("Fortfahren")
					bell.show("Hauptmenu")
				else:
					bell.showSubWindow("Bib")
						
					

#ISBN-Button
def pressIsbn(btn):
	if btn=="OK":
		#Checken, ob Eingabe ISBN ist.
		isbn=canonical(bell.getEntry("Isbn"))
		if len(isbn)==10:
			isbn= to_isbn13(isbn)
		if is_isbn13(isbn)==True:
			#nichts
			if l==[]:
				l.append(isbn)
				bell.hideSubWindow("Isbn")
				bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="Isbn")
				bell.show("Hauptmenu")
			#nur Bib
			elif l[0][-1]=="b" and l[0][-2]=="i" and l[0][-3]=="b" and l[0][-4]=="." and len(l)==1:
				l.append(isbn)
				bell.enableButton("Fortfahren")
				bell.hideSubWindow("Isbn")
				bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="Isbn")
				bell.show("Hauptmenu")
			#nur ISBN
			elif len(l)==1 and l[0][-1]!="b" and l[0][-2]!="i" and l[0][-3]!="b" and l[0][-4]!=".":
				if bell.yesNoBox("ISBN überschreiben", "Wollen Sie die ISBN überschreiben?", parent="Isbn")==True:	
					del l[0]
					l.append(isbn)
					bell.hideSubWindow("Isbn")
					bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="Isbn")
					bell.show("Hauptmenu")
			#beides
			elif len(l)==2:
				if bell.yesNoBox("ISBN überschreiben", "Wollen Sie die ISBN überschreiben?", parent="Isbn")==True:	
					del l[1]
					l.append(isbn)
					bell.enableButton("Fortfahren")
					bell.hideSubWindow("Isbn")
					bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="Isbn")
					bell.show("Hauptmenu")
		
		else:
			bell.errorBox("Fehler", "Es ist ein Fehler aufgetreten!" +  "\n" + "Bitte überprüfen Sie die ISBN und versuchen Sie es erneut.", parent="Isbn")	
			
			
	elif btn=="ZurückIsbn":
		bell.hideSubWindow("Isbn")
		bell.show("Hauptmenu")

#ISBN-Scan-Button:
def pressIsbnScan(btn):
	if btn=="Scannen":
		#print scanner
		ser=serial.Serial(scanner)
		isbn=ser.read(13)
		#print isbn
		#Checken, ob Eingabe ISBN ist.
		#isbn=canonical(ser.read(13))
		if is_isbn13(isbn)==True:
			#nichts
			if l==[]:
				l.append(isbn)
				bell.hideSubWindow("IsbnScan")
				bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="IsbnScan")
				bell.show("Hauptmenu")
			#nur Bib
			elif l[0][-1]=="b" and l[0][-2]=="i" and l[0][-3]=="b" and l[0][-4]=="." and len(l)==1:
				l.append(isbn)
				bell.enableButton("Fortfahren")
				bell.hideSubWindow("IsbnScan")
				bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="IsbnScan")
				bell.show("Hauptmenu")
			#nur ISBN
			elif len(l)==1 and l[0][-1]!="b" and l[0][-2]!="i" and l[0][-3]!="b" and l[0][-4]!=".":
				if bell.yesNoBox("ISBN überschreiben", "Wollen Sie die ISBN überschreiben?", parent="IsbnScan")==True:	
					del l[0]
					l.append(isbn)
					print l
					bell.hideSubWindow("IsbnScan")
					bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="IsbnScan")
					bell.show("Hauptmenu")
			#beides
			elif len(l)==2:
				if bell.yesNoBox("ISBN überschreiben", "Wollen Sie die ISBN überschreiben?", parent="IsbnScan")==True:	
					del l[1]
					l.append(isbn)
					bell.enableButton("Fortfahren")
					bell.hideSubWindow("IsbnScan")
					bell.infoBox("Erfolgreich", "Sie haben Ihre ISBN erfolgreich hinzugefügt.", parent="IsbnScan")
					bell.show("Hauptmenu")
		
		else:
			bell.errorBox("Fehler", "Es ist ein Fehler aufgetreten!" +  "\n" + "Bitte überprüfen Sie die ISBN und versuchen Sie es erneut.", parent="Isbn")	
	
	if btn=="ZurückIsbnScan":
		bell.hideSubWindow("IsbnScan")
		bell.show("Hauptmenu")

#Credits-Button
def pressCredits(btn):
	if btn=="OKCredits":
		bell.hideSubWindow("Credits")
		bell.showSubWindow("Einstellungen")
		
#Hilfe-Link
def HilfeLink(link):
	bell.infoBox("Was ist Isbn2BibTeX?", "Isbn2BibTeX ist ein Programm, welches entwickelt wurde, um die ISBN von Büchern einzuscannen und diese, samt Metadaten, automatisch dem Literaturverzeichnis einer LaTeX-Datei hinzuzufügen.")

#Hilfe-Button
def pressHilfe(btn):
	if btn=="OKHilfe":
		bell.hideSubWindow("Hilfe")
		bell.showSubWindow("Einstellungen")
				
#Scanner-Button
def pressScanner(btn):
	if btn=="OKScanner":
		global scanner
		scannerDesc=bell.getListBox("Scanner")[0]
		print scannerDesc
		for dev in scannerliste:
			if (dev in scannerDesc) == True:
				scanner=dev
				#INI setzen
				config.set('scannerklasse', 'scanner', scanner)
				with open(ini, "w") as configfile:
					config.write(configfile)
			else:
				scanner="---"
		bell.hideSubWindow("Scanner")
		bell.showSubWindow("Einstellungen")
					
				
#Hauptmenu
bell=gui("Hauptmenu", "800X200")
bell.setResizable("False")
bell.setStretch("Couluomn")
bell.setSticky("ew")
bell.setFont(size=12, family="Sans Serif")
#bell.showSplash("*Name einfuegen*", fill='black', stripe='black', fg='white', font=40)
bell.addLabel("titel", "Willkommen bei der BETA von ISBN2BibTeX!")
bell.getLabelWidget("titel").config(font=("Sans Serif", "20", "bold"))
bell.setStretch("None")
bell.addLabel("untertitel1", "Wählen Sie eine Bibliotheksdatei aus und")
bell.addLabel("untertitel2", "scannen Sie eine ISBN ein, um dieses Buch zu ihrem Literaturverzeichnis hinzuzufügen.")
bell.setStretch("both")
bell.addButtons(["Bibliotheksdatei", "ISBN", "Einstellungen", "Abbrechen"], pressHauptmenu)
bell.addButton("Fortfahren", pressHauptmenu)
bell.disableButton("Fortfahren")


#Bibliotheksdatei
bell.startSubWindow("Bib", "Bibliotheksdatei", transient=True, modal=True)
bell.setStretch("None")
bell.addLabel("l1Bib", "Bibliotheksverzeichnis auswählen")
bell.getLabelWidget("l1Bib").config(font=("Sans Serif", "14", "bold"))
bell.addLabel("l2Bib", "Bitte wählen sie ein")
bell.addLabel("l3Bib", "Literaturverzeichnis des Typs .bib aus")
bell.setStretch("both")
bell.addButtons(["Datei hinzufügen", "Zurück"], pressBib)
bell.setSize(400, 150)
bell.stopSubWindow()	

#ISBN auswählen (ohne Scanner)
bell.startSubWindow("Isbn", "ISBN", modal=True)
bell.setStretch("none")
bell.addLabel("l1Isbn", "ISBN eingeben")
bell.getLabelWidget("l1Isbn").config(font=("Sans Serif", "14", "bold"))
bell.addLabel("l2Isbn", "Bitte geben Sie die ISBN manuell ein.")
bell.addLabel("l3Isbn", "Beachten Sie, dass eine ISBN 10 oder 13 Ziffern enthält.")
bell.setStretch("both")
bell.addEntry("Isbn")
bell.addButton("OK", pressIsbn)
bell.addNamedButton("Zurück", "ZurückIsbn", pressIsbn)
bell.stopSubWindow()

#ISBN (mit Scanner)
bell.startSubWindow("IsbnScan", "ISBN mit Scanner", modal=True)
bell.setSize(400, 400)
bell.addLabel("l1IsbnScan", "ISBN scannen")
bell.getLabelWidget("l1IsbnScan").config(font=("Sans Serif", "14", "bold"))
bell.addLabel("l2IsbnScan", "ISBN mit Scanner eingeben.")
bell.addButton("Scannen", pressIsbnScan)
bell.addNamedButton("Zurück", "ZurückIsbnScan", pressIsbnScan)
bell.stopSubWindow()

#Einstellungen
bell.startSubWindow("Einstellungen", "Einstellungen", modal=True)
bell.setStretch("both")
bell.setSize(400, 400)
bell.addLabel("l1Einstellungen", "Einstellungen")
bell.getLabelWidget("l1Einstellungen").config(font=("Sans Serif", "14", "bold"))
bell.addButton("Hilfe", pressEinstellungen)##DONE
bell.addButton("Standardverzeichnis", pressEinstellungen) ##DONE
bell.addButton("Credits", pressEinstellungen) ##DONE
bell.addButton("Scanner", pressEinstellungen)
bell.addNamedButton("Zurück", "ZurückEinstellungen", pressEinstellungen)##DONE
bell.stopSubWindow()

#Credits
bell.startSubWindow("Credits", "Credits", modal=True)
bell.setStretch("both")
bell.setSize(600, 250)
bell.addLabel("l1Credits", "Credits")
bell.getLabelWidget("l1Credits").config(font=("Sans Serif", "14", "bold"))
bell.addLabel("l2Credits", "Isbn2BibTeX wird als Besondere Lernleistung (BeLL) entwickelt.")
bell.addLabel("l3Credits", "von Mika Miosge")
bell.addLabel("l4Credits", "Außenbetreuer: Stephan Keller")
bell.addLabel("l5Credits", "Innenbetreuer: Matthias Richter")
bell.addNamedButton("OK", "OKCredits", pressCredits)
bell.stopSubWindow()

#Hilfe
bell.startSubWindow("Hilfe", "Hilfe", modal=True)
bell.setStretch("both")
bell.setSize(600, 250)
bell.addLabel("l1Hilfe", "Hilfe")
bell.getLabelWidget("l1Hilfe").config(font=("Sans Serif", "14", "bold"))
bell.addLink("Was macht Isbn2BibTeX?", HilfeLink)
bell.addWebLink("Was ist BibTeX?", "https://de.wikipedia.org/wiki/BibTeX")
bell.addWebLink("Was ist eine ISBN?", "https://de.wikipedia.org/wiki/Internationale_Standardbuchnummer")
bell.addNamedButton("OK", "OKHilfe", pressHilfe)
bell.stopSubWindow()

#Scanner
bell.startSubWindow("Scanner", "Scanner auswählen", modal=True)
bell.setStretch("coloumn")
bell.setSize(300, 250)
bell.addLabel("l1Scanner", "Scanner auswählen.")
bell.addListBox("Scanner", ["---"])
scannercounter=0
if 	scannerliste != []:
	for device in scannerliste:	
		scannerOut=""
		scannerOutListe=([comport.device for comport in serial.tools.list_ports.comports()])
		scannerOutListe.append([comport.product for comport in serial.tools.list_ports.comports()])
		scannerOutListe.append([comport.manufacturer for comport in serial.tools.list_ports.comports()])
		scannerOut+=scannerOutListe[scannercounter]
		scannerOut+=": " + scannerOutListe[-2][scannercounter] + " (" + scannerOutListe[-1][scannercounter] + ")"
		bell.addListItem("Scanner", scannerOut)
		scannercounter+=1
bell.addNamedButton("OK", "OKScanner", pressScanner)
bell.stopSubWindow()


bell.go()


#testISBN: 3551555559 (harry potter und der orden des phönix)
#9783551551672 (harry potter und der stein der weisen)
