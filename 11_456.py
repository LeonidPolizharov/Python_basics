class Warehouse:
    print("Склад:")


class Equipment:
    def __init__(self, vendor, color):
        self.vendor = vendor
        self.color = color


class Printer(Equipment):
    cnt_printer = 0

    def __init__(self, vendor, color):
        super().__init__(vendor, color)
        Printer.cnt_printer += 1

    @staticmethod
    def name():
        return "Принтер"

    def __str__(self):
        return "\t Vendor, color: {}, {}".format(self.vendor, self.color)


class Scanner(Equipment):
    cnt_scanner = 0

    def __init__(self, vendor, color):
        super().__init__(vendor, color)
        Scanner.cnt_scanner += 1

    @staticmethod
    def name():
        return"<<Сканер>>"

    def __str__(self):
        return "\t Vendor, color: {}, {}".format(self.vendor, self.color)



class Xerox(Equipment):
    cnt_xerox = 0

    def __init__(self, vendor, color):
        super().__init__(vendor, color)
        Xerox.cnt_xerox += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def __str__(self):
        return "\t Vendor, color: {}, {}".format(self.vendor, self.color)


p1 = Printer('Canon', 'white')
p2 = Printer('HP', 'gray')
print(p1.name(), p1.cnt_printer, "шт.:")
print(p1.__str__())
print(p2.__str__())


s1 = Scanner('Epson', 'black')
s2 = Scanner('HP', 'white')
print(s1.name(), s1.cnt_scanner, "шт.:")
print(s1.__str__())
print(s2.__str__())


x1 = Xerox('HP', 'white')
x2 = Xerox('Canon', 'black')
x3 = Xerox('Xerox', 'white')
print(x1.name(), x1.cnt_xerox, "шт.:")
print(x1.__str__())
print(x2.__str__())
print(x3.__str__())
