lines = [
    'grape banana mango',
    'nut orange peach',
    'apple nut banana apple mango',
]

lines_list = []

for idx, element in enumerate(lines):
    lines_list += element.split()

print(lines_list)

lines_sort = sorted(list(set(lines_list)))
print(lines_sort)