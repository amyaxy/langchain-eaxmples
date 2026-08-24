class Person:
    species = "Homo sapiens"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# 创建实例
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 访问类属性
print(Person.species)  # 输出: Homo sapiens
print(person1.species)  # 输出: Homo sapiens
print(person2.species)  # 输出: Homo sapiens

# 修改类属性
Person.species = "Human"
print(person1.species)  # 输出: Human

# 访问实例属性
print(person1.name)  # 输出: Alice
print(person2.age)  # 输出: 25

# 调用方法
print(person1.greet())  # 输出: Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # 输出: Hello, my name is Bob and I am 25 years old.
