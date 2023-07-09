def Rshift(num, shift):
    if num >= 0 and num<=shift:
        return 0
    
    binary_num = bin(num & 0xFFFFFFFF)  # Convert num to 32-bit binary string
    shifted_num = int(binary_num[:-shift], 2)  # Perform right shift operation
    
    if num < 0:
        one_in_binary = bin(1 & 0xFFFFFFFF)
        shifted_temp = int(one_in_binary + '0' * (32-shift), 2)  # Perform left shift operation
        shifted_num = shifted_num - shifted_temp  # Adjust for negative numbers
    
    return shifted_num


n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))