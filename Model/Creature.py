# Create class with name Creature and attributes name, status, attack, vulnerability, trigger, and item
# Create method __init__ with parameters self, name, status, attack, vulnerability, trigger, and item
# Create method __str__ with parameters self
# Create method attack with parameters self, creature
class Creature:
    def __init__(self, Creature): 
        for att in Creature:
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
