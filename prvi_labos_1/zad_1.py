names = ["Ana", "Petar", "Ana", "Lucija", "Vanja", "Pavao", "Lucija"]


def reverse_sort(names: list) -> list:
    names_copy = names[:]
    names_copy.sort(reverse=True)
    return names_copy


names_desc = reverse_sort(names)
print(names_desc)

selected_names = reverse_sort(names)[:len(names) - 1]
print(selected_names)

unique_selected_names = set(selected_names)
print(unique_selected_names)

pass_names = []
for name in unique_selected_names:
    nameExtended = name + " - pass"
    pass_names.append(nameExtended)

print(pass_names)
