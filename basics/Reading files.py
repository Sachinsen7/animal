

#"r" == read this file
#"w" == you can change this file
#"a" == append
#"r" == read and write

employee_file = open("employee.txt", "r")
print(employee_file.readlines()[1])             #readable , read , readline , readlines
employee_file.close()


employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()