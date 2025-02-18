#Modo normal
frutas=['abacate','banana','caju','damasco','figo']
# frutas2 = []
# for item in frutas:
#     if 'f' in item:
#         frutas2.append(item)
# print(frutas2)

#Comprehension
frutas2=[item for item in frutas if 'f' in item]
print(frutas2)