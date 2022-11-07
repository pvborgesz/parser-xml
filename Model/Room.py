## Cria um objeto room e garante que se existir dois atributos com mesmo nome, esse atributo passará a ser um array com esses valores

class Room: 
  def __init__(self, Room, *container): 
    if container != None:
      self.container = container

    for att in Room:
      tag = att.tag
      try: 
        # se já existe valor no atributo
        value = getattr(self, tag)
        if (not isinstance(value, list)):
          setattr(self, tag, [value, att])
          # print("coloquei o valor ", tag , att)
        else:
          value.append(att)
          
      except(AttributeError):
        # não existe valor no atributo
        setattr(self, tag, att)
        # print("coloquei o valor ", tag , att)
    # for i in self.__dict__: 
    #   print(i, self.__dict__[i])
      
  def __str__(self):
    if (self.item) is not None:
    #   print('Item -', self.item)
    # print(f"Room: {self.name} ")
      print()
      
    