import xml.etree.ElementTree as ET
from Model.Room import Room
from Model.Player import Player
from View import View
from Controllers.ItemController import ItemController
from Controllers.ContainerController import ContainerController
from Views.PlayerView import PlayerView

tree = ET.parse('adventure.xml') # le o arquivo
root = tree.getroot()

#Navegar
#Implementar verbo Pegar(coletar item)
#Verbo Olhar (mostrar descricao item)
#Implementar Triggers
#implementar creatures 

rooms = []
username = input("Digite seu nome: ")
itens = [] # lista de itens do jogador

player = Player(username, itens)

for room in root:
  sala = Room(room)
  container =  ContainerController.createContainer(room)
  # container.__str__()
  # print(type(container))
  sala = Room(room, container)
  # player.__str__()
  rooms.append(sala)


view = View(rooms,player)

