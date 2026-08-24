# 封装的实现
# __name和__age是私有属性，不能直接从外部访问
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age  # 私有属性

    def greet(self):
        return f"Hello, my name is {self.__name} and I am {self.__age} years old."

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")


# 创建实例
person = Person("Alice", 30)

# 访问私有属性 (通过方法)
print(person.greet())  # 输出: Hello, my name is Alice and I am 30 years old.

# 修改私有属性 (通过方法)
person.set_age(35)
print(person.get_age())  # 输出: 35

# 直接访问私有属性会导致错误
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'
