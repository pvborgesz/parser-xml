from Model.Border import Border
class BorderView:
  def printBorder(border):
    # if type(border) is Border:
    # borderAux = Border(border.name, border.direction)
    for borderAux in border:
      print("BorderDirection ->", borderAux.direction, "BorderName -> ",borderAux.name)
    print()   

