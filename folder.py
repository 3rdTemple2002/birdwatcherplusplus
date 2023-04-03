import os #Import OS-Bibliothek (Funktionen des Betriebssystems)
import logging #Import Logging-Bibliothek
import shutil #Import Shutil-Bibliothek (Datei- und Ordneroptionen)

class folder:
    
    
  #  def __init__():
        #logging.basicConfig(filename="folder_log.txt", format="%(asctime)s %(message)s")
        #year = datetime.now().strftime("%Y")
        #month = datetime.now().strftime("%m-%Y")
        
            
    def createFolder(pPath): # Erstellung eines Ordners falls dieser noch nicht existiert, mit Pfad als Parameter

        if not os.path.exists(pPath): #"Wenn Ordner noch nicht existiert"
            try:
                os.mkdir(pPath) #Erstelle Ordnern
            except OSError as error:
                print("mkdir error")
                logging.error(error) #Logging potentieller Fehlermeldung

    def delFolder(pTransfer): # Löschen eines Ordners, mit Pfad als Parameter
        try:
            shutil.rmtree(pTransfer) # Lösche Ordner
        except Exception as e:
            logging.error(e) #Logging potentieller Fehlermeldung
                    
            
    def transfer (pFile, pTransfer): # Kopieren einer Datei an einen anderen Ort, Dateipfad und Kopierpfad als Parameter
        
        try:
            shutil.copy(pFile, pTransfer) # Kopiere Datei
            #shutil.make_archive(pTransfer,'zip', pTransfer)
        except Exception as e:
            print('transfer error: ')
            print(e)
            logging.error(e) #Logging potentieller Fehlermeldung
            
    def compress(pTransfer): # Komprimierung einer Datei, eines Ordners als Zip. Pfad als Parameter
        
        try:
            shutil.make_archive(pTransfer,'zip', pTransfer) # Komprimierung, Speicherung des .zip an dem gleichen Ort
        except Exception as e:
            logging.error(e) #Logging potentieller Fehlermeldung
            
    def move_all_files(root_dir, d_dir):
        try:
            folder.createFolder(d_dir)
            contents = os.listdir(root_dir)
            for obj in contents:
                path = root_dir + '/' + obj
                if os.path.isfile(path):
                    shutil.move(path,d_dir)
        except Exception as e:
            print("error move_all_files")
            logging.error(e) #Logging potentieller Fehlermeldung
            
    # verschiebt die Dateien eines Ordners in Unterordner die jeweils nicht max_size in Speichergröße erreichen
    # max_size beschreibt die Größe in Bytes
    def chop_dir(root_dir, max_size):
        
        folder.move_all_files(root_dir,root_dir + '/0') # Verschieben aller Dateien im Verzeichnis ins Unterverzeichnis "root_dir/0"
        list_sub_dirs = os.listdir(root_dir)
        list_sub_dirs.sort()
        d = 0
        
        while ( d < len(list_sub_dirs)):
            bytesize = 0
            split_idx = 0
            cw_dir = root_dir + '/' + list_sub_dirs[d] # der zu überprüfende Ordner
            files = os.listdir(cw_dir)
            files.sort()
            
            for file in files:
                fPath = cw_dir + '/' + file
                f_size = os.path.getsize(fPath)
                if f_size >= max_size:
                    raise SizeError(file) # Fehler falls eine einzelne Datei das Limit überschreitet
                 
                bytesize += f_size
                if bytesize >= max_size :
                    split_idx = files.index(file)
                    
                    new_dir = root_dir + '/' + str(d+1)
                    j = 1
                    while new_dir == cw_dir:
                        new_dir = root_dir + '/' + str(d+j)
                        j = j + 1
                        
                    folder.createFolder(new_dir)
                    for i in range(split_idx,len(files)):
                        shutil.move(cw_dir + '/' + files[i], new_dir)
                    # falls cwdir in alphabetischer Ordnung hinter new_dir ist
                    # wird die Funktion erneut ausgeführt, damit auch new_dir überprüft wird
                    if (max(cw_dir,new_dir) in cw_dir):
                        return chop_dir(root_dir, max_size)
                    break
            d = d + 1
            list_sub_dirs = os.listdir(root_dir)
            list_sub_dirs.sort()
            
        # löschen leerer Unterverzeichnisse
        for i in list_sub_dirs:
            if not os.listdir(root_dir + '/' + i):
                folder.delFolder(root_dir + '/' + i)
 
class SizeError(Exception):
    
    def __init__(self, file):
        self.file = file
        
    def __str__(self):
        return ("file " + self.file + " exceeds size limit")

