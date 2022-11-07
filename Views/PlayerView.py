from Model.Player import Player
from Controllers.PlayerController import PlayerController
class PlayerView:
  def showCurrentPos(player):
    print("--------------------------------")
    print("Você está em: ", player.room.name)
    print("--------------------------------")

  def chooseNewDirection(player, allRooms):
    pos = ''
    directions = ["sul", "norte", "leste", "oeste"]
    while (pos not in directions):
      pos = input("Digite para qual direcao deseja ir (norte,sul,leste,oeste): ")
      PlayerController.changePlayerRoom(player,allRooms, pos)
    PlayerView.showCurrentPos(player)
    return pos