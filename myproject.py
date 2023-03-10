class Bird:
    ruClassName = "Птица"
    objInstancesCount = 0

    def __init__(self, name: str, id: int, age: int):
        self.__name = name
        self.id = id
        self.age = age
        Bird.objInstancesCount = Bird.objInstancesCount + 1
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    def info(self):

        print(self.__name)
        print("id :" + str(self.id))
        print("age:" + str(self.age))

b1 = Bird(name = "объект №1 класса " + Bird.ruClassName, id = 123456, age=15)
print("its " + b1.get_name())
b1.set_name("goose")
print("its " + b1.get_name() )
