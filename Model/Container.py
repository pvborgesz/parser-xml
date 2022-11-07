class Container:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.item = kwargs.get('item')
        self.trigger = kwargs.get('trigger')
        self.status = kwargs.get('status')
        # if self.name is not None:
        #     print(self.name, "oi nome")
        # if self.item is not None:
        #     print(self.item, "oi item")
        # if self.trigger is not None:
        #     print(self.trigger, "oi trigger")
        # if self.status is not None:
        #     print(self.status.text, "oi status")
    #     self.__str__()

    # def __str__(self):
    #     return print(f"Container: {self.name} - Item: {self.item} - Trigger: {self.trigger} - Status: {self.status}")
    def getNonNoneAttributes(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
    
    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def createContainer(room):
        trigger = None
        name = None
        item = None
        for container in room:
            if container.tag == 'container':
                containerRoom = container
                for att in containerRoom:
                    tag = att.tag
                    print(att)
                    if tag == 'name':
                        name = att.text
                    if tag == 'trigger':
                        trigger = att
                    if tag == 'item':
                        item = att
                    
                    if name != None and trigger != None and item != None:
                        # print("O container atual tem name, trigger e item")
                        container = Container(name=name,item=item, trigger=trigger)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif name != None and trigger != None:
                        # print("O container atual tem name e trigger")
                        container = Container(name=name, trigger=trigger)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif name != None and item != None:
                        # print("O container atual tem name e item")
                        container = Container(name=name, item=item)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif name != None:
                        # print("O container atual tem name")
                        container = Container(name=name)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif trigger != None and item != None:
                        # print("O container atual tem trigger e item")
                        container = Container(item=item, trigger=trigger)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif trigger != None:
                        # print("O container atual tem trigger")
                        container = Container(trigger=trigger)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    elif item != None:
                        # print("O container atual tem item")
                        container = Container(item=item)
                        if (type(container) != "<class 'NoneType'>"):
                            return container
                    # elif name == None and trigger == None and item == None:
                    #     # print("O container atual não tem nada")
                    