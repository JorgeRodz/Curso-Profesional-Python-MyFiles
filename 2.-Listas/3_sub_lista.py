lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

# To create a sub-list, we use the following syntax:
# list_name[start_index:stop_index]
sub_lista = lista_cursos[0:3]
print(sub_lista)

sub_lista_2 = lista_cursos[1:4]
print(sub_lista_2)

# [start_index:] -> From the start index to the end of the list
sub_list_to_end = lista_cursos[3:]
print(sub_list_to_end)

# [:stop_index] -> From the beginning of the list to the stop index
sub_list_from_start = lista_cursos[:4]
print(sub_list_from_start)

# [start_index:stop_index:step] -> From the start index to the stop index, with a step
sub_list_step = lista_cursos[1:5:2]
print(sub_list_step)

# [::-1] -> Reverse the list
sub_list_reverse = lista_cursos[::-1]
print(sub_list_reverse)

# [start_index:stop_index:-1] -> Reverse the list from the start index to the stop index
sub_list_reverse_2 = lista_cursos[4:1:-1]
print(sub_list_reverse_2)

# [start_index::-1] -> Reverse the list from the start index to the beginning of the list
sub_list_reverse_3 = lista_cursos[4::-1]
print(sub_list_reverse_3)
