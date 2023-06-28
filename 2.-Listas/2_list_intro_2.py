#index              0        1       2     3          4
#index             -5       -4      -3    -2         -1
lista_cursos = ['Python', 'Java', 'C++', 'C#', 'Javascript']
print(lista_cursos)
primer_curso = lista_cursos[0]
primer_curso = lista_cursos[-5]
print('0:', primer_curso)

segundo_curso = lista_cursos[1]
segundo_curso = lista_cursos[-4]
print('1: ', segundo_curso)

# ultimo_curso = lista_cursos[4]
ultimo_curso = lista_cursos[-1] # always return the last element
print('4:', ultimo_curso)

# -----------------------------------------------------------------------
lista_cursos[4] = 'Rust'
print(lista_cursos)
