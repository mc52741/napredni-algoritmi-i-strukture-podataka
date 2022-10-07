person_data = {
    "Ana": 1995, "Zoran": 1978,
    "Lucija": 2001, "Anja": 1997
}
# person_data : dict = {"Ana":1995,"Zoran":1979,"Lucija":2001,"Anja":1997}
print(person_data)

for key_name in person_data:
    # print(key_name + ": " + str(person_data[key_name]))
    person_data[key_name] -= 1
    # print(key_name + ": " + str(person_data[key_name]))

print(person_data)

year_age = []

for birth_year in person_data.values():
    temp = (birth_year, 2022 - birth_year)
    year_age.append(temp)

print(year_age)
