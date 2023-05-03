def listarTerminos(**terminos): #**kwards diccionario
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE = 'Integrated Developement Enviroment', PK = 'Primary key')
listarTerminos(DBMS = 'Database Management System')