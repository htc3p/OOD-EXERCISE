def count_characters(text):
    uppercase_letters = set()
    lowercase_letters = set()

    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                uppercase_letters.add(char)
                uppercase_count += 1
            else:
                lowercase_letters.add(char)
                lowercase_count += 1

    sorted_uppercase_letters = sorted(uppercase_letters)
    sorted_lowercase_letters = sorted(lowercase_letters)

    return uppercase_count, sorted_uppercase_letters, lowercase_count, sorted_lowercase_letters

print(" *** String count ***")
input_text = input("Enter message : ")
uppercase_count, sorted_uppercase_letters, lowercase_count, sorted_lowercase_letters = count_characters(input_text)

print("No. of Upper case characters :", uppercase_count)
print("Unique Upper case characters :", '  '.join(sorted_uppercase_letters))
print("No. of Lower case Characters :", lowercase_count)
print("Unique Lower case characters :", '  '.join(sorted_lowercase_letters))