lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

print(len(lista_cursos)) # print the length of the list
print('------------------')

# Add elements to the end of the list
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('Javascript')

print(lista_cursos)
print('------------------')

# Add element to an specific index
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')
print(lista_cursos)

# Merge two lists
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)
