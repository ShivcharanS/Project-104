# Python program to print
# mode of elements
from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


n = len(new_data)
#using counter function to get the occurences of numbers
data = Counter(new_data)
# # print(data)
get_mode = dict(data)
#
mode = []
mode1 = []
mode2 = []
mode3 = []
mode4 = []
mode5 = []
mode6 = []
mode7 = []
mode8 = []
mode9 = []

#taking a,v for key and value
for a,v in get_mode.items():
    #changing type of a from string to float
    a= float(a)
    if 75< a <85:
        if v == max(list(data.values())):
            mode.append(a)
    elif 85< a <95:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 95< a <105:
        if v == max(list(data.values())):
            mode2.append(a)
    elif 105< a <115:
        if v == max(list(data.values())):
            mode3.append(a)
    elif 115< a <125:
        if v == max(list(data.values())):
            mode4.append(a)
    elif 125< a <135:
        if v == max(list(data.values())):
            mode5.append(a)
    elif 135< a <145:
        if v == max(list(data.values())):
            mode6.append(a)
    elif 145< a <155:
        if v == max(list(data.values())):
            mode7.append(a)
    elif 155< a <165:
        if v == max(list(data.values())):
            mode8.append(a)
    elif 165< a <175:
        if v == max(list(data.values())):
            mode9.append(a)
    

if len(mode)>len(mode1) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode)))
elif len(mode1)>len(mode) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode1)))
elif len(mode2)>len(mode) and len(mode1):
    print("Mode is /are "+ ', '.join(map(str, mode2)))
elif len(mode3)>len(mode) and len(mode4):
    print("Mode is /are "+ ', '.join(map(str, mode3)))
elif len(mode4)>len(mode) and len(mode3):
    print("Mode is /are "+ ', '.join(map(str, mode4)))
elif len(mode5)>len(mode) and len(mode6):
    print("Mode is /are "+ ', '.join(map(str, mode5)))
elif len(mode6)>len(mode) and len(mode5):
    print("Mode is /are "+ ', '.join(map(str, mode6)))
elif len(mode7)>len(mode) and len(mode8):
    print("Mode is /are "+ ', '.join(map(str, mode7)))
elif len(mode8)>len(mode) and len(mode7):
    print("Mode is /are "+ ', '.join(map(str, mode8)))
elif len(mode9)>len(mode) and len(mode8):
    print("Mode is /are "+ ', '.join(map(str, mode9)))

# print(get_mode,"this is  mdoe")
