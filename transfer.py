import smtplib # SMTP-Bibliothek zum Versenden der Mail
import mimetypes # Mimtype-Bibliothek, Zuordnung von Dateien zu MIME types (Dateitypen, -endungen)
from email.message import EmailMessage # E-Mail-Bibliothek, zum Erstellen von versandfähigen E-Mails
import os # OS-Bibliothek
import logging # Logging-Bibliothek
from folder import * # Import der Klasse folder

class transfer():     

    def sendMail(pSubject, pFrom, pTo, pContent, pFile, filename, host, username, password): # Definition der Methode zum Versenden der E-Mails
  
        folder.compress(pFile) # Komprimierung der zu versendenden Datei/Ordner
        pZip = pFile + '.zip' # Vervollständigung des Dateipfads der .zip
        msg = EmailMessage() # Erstellung der E-Mail
        msg['Subject'] = pSubject #Hinzufügen Betreff
        msg['From'] = pFrom # Hinzufügen Absender
        msg['To'] = pTo # Hinzufügen Empfänger
        msg.set_content(pContent) # Inhalt der Mail
            
        try:
            with open(pZip, 'rb') as fp: # Öffnen der zu versendenden Datei
                file_data = fp.read()
                maintype, _, subtype = (mimetypes.guess_type(pZip)[0] or 'application/octet-stream').partition("/") # Auslesen des MIME Types (Dateityp)
                msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename) # Anhängen der Datei an die E-Mail
                
        except Exception as e:
            logging.error(e) # Logging potentieller Fehlermeldung
                
        try:
            s = smtplib.SMTP(host) # SMTP-URL
            s.starttls() # Start des TLS-Verschlüsselungsprotokolls
            s.login(username, password) # Anmeldung mit Benutzernamen und Passwort
            s.send_message(msg) # Versenden der Nachricht
            s.quit() # Schließen des SMTP-Vorgangs
            folder.delFolder(pFile) # Löschen des Transferordners
            os.remove(pZip) # Löschen der .zip-Datei
        except Exception as e:
            logging.error(e) # Logging potentieller Fehlermeldung
            if os.path.exists(pZip):
                os.remove(pZip)
            
    def sendMessage(pSubject, pFrom, pTo, pContent, host, username, password):       

        msg = EmailMessage() # Erstellung der E-Mail
        msg['Subject'] = pSubject #Hinzufügen Betreff
        msg['From'] = pFrom # Hinzufügen Absender
        msg['To'] = pTo # Hinzufügen Empfänger
        msg.set_content(pContent) # Inhalt der Mail
          
        try:
            s = smtplib.SMTP(host) # SMTP-URL
            s.starttls() # Start des TLS-Verschlüsselungsprotokolls
            s.login(username, password) # Anmeldung mit Benutzernamen und Passwort
            s.send_message(msg) # Versenden der Nachricht
            s.quit() # Schließen des SMTP-Vorgangs
        except Exception as e:
            logging.error(e) # Logging potentieller Fehlermeldung

            
            

