import gzip
import os


folder_dow = "C:\\Users\\Sr Director Patricio\\Downloads"
#extencion de los archivos 
ext_file = ['.png', '.pdf', '.gif', '.txt', '.exe' ]

#recorre el directorio 
for files in os.listdir(folder_dow):
    for i in  ext_file:
        if files.endswith(i):
            
            with open(os.path.join(folder_dow, files), 'rb') as f_input:
            
                with gzip.GzipFile(os.path.join(folder_dow, files + '.gz'), 'wb') as f_out:
                    f_out.writelines(f_input)
 
