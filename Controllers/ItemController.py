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