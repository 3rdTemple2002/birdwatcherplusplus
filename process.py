from datetime import datetime # Import Datetime-Bibliothek, für den Umgang mit Daten und Zeiten
from folder import * # Import folder.py
from camera import * # Import camera.py
from transfer import * #Import transfer.py
import logging # Import Logging-Bibliothek zum Erstellen einer Logdatei

class Process():
        
    class __init__(): # Ausführung beim Programmaufruf
                                                                                                        # DD-MM-YYYY_HH-MM-SS
        time = datetime.now(  ).strftime("%Y-%m-%d_%H-%M-%S") # Erstellung der aktuell Uhrzeit im Format "03-10-2022_20-13-23"
        year = datetime.now().strftime("%Y") # Erstellung des Jahres als Text
        month = datetime.now().strftime("%m-%Y") # Erstellung des Monates und Jahres als Text
        path1 = '/home/pi/Desktop/Birdwatcher_pp' # Ordnerpfad 1
        path2 = '/home/pi/Desktop/Birdwatcher_pp/%s' %year #Ordnerpfad 2
        path3 = '/home/pi/Desktop/Birdwatcher_pp/%s/%s' % (year, month) # Ordnerpfad 3
        pFile = path3 +'/image_'+ time + '.jpg' #Dateipfad für die Aufnahme
        filename = time # Dateiname für den Mail-Versand
        
        pSubject = 'Vogelbeobachtung ' + time # Betreff der E-Mail
        pFrom = # Absenderadresse der Mail [zu ergänzen]
        pTo = # Empfaengeradresse [zu ergänzen]
        pContent = # E-Mailtext [zu ergänzen]
        host = # SMTP-Url des Mailproviders [zu ergänzen]
        username = # Benutzername des Mail-Kontos
        password = # Passwort des Mail-Kontos
        
        pTransfer = '/home/pi/Desktop/Birdwatcher_pp/transfer' # Ordnerpfad für den Transferordner

        logging.basicConfig(filename="process_log.txt", format="%(asctime)s %(message)s") # Erstellung und Konfiguration der Log-Datei
            
        folder.createFolder(path1) # Erstellung des Orners an Pfad 1
        folder.createFolder(path2) # Erstellung des Orners an Pfad 2
        folder.createFolder(path3) # Erstellung des Orners an Pfad 3
        folder.createFolder(pTransfer) # Erstellung des Hauptverzeichnis für den Transfer
             
        if(folder.get_size(path1) < 5000000000):

            camera.takePhoto(pFile) # Aufnahme und Speicherung unter dem Dateipfad
                    
            folder.transfer(pFile, pTransfer) # Kopieren der Aufnahme in den Transferordner

            folder.chop_dir(pTransfer,20000000)

            transfer_sub_dirs = os.listdir(pTransfer)
            transfer_sub_dirs.sort()
            #print(transfer_sub_dirs)
            for obj in transfer_sub_dirs:
                transfer.sendMail(pSubject, pFrom, pTo, pContent, pTransfer + '/' + obj, filename, host, username, password) # Versand der Datei per E-Mail in einer .zip-Datei
        else:
            
            transfer.sendMessage('Speicher voll', pFrom, pTo, 'Der Speicher muss geleert werden.', host, username, password)

