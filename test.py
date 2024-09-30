class MyClass:
  def __init__(self) -> None:
    self.name = "John"
    self.age = 30
    self.height = 180

  def __str__(self) -> str:
    return f"str name: {self.name}, age: {self.age}, height: {self.height}"

  def __repr__(self) -> str:
    return f"repr: MyClass(name={self.name}, age={self.age}, height={self.height})"

obj = MyClass()
print(obj)  # MyClass(name=John, age=30, height=180)
print(repr(obj))  # repr: MyClass(name=John, age=30, height=180)
