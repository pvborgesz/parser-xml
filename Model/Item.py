from Model.TurnOnItem import TurnOnItem

class Item:
    def __init__(self, **kwargs):
        # turnOn = TurnOnItem.__init__(self)
        self.item = kwargs.get('item')
        for i in self.item:
            if i.tag == 'name':
                self.name = i.text
            if i.tag == 'writing':
                self.writing = i.text
            if i.tag == 'turnon':
                self.turnon = TurnOnItem(i)
            if i.tag == 'status':
                self.status = i.text
        # self.__str__()
    def __str__(self):
        if self.name is not None:
            print(f"Item: {self.name}")
        # if self.writing is not None:
        #     print(f"Writing: {self.writing}")
        # if self.turnon is not None:
        #     print(f"TurnOn: {self.turnon}")
        # if self.status is not None:
        #     print(f"Status: {self.status}")     
        # print(f"Item: {self.name} - Writing: {self.writing} - Status: {self.status}")

    def actionItem(self):
        return print(self.turnon.__str__())

'''
<Element 'name' at 0x101138bd0>
<Element 'writing' at 0x101138c20>
<Element 'status' at 0x101138c70>
<Element 'turnon' at 0x101138cc0>

<name>jammer</name>
       <status>Inativo</status>
       <writing>Coloque-me no gerador para travar e desligar a energia!</writing>
       <turnon>
           <print>O jammer foi ligado</print>
           <action>Atualize o jammer para on</action>
       </turnon>
'''