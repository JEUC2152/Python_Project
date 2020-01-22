import os 

pila = []
cima =-1
print('\t\tROBOT LAVAPLATOS\n\n 1. Agregar plato \n 2. Lavar plato \n 3. listar cantidad de platos \n 4. Apagar Robot\n')

while True:
    opcion = int(input('\nOpcion: '))
    total = len(pila)
    total_lavado = total - 1

    if opcion == 1:
        if cima < 20:
            plato = 1
            pila.append(plato) 
            cima += 1
            print('\nSe agrego plato, Correctamente\n')
        else: 
            print('Esta llena la pila de platos\n')
    elif opcion == 2:
        if cima > -1:
            pila.pop()
            cima-=1
            print('\nSe ha lavado el plato\nRestantes: ' + str(total_lavado))
        else:
            print('\nLa pila esta vacia, ingresar platos \n')

    elif opcion == 3:
        print ('\nPlatos restantes: ' + str(total) + '\n') 
    
    elif opcion == 4:
        print ('Apagando...')
        break
    
    else:
        print('No reconoce la opcion\n')

    """ os.system("cls") """ 








""" class RobotLavaplatos:

    def __init__(self, dato):
        self.items = [20]
        self.dato = dato
    
    def agregar(dato):
        return self.items.append(dato)
        print('Se agrego plato')
    
    def lavar(self):
        if self.esta_vacia():
            return ('Ya no quedan plato')
            print('Ya no quedan platos')
        else:
            return self.items.pop()

    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else: 
            return False
        
    def lista(self):
        return len(self.items)


if __name__ == '__main__':
    Robot = RobotLavaplatos(1)
    
    print('\t\tROBOT LAVAPLATOS\n\n 1. Agregar plato \n 2. Lavar plato \n 3. listar cantidad de platos \n')
    opcion = int(input('Opcion: '))

    if opcion == 1:
        Robot.agregar()    

    elif opcion == 2:
        Robot.lavar()

    elif opcion == 3:
        Robot.lista()
    else:
        print('No reconoce la opcion')


 """

























""" def agregar_plato:



if __name__ == '__main__':
    print('\t\tROBOT LAVAPLATOS\n 1. Agregar plato \n 2. Lavar plato \n 3. listar cantidad de platos \n')
    opcion = int(input('Opcion: '))

 """




""" class Stack:

    def __init__(self, n):
        self.size = n 
        self.data = [None] * n
        self.top = -1
    
    def push(self, e):
        if self.top + 1 == self.size:
            raise Exception('Overflowed')
        self.top += 1 
        self.data[self.top]= e
    
    def pop(self):
        if self.top == -1:
            raise Exception('under flowed')
        e = self.data[self.top]
        self.top -= 1
        return e   """