from XMLController import Controller
from Model.Room import Room
import os

class RoomView:
  
  def __init__(self, map: dict): 
    self.controller = Controller(map)
    self.viewRoom(0, "")
  
  def getRoomByIndex(self, index: int):
    return self.controller.keys[index]

  def viewRoom(self, index: int, nameRoom: str):

    os.system("clear") # clear terminal

    if (index != -1): # buscar por índice
      nameRoom = self.getRoomByIndex(index)

    # buscar por nome
    room = self.controller.getRoom(nameRoom)

    print('---' * 20)
    print("Você está na sala " + room.name.text)
    print('---' * 20)
    
    print(room.description.text)

    self.showMenuOptions(room)


  def viewDirections(self, room: Room):
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

    self.viewRoom(-1, direction.name)
    #return direction.name

  def showMenuOptions(self, room: Room):
    try:
      print("\nEscolha uma opção: \n")
      print('---' * 20)
      print("[ 0 ] - Andar")
      print('---' * 20)

      op = (input(": "))
      if int(op) == 0:
        self.viewDirections(room)
    except Exception as e:
      print("Opção inválida")
      self.showMenuOptions(room)
