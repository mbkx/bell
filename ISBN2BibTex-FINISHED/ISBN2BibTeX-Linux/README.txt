#für die Benutzung mit Docker(-compose):
#entweder mit:
docker-compose up (starten)
docker-compose down (schließen)
#oder:
docker-compose run --rm isbn bash (im Terminal des Containers starten)

###Es kann ein Zugriffsfehler ("No protocol specified") auftritt. Dann muss
Docker mit dem Befehl "xhost +local:docker" zur xhost-Gruppe hinzugefügt werden.
