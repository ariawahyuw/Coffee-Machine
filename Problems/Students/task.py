class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        names = list(name)
        self.id = (names[0] + last_name + birth_year)


input_ = Student(str(input()), str(input()), str(input()))
print(input_.id)
