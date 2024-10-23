class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    _sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
         self.sound = super().sound
         self.sound = super()._sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

print(Pegasus.mro())

# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)
#         super().about()
#
#     def info(self):
#         print(f'Привет, меня зовут {self.name}')
#
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} учится в группе {self.group}')
#
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         super().__init__(name, group)
#         self.place = place
#         super().info()
#
#
# # human = Human('Сэм')
# # print(human.name)
# student = Student('Бэн','Омск', 'Питонище')
# print(Student.mro())
#
