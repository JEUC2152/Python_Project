""" #Ejercicio Platzi  


print('''
Digiturno  BanPlatzi

a. Deposito
b. Apertura de cuenta 

''')

Opcion = str(input('Opcion: '))

caja = []
apertura = []
turno = 0

if Opcion == 'a':
    turno += 1
    print('\nSu turno es: c{}'.format(turno))
else:
    turno += 1
    print('\nSu turno es: d{}'.format(turno)) """


import logging

logging.basicConfig(level=logging.INFO)

class Queue(object):
    def __init__(self,max_size):
        self.__rear=-1
        self.__front=-1
        self.__queue=[]
        self.__max_size=max_size-1
        pass
    def enQueue(self,data):
        if self.__rear<self.__max_size:
            self.__queue.append(data)
            logging.info('el dato {} ha sido agregado'.format(str(data)))
            self.__rear+=1
        
        else:
            logging.info('el queue ya ha alcanzado su capacidad maxima')
        pass
    def deQueue(self):
        if self.__rear>-1:
            logging.info('el dato {} ha sido retornado y removido'.format(self.__queue[0]))
            self.__front+=1
            self.__rear-=1
            return self.__queue.pop(0)
        else:
            logging.info('no existen más datos en el queue')
        pass
    def returnQueue(self):
        return self.__queue
    pass
queue=Queue(5)
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
queue.enQueue(5)
queue.enQueue(6)
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.deQueue()
