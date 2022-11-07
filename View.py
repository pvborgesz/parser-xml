from XMLController import Controller
from Model.Room import Room
from Model.Player import Player
from Model.Item import Item
from Model.Trigger import Trigger
from Controllers.ContainerController import ContainerController
from Controllers.ItemController import ItemController
import os

class View:
  
  def __init__(self, map: dict, *player: Player): 
    self.controller = Controller(map)
    self.viewRoom(0, "",player)
    if player != None: self.player = player
  
  def getRoomByIndex(self, index: int, player):
    return self.controller.keys[index]

  def viewRoom(self, index: int, nameRoom: str, player: Player):

    os.system("clear") # clear terminal

    if (index != -1): # buscar por índice
      nameRoom = self.getRoomByIndex(index, player)

    userCanPass = False
    # buscar por nome
    room = self.controller.getRoom(nameRoom)
    print('---' * 20)
    print("Você está na sala " + room.name.text)
    print("Descrição: " + room.description.text)
    print('---' * 20)
    if (room.name.text.lower() == "escape pod"):
      print("VOCÊ VENCEU!!!")
      print("Obrigado por jogar {}!" .format(player[0].name))
    currentRoom = room
    currentContainer = room.container
    # print(hasattr(room, "item"))

    # descobrir se tem um trigger
    if (hasattr(room, "trigger")):
      trigger = Trigger(room.trigger)
      # print(trigger.__str__())
      if (trigger.condition != None):
        for i in trigger.condition:
          # print(i, "eai")
          if i.tag == "has":
            if i.text != 'sim':
              # print(i.text, "oi, pode entrar")
              userCanPass = True
            else:
              for j in trigger.condition:
                if j.tag == "object":
                  print("Voce precisa ter o item", j.text, "para entrar nesse ambiente.")
                  # print(player[0].itens, "1231")
                  for k in player[0].itens:
                    if k == j.text:
                      print("voce tem o item para entrar no local, pode entrar")
        # print("Você não pode prosseguir")
        # self.showMenuOptions(room, player)
      else:
          print("Você pode prosseguir")
          # self.showMenuOptions(room, player)
    
    if (hasattr(room, "creature")):
      print("Tem criatura aqui, eita.")
      for i in room.creature:
        # print(i,'to no for de criatura')
        if i.tag == "creature":
          for j in i:
            if j.tag == 'name':
              print("O nome da criatura é ", j.text)
            if j.tag == 'vulnerability':
              print("A criatura é vulnerável a ", j.text)
            if j.tag == 'attack':
              for k in j:
                if k.tag == 'condition':
                  for l in k:
                    if l.tag == 'object':
                      print("Você precisa ter o item", l.text, "para atacar a criatura.")
                      # print(player[0].itens)
                      for o in player[0].itens:
                        if o.name == l.text:
                          print("Você tem o item necessário para atacar a criatura.")
                          for j in i:
                            if j.tag == 'print':
                                print(j.text)
                          print("Você pode prosseguir")
        if i.tag == 'name':
          print("O nome da criatura é ", i.text)
        if i.tag == 'vulnerability':
          print("A criatura é vulnerável a ", i.text)
        if i.tag == 'attack':
          for j in i:
            if j.tag == 'condition':
              for k in j:
                if k.tag == 'object':
                  print("Você precisa ter o item", k.text, "para atacar a criatura.")
                  # print(player[0].itens)
                  for l in player[0].itens:
                    if l.name == k.text:
                      print("Você tem o item necessário para atacar a criatura.")
                      for k in i:
                        if k.tag == 'print':
                            print(k.text)
                      print("Você pode prosseguir")
                      # self.showMenuOptions(room, player)
        
      # showAllAttributes(trigger)
 # if room.item is not None: #pegar item que fica dentor da sala
    # print(hasattr(room, "item"), "tem item?")
    if hasattr(room, "item"):
      for i in room.item:
          nameItem = ''
          flagCatched = False
          itemObj = Item(item=room.item)
          for j in room.item:
            if j.tag == 'name':
              nameItem = j.text
          try:
            op = input("Voce encontrou um(a) " + nameItem + ". Deseja pegar? (1-Sim / 0- Não): ")
            if int(op) == 1:
              print(nameItem, " foi adicionado ao seu inventário.")
              flagCatched = True
              player[0].itens.append(itemObj) 
              break
            else:
              break
          except Exception as e:
            print("Opção inválida", e, "i")
            # self.viewRoom(index, nameRoom, player)
          if flagCatched:
            player[0].itens.append(itemObj)
            print("adicionei", itemObj)
            break
                        
    for i in range(len(currentContainer)): #pegar item dentro do container 
      # print(i, currentContainer[i])
      if i > 0:
        for j in currentContainer[i]:
          if j.tag == "item":
            itemObj = Item(item=j)
            flagCatched = False
            for w in j :
              if w.tag == 'name':
                try:
                  op = input("Voce encontrou um(a) " + w.text + ". Deseja pegar? (1-Sim / 0- Não): ")
                  if int(op) == 1:
                    print(w.text, " foi adicionado ao seu inventário.")
                    flagCatched = True
                except Exception as e:
                  print("Opção inválida", e)
                  # self.viewRoom(index, nameRoom, player)
            if flagCatched:
              player[0].itens.append(itemObj)

      if hasattr(room, "item"):
        # print(currentRoom.name.text, "to aqui e tem item")
        print("\n"*5)

     



    self.showMenuOptions(room, player)


  def viewDirections(self, room: Room, player):
    borders = room.border
    cont = 0

    print("\nDireções: \n")

    if (str(type(room.border)) == "<class 'list'>"): 
      for border in borders:
        print(f"{cont} - Ao {border.direction} está a sala {border.name}. " )
        cont += 1
    else: 
        print(f"0 - Ao {borders.direction} está a sala {borders.name}." )

    opt_direction = int(input("\nDigite a opção desejada: "))

    if (str(type(room.border)) == "<class 'list'>"):
      direction = borders[opt_direction]
    else: 
      direction = borders

    self.viewRoom(-1, direction.name, player)
    #return direction.name

  def showMenuOptions(self, room: Room, player):
    try:
      print("\nEscolha uma opção: \n")
      print('---' * 20)
      print("[ 0 ] - Andar")
      print("[ 1 ] - Olhar Inventário de Itens")
      print('---' * 20)

      op = (input(": "))
      if int(op) == 0:
        self.viewDirections(room, player)
      if int(op) == 1:
        print("Inventário de Itens:")
        for i in player[0].itens:
          i.__str__()
        wannaSee = int(input("Deseja ver algum item? (1-Sim / 0- Não): "))
        if wannaSee == 1:
            itemIndex = int(input("Digite o índice do item que deseja ver: "))
            print()
            print(player[0].itens[itemIndex].actionItem())
        self.showMenuOptions(room, player)
      else:
        print("Opção inválida")
        self.showMenuOptions(room, player) 
    except Exception as e:
      print("Opção inválida", e)
      self.showMenuOptions(room, player)
