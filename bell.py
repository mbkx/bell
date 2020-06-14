# -*- coding: utf-8 -*-
from isbnlib import *
from appJar import gui
l=[]

#Buttons
#Hauptmenübutton
def pressHauptmenu(btn):
	if btn=="Abbrechen":
		bell.stop()
	if btn=="Bibliotheksdatei":
		bell.hide("Hauptmenu")
		bell.showSubWindow("Bib")
	if btn=="ISBN":
		bell.hide("Hauptmenu")
		bell.showSubWindow("Isbn")
	if btn=="Fortfahren":
		if bell.yesNoBox("Fortfahren", "Wollen Sie diese Daten übermitteln?", parent=None)==True:
			l.append(bell.stringBox("Bibtexkey eingeben", "Bitte geben Sie den Bibtexkey ein. Dieser wird in Latex verwendet um das Werk zu ziteren."))
			bell.infoBox("Erfolgreich", "Sie haben Ihre Daten erfolgreich übermittelt. Ihr Buch wurde im Literaturverzeichnis hinzugefügt", parent=None)
			bell.stop() 
		
		
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
			l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
			if len(l[0])>=4:	
				bell.hideSubWindow("Bib")
				bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt", parent="Bib")
				bell.show("Hauptmenu")

	#noch keine Bib-Datei, aber ISBN
		elif str(l[0])[-1]!="b" and str(l[0])[-2]!="i" and str(l[0])[-3]!="b" and str(l[0])[-4]!=".":
			l.insert(0, bell.openBox("Bibliothek waehlen", fileTypes=[('Bibliothek', '*.bib')],parent="Bib"))
			if len(l[0])>=4:	
				bell.hideSubWindow("Bib")
				bell.infoBox("Erfolgreich", "Sie haben Ihr Literaturverzeichnis erfolgreich hinzugefügt", parent="Bib")
				bell.enableButton("Fortfahren")
				bell.show("Hauptmenu")


	#Wenn NUR Bib-Datei angefügt		
		elif str(l[0])[-1]=="b" and str(l[0])[-2]=="i" and str(l[0])[-3]=="b" and str(l[0])[-4]=="." and len(l)==1:
			if bell.yesNoBox("Bibliotheksdatei überschreiben", "Wollen Sie die Bibliotheksdatei überschreiben?", parent="Bib")==True:
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


	
				
				
#Hauptmenu
bell=gui("Hauptmenu", "800X200")
bell.setResizable("False")
bell.setStretch("Couluomn")
bell.setSticky("ew")
bell.setFont(size=12, family="Sans Serif")
#bell.showSplash("*Name einfuegen*", fill='black', stripe='black', fg='white', font=40)
bell.addLabel("titel", "Willkommen bei **!")
bell.getLabelWidget("titel").config(font=("Sans Serif", "20", "bold"))
bell.setStretch("None")
bell.addLabel("untertitel1", "Wählen Sie eine Bibliotheksdatei aus und")
bell.addLabel("untertitel2", "scannen Sie eine ISBN ein, um dieses Buch zu ihrem Literaturverzeichnis hinzuzufügen.")
bell.setStretch("both")
bell.addButtons(["Bibliotheksdatei", "ISBN", "Abbrechen"], pressHauptmenu)
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

#ISBN auswählen
bell.startSubWindow("Isbn", "ISBN", modal=True)
bell.setStretch("none")
bell.addLabel("l1Isbn", "ISBN scannen")
bell.getLabelWidget("l1Isbn").config(font=("Sans Serif", "14", "bold"))
bell.addLabel("l2Isbn", "Bitte scannen Sie eine ISBN oder geben sie diese manuell ein.")
bell.addLabel("l3Isbn", "Beachten Sie, dass eine ISBN 10 oder 13 Ziffern enthält.")
bell.setStretch("both")
bell.addEntry("Isbn")
bell.addButton("OK", pressIsbn)
bell.addNamedButton("Zurück", "ZurückIsbn", pressIsbn)
bell.stopSubWindow()
	


bell.go()


#testISBN: 3551555559 (harry potter und der orden des phönix)
#9783551551672 (harry potter und der stein der weisen)
