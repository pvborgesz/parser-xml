from Model.Border import Border;
from Model.Room import Room;

class BorderController:
  def updateBorders(nextRoom, allRooms):
    currentBorders = ''
    for i in allRooms:
      currentBorder = i.border
      if (nextRoom.name.lower() == i.name.lower()):
        # currentBorders.append(i.border)
        currentBorders = (i.border)
        # print("atualizei a borda do quarto", nextRoom.name, "para", currentBorder.name, "na direcao", currentBorder.direction)
    return currentBorders