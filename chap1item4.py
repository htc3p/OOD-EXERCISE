def num_grid(lst):
    rows = len(lst)
    cols = len(lst[0])
    
    # Create new matrix with the same size as the input matrix
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if lst[i][j] == "#":
                result[i][j] = "#"
            else:
                count = 0
                
                # Check around '#'
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (0 <= i + x < rows) and (0 <= j + y < cols) and lst[i + x][j + y] == "#":
                            count += 1
                result[i][j] = str(count)
    
    return result


lst_input = []

print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
    lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")