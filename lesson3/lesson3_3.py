import tools

print(tools.MON)
p1 = tools.person(name='robert',age=30)
print(p1)

s1 = tools.Student(name='LIN',age=40,chinese=87,english=75,math=67)
print(s1.name)
print(s1.age)
print(s1.chinese)
print(s1.english)
print(s1.math)
print(s1.total)
print(s1.average())

print('===============')
p2 = tools.get_person('CAU JYU',32)
print(p2)

print('===============')
s2 = tools.get_student(name='Orange',age=28)
print(s2)
print(s2.total)
print(s2.average())
