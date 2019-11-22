a = [4,5,10,105,2,1,6,2,3,4]
b = [4,6,2,3,1,7,2,3]


a_dif = []

for item_a in a:
    if not item_a in b:
        a_dif.append(item_a)
print(a_dif)

a_dif_b_for_comprehensive = [item_a for item_a in a if item_a not in b]

print(a_dif_b_for_comprehensive)