num_list = [3, 5, 7, 9, 10.5]
print(num_list)
num_list.append('Python')
print(len(num_list))
print(num_list)

print(num_list[0])
print(num_list[-1])
print(num_list[1:4]) # [5, 7, 9]

del num_list[-1]
print(num_list)




dict = {
    'city': 'Moscow',
    'temperature': '20'
}

print(dict['city'])
print(int(dict['temperature']) - 5)
print(dict)

print(dict.get("country"))
print(dict.get("country", "Russia"))

dict["date"] = "27.05.2019"
print(dict["date"])

print(dict)
print(len(dict))