from appJar import gui
l=[]
def press(btn):
	if btn=="Abbrechen":
		welcome.stop()
	elif btn=="Scan":
		welcome.hide(welcome)
		welcome.showSubWindow("OpenFile")
		
def press2(btn):
	if btn=="Abbrechen2":
		welcome.stop()
	elif btn=="Zurueck":
		welcome.hideSubWindow("OpenFile")
		welcome.show(welcome)
	elif btn=="Datei hinzufuegen":
		l.append(welcome.openBox("Bibliothek waehlen", parent="OpenFile"))
		datei=l[0]
		if datei[-1]=="b" and datei[-2]=="i" and datei[-3]=="b" and datei[-4]==".":
			welcome.hideSubWindow("OpenFile")
			welcome.showSubWindow("ISBN")
		else:
			del l[0]
			welcome.hideSubWindow("OpenFile")
			welcome.showSubWindow("FehlerDatei")
			
			
def pressFehlerDatei(btn):
	if btn=="Bestaetigen":
		welcome.hideSubWindow("FehlerDatei")
		welcome.showSubWindow("OpenFile")

def pressISBN(btn):
	if btn=="OK":
		l.append(int(welcome.getEntry("ISBN")))
		print(l)
		isbn=l[1]
		if len(str(isbn))!=10 and len(str(isbn))!=13:
			del l[1]
			welcome.hideSubWindow("ISBN")
			welcome.showSubWindow("FehlerISBN")
			print(len(str(isbn)))
		else:
			welcome.hideSubWindow("ISBN")
			welcome.showSubWindow("Abgeschlossen")
	elif btn=="Abbrechen3":
		welcome.stop()		
				
def pressFehlerISBN(btn):
	if btn=="BestaetigenISBN":
		welcome.hideSubWindow("FehlerISBN")
		welcome.showSubWindow("ISBN")




welcome=gui("Willkommen bei **", "720X540")
welcome.setFont(size=20, family="Comic Sans")
welcome.showSplash("*Name einfuegen*", fill='black', stripe='black', fg='white', font=40)
welcome.addLabel("title", "Willkommen!")
welcome.addButtons(["Scan", "Abbrechen"], press)



welcome.startSubWindow("OpenFile", "Datei auswaehlen", modal=True)
welcome.addLabel("l1", "Bibliotheksdatei auswaehlen")
welcome.addButtons(["Datei hinzufuegen", "Zurueck"], press2)
welcome.addNamedButton("Abbrechen", "Abbrechen2", press2)
welcome.setSize(720, 540)
welcome.stopSubWindow()	

welcome.startSubWindow("ISBN", "ISBN scnannen")
welcome.addLabelNumericEntry("ISBN")
welcome.addButtons(["OK"], pressISBN)
welcome.addNamedButton("Abbrechen", "Abbrechen3", pressISBN)
#Noch Einbauen, dass Eintrag gecleart wird, wenn man zum Fehler geht und wieder zurueck.
welcome.stopSubWindow()

welcome.startSubWindow("FehlerDatei", "Ein Fehler ist aufgetreten!", modal=True)
welcome.addLabel("l2", "Bitte ueberpruefen sie, ob sie eine Bibliotheksdatei des Typs *.bib* ausgewaehlt haben und versuchen sie es erneut!")
welcome.addButtons(["Bestaetigen"], pressFehlerDatei)
welcome.stopSubWindow()

welcome.startSubWindow("FehlerISBN", "Ein Fehler ist aufgetreten!", modal=True)
welcome.addLabel("l3", "Inkorrekte ISBN-Eingabe. Eine ISBN muss entweder 10 oder 13 Ziffern lang sein.")
welcome.addNamedButton("Bestaetigen", "BestaetigenISBN", pressFehlerISBN)
welcome.stopSubWindow()

welcome.startSubWindow("Abgeschlossen", "Vorgang abgeschlossen!", modal=True)
welcome.addLabel("l4", "Vorgang abgeschlossen") 
welcome.stopSubWindow()

welcome.go()


