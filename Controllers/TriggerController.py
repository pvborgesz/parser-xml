class TriggerController:
    def __init__():
        pass
    
    def hasTrigger():
        if (hasattr(room, "trigger")):
            trigger = Trigger(room.trigger)
            if (trigger.print is not None):
                print(trigger.print.text)
                if (trigger.condition != None):
                    for i in trigger.condition:
                        if i.tag == "has":
                            if i.text != 'sim':

                                userCanPass = True
                        else:
                            for j in trigger.condition:
                                if j.tag == "object":
                                    print("Voce precisa ter o item", j.text, "para entrar nesse ambiente.")
                            for k in player[0].itens:
                                if k == j.text:
                                    print("voce tem o item para entrar no local, pode entrar")

        else:
            print("Você pode prosseguir")
            # self.showMenuOptions(room, player)