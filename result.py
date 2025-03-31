result = ['Mario', 'Luigi']

# 这里的append方法是用来在已存在的列表末尾增添元素的
result.append('Daisy')
result.append('Yoshi')
result.append('Peach')
result.append('Toad')
result.append('Wario')

# 这里的extend方法是用来在已存在的列表末尾增添多个元素的
result.extend(['Bowser', 'Koopa'])

# 这里的remove方法是用来删除列表中指定的元素的
result.remove('Koopa')     

# 这里的insert方法是用来在已存在的列表中插入元素的，其中的0表示在列表的第一个位置插入元素
result.insert(0, 'Koopa')

result.reverse()  # 反转列表

print(result)
print(result[3])