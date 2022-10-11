#improving the ability to use numbers, operators, and arithmetic operations in Python;
#using the print() function's formatting capabilities;
#learning to express everyday-life phenomena in terms of programming language.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
total_time=hour*60
total_time=total_time + mins + dura
print((total_time//60)%24, end=":")
print(total_time%60)
