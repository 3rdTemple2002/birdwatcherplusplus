from picamera import PiCamera #Import des RaspberryPi-Camera Bibliothek
import logging #Import der Bibliothek zum Erstellen eines Logfiles
from time import sleep #Import der Time-Bibliothek für die Funktion sleep()

class camera():
    
    def takePhoto(pFile): #Definition der Methode takePhoto mit dem Paramter pFile (Speicherort des aufzunehmenden Fotos)
    
        try:
            camera = PiCamera() 
            camera.rotation =180 #Drehen des Kamerabildes um 180°
            camera.start_preview() #Start der Kamera
            sleep(2) #Warten (2 Sekunden), für die Lichtverhältnisse
            camera.capture(pFile) #Aufnahme des Fotos an den vorgegebenen Speicherort
            camera.stop_preview() #Stop der Kamera
            camera.close()
        except Exception as a:
            logging.error(a) #Logging, falls Exceptions auftreten
        
    
