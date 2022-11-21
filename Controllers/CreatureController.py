class CreatureController:
    
    def hasCreature():
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
        