MON = 1
TUE = 2
WEN = 3
THU = 4
FRI = 5
SAT = 6
SUN = 7

class person(object):
    def __init__(self,name:str,age:int):
        self.__name = name
        self.__age = age

    def __repr__(self) -> str:
        return f'我的名字是:{self.name}\n我的age是:{self.age}'
    
    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self,n):
        print(f'不可以改名為{n}')

    @property
    def age(self)->int:
        return self.__age
    
    @age.setter
    def age(self,value):
        if value > 100 or value < 0:
            print(f'不合法的值')
        else:
            self.__age = value

class Student(person):
    @classmethod
    def echo(cls):
        print('Hello!我是StudentClass')

    def __init__(self, age:int, name:str, chinese:int=0, english:int=0, math:int=0):
        super().__init__(name=name,age=age)
        self.chinese = chinese
        self.english= english
        self.math = math
        
    @property
    def total(self) -> int:
        return self.chinese + self.english + self.math

    def average(self) -> float:
        return round(self.total / 3,ndigits=2)
    
def get_person(name:str, age:int) -> person:
    return person(name=name,age=age)
    
def get_student(name:str, age:int, chinese=60,english=60,math=60)->Student:
    return Student(name=name,age=age,chinese=chinese,english=english,math=math)