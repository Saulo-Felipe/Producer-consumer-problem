'''
Utilizei duas threads chamadas "consumerThreading" e "producerThreading" 
para realizar suas respectivas funções de forma aleatória (inserir e remover do buffer). 
Caso o buffer esteja cheio ou vazio, o produtor ou o consumidor aguardará até que possa
realizar a ação.

Os metodos executados pelas threads operam de forma recursiva tentando produzir ou consumir 
em um intervalo de tempo aleatório, entre 1 e 4 segundos. Como se trata de uma 
simulação do problema, o programa não possui uma condição de parada definida, 
sendo necessário que o usuário o interrompa.

O tamanho do buffer é pequeno (2) para facilitar a visualização do problema.
'''

import threading
from time import sleep
from Buffer import buffer
from random import randint


def randomProduceNewData():
  sleep(randint(1, 4))
  buffer.produce()
  randomProduceNewData()

def randomConsumeNewData():
  sleep(randint(1, 4))
  buffer.consume()
  randomConsumeNewData()


consumerThreading = threading.Thread(target=randomConsumeNewData)
producerThreading = threading.Thread(target=randomProduceNewData)

consumerThreading.start()
producerThreading.start()