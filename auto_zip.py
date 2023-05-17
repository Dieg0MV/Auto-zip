import gzip
import os

#directorio 
folder_dow = "C:\\Users\\Sr Director Patricio\\Downloads"
#extencion of file
ext_file = ['.png', '.pdf', '.gif', '.txt', '.exe' ]

#recorre el directorio 
for files in os.listdir(folder_dow):
    #Scroll through the list of extensions
    for i in  ext_file:
        #Select files with the correct extension
        if files.endswith(i):
            
            with open(os.path.join(folder_dow, files), 'rb') as f_input:
            
                with gzip.GzipFile(os.path.join(folder_dow, files + '.gz'), 'wb') as f_out:
                    f_out.writelines(f_input)
 