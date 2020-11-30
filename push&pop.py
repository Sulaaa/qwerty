stack_store = []

for x in range(5):
    stack_store.append(x)
print(f'Текущий стек: {stack_store},Размер стека:{len(stack_store)}')

stack_store = stack_store[:-1]

while stack_store != 0:
    print(stack_store.pop)

print(f'Стек после pop:{stack_store}')