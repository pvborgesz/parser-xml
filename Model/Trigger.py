# generate a class with the name of the trigger and attributes: type, condition, print

class Trigger: 
   def __init__(self, Room): 
    for att in Room:
      tag = att.tag

      try: 
        # se já existe valor no atributo
        value = getattr(self, tag)

        if (not isinstance(value, list)):
          setattr(self, tag, [value, att])
        else:
          value.append(att)
          
      except(AttributeError):
        # não existe valor no atributo
        setattr(self, tag, att)

    # i wanna se all the attributes of the class trigger
        # for i in self.__dict__: 
        #   print(i, self.__dict__[i])

    def showAllAttributes(self, trigger):
        for att in self:
            print(att)