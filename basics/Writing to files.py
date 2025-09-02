
#"r" == read this file
#"w" == you can change this file
#"a" == append
#"r+" == read and write




employee_file = open("employee.txt", "r")
print(employee_file.read())
employee_file.close()



employee_file = open("employee.txt", "a")
employee_file.write("\nRishabh - Human Resources")      #/n == Next line
employee_file.close()

employee_file = open("employee.txt", "w")
employee_file.write("\nSambhavi - Collector")      #/n == Next line
employee_file.close()

employee_file = open("employee.txt", "r+")
employee_file.write("\nUday - Inspector")      #/n == Next line
employee_file.close()

employee_file = open("index,html", "w")
employee_file.write("<p>This is HTML<p>")
employee_file.close()


