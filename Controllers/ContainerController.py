from Model.Container import Container
from Model.Item import Item

class ContainerController:
    def createContainer(room):
        trigger = None
        name = None
        item = None
    #     for container in room:
    #         if container.tag == 'container':
    #             containerRoom = container
    #             for att in containerRoom:
    #                 tag = att.tag
    #                 # print(att)
    #                 if tag == 'name':
    #                     name = att.text
    #                 if tag == 'trigger':
    #                     trigger = att
    #                 if tag == 'item':
    #                     item = Item(item=att)
                    
    #                 if name != None and trigger != None and item != None:
    #                     # print("O container atual tem name, trigger e item")
    #                     container = Container(name=name,item=item, trigger=trigger)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif name != None and trigger != None:
    #                     # print("O container atual tem name e trigger")
    #                     container = Container(name=name, trigger=trigger)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif name != None and item != None:
    #                     # print("O container atual tem name e item")
    #                     container = Container(name=name, item=item)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif name != None:
    #                     # print("O container atual tem name")
    #                     container = Container(name=name)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif trigger != None and item != None:
    #                     # print("O container atual tem trigger e item")
    #                     container = Container(item=item, trigger=trigger)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif trigger != None:
    #                     # print("O container atual tem trigger")
    #                     container = Container(trigger=trigger)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 elif item != None:
    #                     # print("O container atual tem item")
    #                     container = Container(item=item)
    #                     if (type(container) != "<class 'NoneType'>"):
    #                         return container
    #                 # elif name == None and trigger == None and item == None:
    #                 #     # print("O container atual não tem nada")
                    
    # def itemFound(container):
    #     if container[0] != None:
    #         for item in container:
    #             if item.tag == 'item':
    #                 return item.text
    #     return None

    # def hasItem(container):
    #     # print(container, "to dentro de hasItem")
    #     if container[0] != None:
    #         # print("O container não é vazio")
    #         for item in container:
    #             # print(item, "to dentro do for do has item")
    #             if item.tag == 'item':
    #                 return True
    #     return False
    
    # def removeItem(container):
    #     if container[0] != None:
    #         for item in container:
    #             if item.tag == 'item':
    #                 container.remove(item)
    #                 return True
    #     return False