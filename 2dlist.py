

list2d=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
#DISPLAY 2D LIST#

print(list2d)

#FIND A NUMBER#

print(list2d[2][2])
#FINDING THE LENGTH#

print(len(list2d))
#PRINTING A ROW#

print(list2d[0])
print(len(list2d[0]))

#ADDING A ROW#

list2d.append([10,11,12])



print(list2d)

#ADDING A COLUMN TO A LIST#

for i in list2d:
     i.append(0)
print(list2d)
     
print(list2d[2][2])

list2d[2][2]=99

print(list2d)

list2d[1][1]=55

print(list2d)
#DELETING A ROW#

del list2d[1]
print(list2d)

#DELETING A COLUMN#

for i in list2d:
     del i[0]
print(list2d)

#PRINTING ALL ITEMS#

for row in list2d:
     for item in row:
          print(item,end=" ")
     print()
print()  
