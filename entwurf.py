from appJar import gui
l=[]
def press(btn):
	if btn=="Abbruch":
		welcome.stop()
	elif btn=="Scan":
		welcome.hide(welcome)
		welcome.showSubWindow("OpenFile")
		
def press2(btn):
	if btn=="Abbrechen": #Aendern, dass die Varable auf die vom ersten zugreifen kann (identischer Name)
		welcome.stop()
	elif btn=="Zurueck":
		welcome.hideSubWindow("OpenFile")
		welcome.show(welcome)
	elif btn=="Datei hinzufuegen":
		l.append(welcome.directoryBox("Bibliothek waehlen", parent="OpenFile"))
		print(l)

welcome=gui("Willkommen bei **", "720X540")
welcome.setFont(size=20, family="Times")
welcome.addLabel("title", "Willkommen!")
welcome.addButtons(["Scan", "Abbruch"], press)



welcome.startSubWindow("OpenFile", "Datei auswaehlen", modal=True)
welcome.addLabel("l1", "Bibliotheksdatei auswaehlen")
welcome.addButtons(["Zurueck", "Datei hinzufuegen"], press2)
welcome.setSize(720, 540)
welcome.stopSubWindow()	



welcome.go()


