from myclass import my_numbers
from myclass import my_numbers_child

x = my_numbers(1,2)
y = my_numbers(5,6)
x.print_n1n2()
x.change_att()
print(x.sum_n1n2())
print(y.mult_n1n2())


#child class
z = my_numbers_child(7, 8, 3)
z.print_n1n2()
print(z.mult_n1n2())
print(z.n3_square())

