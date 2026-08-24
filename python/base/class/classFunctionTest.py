class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


person = Person("Alice", 30)
print(person)  # 输出: Person(name=Alice, age=30)
print(repr(person))  # 输出: Person(name='Alice', age=30)


person = Person("Alice", 30)
print(person.__dict__)  # 输出: {'name': 'Alice', 'age': 30}

# 修改属性
person.__dict__["age"] = 31
print(person.age)  # 输出: 31


person = Person("Alice", 30)
print(person.__class__)  # 输出: <class '__main__.Person'>

# 检查对象是否为特定类的实例
print(isinstance(person, Person))  # 输出: True
