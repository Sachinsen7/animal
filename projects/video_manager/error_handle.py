file = open('index.txt', 'w')

try:
  file.write('im sachin')
finally:
    file.close()


with open('index.txt', 'w') as file:
   file.write('chai aur python')