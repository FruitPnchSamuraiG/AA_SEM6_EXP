import string

def to_split(array):
    new_final = []  
    i = 0

    while i < len(array):
        sub_list = []

        # Check if there is another letter for pairing
        if i + 1 < len(array):
            # Check for consecutive same letters within the same 2-pair split
            if array[i] == array[i + 1]:
                sub_list.extend([array[i], 'X'])
                i += 1  # Move to the next pair
            else:
                sub_list.extend([array[i], array[i + 1]])
                i += 2  # Move to the next pair
        else:
            # Handle the case when there is an odd number of letters
            sub_list.extend([array[i], 'X'])
            i += 1  # Move to the next pair

        new_final.append(sub_list)

    print(new_final)
    return new_final


key = input("Enter key: ")
key = key.replace('J', 'I').upper()  # Convert to uppercase and replace J with I
key_set = []
for i in key:
    if i not in key_set:
        key_set.append(i)


def create_matrix():
    alphabet = [letter for letter in string.ascii_uppercase if letter != 'J']
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Fill in the matrix with the sorted key
    row = col = 0
    for i in range(len(key_set)):
        row = i // 5
        col = i % 5
        matrix[row][col] = key_set[i]
    print(row,col)

    j = 0
    for letter in key_set:
        alphabet.remove(letter)
    # Fill in the rest of the matrix with the remaining alphabet
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == '':
                matrix[row][col] = alphabet[j]
                j+=1  # Update key_set to include the new letter
                        
    return matrix

result_matrix = create_matrix()

# Display the result
for row in result_matrix:
    print(row)

plaintext = input("Enter plaintext: ").upper().replace('J', 'I')
plaintext_pairs = to_split(plaintext)

def find_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return [i, j]

ciphered_pairs = []

for pair in plaintext_pairs:
    char1, char2 = pair[0], pair[1]
    pos1 = find_position(char1, result_matrix)
    pos2 = find_position(char2, result_matrix)
    
    if pos1[0] == pos2[0]:  # for same row
        ciphered_pairs.append([result_matrix[pos1[0]][(pos1[1] + 1) % 5], result_matrix[pos2[0]][(pos2[1] + 1) % 5]])
        
    elif pos1[1] == pos2[1]:  # for same column
        ciphered_pairs.append([result_matrix[(pos1[0] + 1) % 5][pos1[1]], result_matrix[(pos2[0] + 1) % 5][pos2[1]]])
        
    else:  # for different rows and columns
        ciphered_pairs.append([result_matrix[pos1[0]][pos2[1]], result_matrix[pos2[0]][pos1[1]]])

cipher_text = ''.join([''.join(pair) for pair in ciphered_pairs])
print("The cipher text is:", cipher_text)
