from time import sleep

class Buffer:
  MAX_LIMIT = 2
  data = [] # buffer data

  def printBuffer(self):
    print("Tamanho atual do Buffer: ", self.data)
    print("Limite do Buffer: ", self.MAX_LIMIT, "\n")

  def produce(self):
    if len(self.data) == self.MAX_LIMIT:
      print("\033[91m=> Buffer cheio, aguardando para produzir...\033[0m")

      while len(self.data) == self.MAX_LIMIT: sleep(1)

    print("\033[92mUm novo dado foi PRODUZIDO ao buffer.\033[0m")
    self.data.append(1)
    return self.printBuffer()

  def consume(self):
    if len(self.data) == 0:
      print("\033[91m=> Buffer vazio, não é possível consumir. Aguardando para consumir...\033[0m")

      while len(self.data) == 0: sleep(1) # verificar 

    print("\033[92mUm dado foi CONSUMIDO do buffer.\033[0m")
    self.data.pop()
    return self.printBuffer()


buffer = Buffer()