class ItemController:
    def createItem(room):
        for item in room:
            print(item)
            if item.tag == 'item':
                itemRoom = item.text
                print(itemRoom)
                return itemRoom

    def roomHasItem(room):
        for item in room:
            if item.tag == 'item':
                return True
            else:
                return False

    def hasItem():
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
    def ativarItem(item : Item):
        for i in player[0].itens:
          i.__str__()
        wannaSee = int(input("Deseja ver algum item? (1-Sim / 0- Não): "))
        if wannaSee == 1:
            itemIndex = int(input("Digite o índice do item que deseja ver: "))
            print()
            print(player[0].itens[itemIndex].actionItem())
            item.status = True