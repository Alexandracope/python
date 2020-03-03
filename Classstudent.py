class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

John=student("John","21")
Jane=student("Jane","22")

print(getattr(John, "age"))

