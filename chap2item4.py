def find_zero_sum(arr):
    n = len(arr)
    if n<3:
        return 'Array Input Length Must More Than 2'
    
    arr.sort()
    final_list = []
    for i in range(n):

        # Initialize left and right pointers
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == 0:
                final_list.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                if arr[i]==0 and arr[left]==0 and arr[right]==0:
                    return final_list
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return final_list


lst = list(map(int, input("Enter Your List : ").split()))
print(find_zero_sum(lst))