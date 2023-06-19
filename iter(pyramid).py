class Pyramid:
    def __iter__(self):
        self.a = "*"
        return self

    def __next__(self):
        x = self.a
        self.a += "."
        return x


i = Pyramid()
j = iter(i)
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
