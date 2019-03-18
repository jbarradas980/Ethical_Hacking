import zipfile
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Ejemplo de uso:')
        print ('\t\tdesencripta_zip_v1 Arg1 Arg2')
        print ('Donde:')
        print ('\tArg1 : Archivo.zip')
        print ('\tArg2 : Diccionario')
        exit (1)
    archivo=sys.argv[1]
    archivo_zip=zipfile.ZipFile(archivo)
    archivoDiccionario=sys.argv[2]
    cont=0
    for palabra in open(archivoDiccionario):
        try:
            password=palabra[:-1]#Limpia sólo el salto de linea
            archivo_zip.extractall(path='/tmp', pwd=bytes((password.encode('utf-8'))))
            print('La clave es: %s' % password)
            exit(0)
        except:
            pass
