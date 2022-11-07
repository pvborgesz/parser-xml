import xml.etree.ElementTree as ET

from Model.Room import Room
from View.RoomView import RoomView
from Model.Border import Border
from View.BorderView import BorderView

tree = ET.parse("./aventura.xml")
root = tree.getroot()


class RoomController:

  def __init__(self):
    self.name = ''
    self.direction = ''

  # def createRooms(root):
  #   roomList = []
  #   currentName = ''
  #   currentDescription = ''
  #   currentBorder = []
  #   nameBorder = ''
  #   directionBorder = ''
  #   for room in root:
  #     for roomAttrib in room:
  #       if (roomAttrib.tag == 'name'):
  #         currentName = roomAttrib.text
  #       if (roomAttrib.tag == 'description'):
  #         currentDescription = roomAttrib.text

  #       if (roomAttrib.tag == 'border'):
  #         for border in roomAttrib:
  #           if (border.tag == 'name'):
  #             nameBorder = border.text
  #           if (border.tag == 'direction'):
  #             directionBorder = border.text
  #           if (len(nameBorder) >= 1 and len(directionBorder) >= 1 ):
  #             currentBorder.append(Border(nameBorder, directionBorder))
  #             aux = Border(nameBorder, directionBorder)
  #             currentBorder = RoomController.filterBorder(currentName,aux)

  #       room = Room(currentName, currentDescription, currentBorder)
  #       roomList.append(room)
  #     currentName = ''
  #     currentDescription = ''
  #     currentBorder = []
  #     nameBorder = ''
  #     directionBorder = ''

  #       # print(roomList)
  #   return roomList

  def filterBorder(room, border):
    listAux = []
    if (border.name == room):
      listAux.append(border)
    return listAux

  def createRooms(root):
    roomList = []
    nameRoom = ''
    descriptionRoom = ''
    itemRoom = ''
    borderRoom = []
    borderName = ''
    borderDirection = ''

    for rootAttrib in root:
      for room in rootAttrib:
        if room.tag == 'name':
          nameRoom = room.text
        if room.tag == 'description':
          descriptionRoom = room.text
        if room.tag == 'item':
          itemRoom = room.text
        if room.tag == 'border':
          for i in room:
            if i.tag == 'direction':
              borderDirection = i.text
            if i.tag == 'name':
              borderName = i.text
            borderRoom.append(Border(borderName, borderDirection))

          # print('estou adicionando', nameRoom, borderName, borderDirection)
          room = Room(nameRoom, descriptionRoom, borderRoom)
          room.item = itemRoom

          roomList.append(room)
    return roomList

  # # def createRooms(root):
  # #   roomList = []
  # #   listAux = []
  # #   for rootAttrib in root:
  # #     roomList.append(rootAttrib)
  # #   for room in roomList:
  # #     # print(room.tag)
  # #     for roomAux in room:
  # #       print(roomAux)
  # #       if roomAux.tag ==
  #   return roomList
  def createMap(rooms: list):
    map_rooms = {}

    for room in rooms:

      if (str(type(room.border)) == "<class 'list'>"):
        borders = room.border  #array
        borders_obj = []

        for border in borders:
          border_obj = Border(border)
          borders_obj.append(border_obj)

        room.border = borders_obj
      else:
        border_obj = Border(room.border)
        room.border = border_obj

      map_rooms[room.name.text] = room
    return map_rooms
