from Model.Player import Player
from Model.Room import Room
from Controllers.BorderController import BorderController
from Views.BorderView import BorderView
from Views.RoomView import RoomView

class PlayerController:

  def changePlayerRoom(player, allRooms, newPosition):
    currentPos = player.room
    hasChanged = False
    # print(currentPos.border.name, currentPos.border.direction)
    for room in allRooms:
      # print(room.name)
      if room.name.lower() ==  player.room.name.lower() and not hasChanged:
        # print(room.name)
        # RoomView.printRoom(room)
        for border in room.border:
          # BorderView.printBorder(border)
          # print(border.name, border.direction)
          if (border.direction.lower() == newPosition.lower()
              and not hasChanged):
            currentPos = border.name
            nextRoom = ''
            for i in allRooms: 
              if(i.name==currentPos): 
                nextRoom = i
                # print("Vim para ", nextRoom.name)
                break
            player.room = nextRoom
            # player.room.name = currentPos
            hasChanged = True
            # player.room.border = BorderController.updateBorders(player.room, allRooms)
            # BorderView.printBorder(player.room.border)          
            # print(player.room.border[0][0].name)
            
            
  


