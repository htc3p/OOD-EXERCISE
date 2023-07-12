def ManageStack(stack , i):
    s = [e for e in i.split(' ')]
    command = s[0]

    if command == 'A':
        if len(s) > 1:
            value = int(s[1])

            stack.append(value)
            return f'Add = {value}'
        
    elif command == 'P':
        if len(stack) <= 0:
            return '-1'
        else:
            temp = stack.pop(-1)
            return f'Pop = {temp}'
        
    elif command == 'D':
        if len(s) > 1:
            value = int(s[1])

            if len(stack) <= 0:
                return '-1'
            else:
                deleted = []
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == value:
                        deleted.append(f'Delete = {stack.pop(i)}')

                return deleted
            
    elif command == 'LD':
        if len(s) > 1:
            value = int(s[1])

            if len(stack) <= 0:
                return '-1'
            else:
                deleted = []
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] < value:
                        temp = stack.pop(i)
                        deleted.append(f'Delete = {temp} Because {temp} is less than {value}')

                return deleted
            
    elif command == 'MD':
        if len(s) > 1:
            value = int(s[1])

            if len(stack) <= 0:
                return '-1'
            else:
                deleted = []
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] > value:
                        temp = stack.pop(i)
                        deleted.append(f'Delete = {temp} Because {temp} is more than {value}')

                return deleted
                
    
lst = [e for e in input('Enter Input : ').split(',')]
stack = []

for i in lst:
    result = ManageStack(stack, i)
    if type(result) == list:
        for i in result:
            print(i)
    elif result is not None:
        print(result)

print('Value in Stack =', stack)