class TurnOnItem:
    def __init__(self, turnOn):
        for i in turnOn:
            if i.tag == 'print':
                self.print = i.text
            if i.tag == 'action':
                self.action = i.text
    def __str__(self):
        if self.print is not None:
            print(f"Print: {self.print}")
        if self.action is not None:
            print(f"Action: {self.action}")
            print()
        # return print(f"Print: {self.print} \nAction: {self.action}")