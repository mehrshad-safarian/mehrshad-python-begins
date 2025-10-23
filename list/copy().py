old_list = [1,2,3]
new_list = old_list.copy()
new_list.append(5)

print(old_list)
print(new_list)


old_list = [1, 2, [3, 4]]
new_list = old_list.copy()
new_list[2].append(5)

print(old_list)  # [1, 2, [3, 4, 5]] ← تغییر کرد!
print(new_list)  # [1, 2, [3, 4, 5]]
