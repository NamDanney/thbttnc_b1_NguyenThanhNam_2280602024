class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key) + remaining
        matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "j" thành "i", thêm "x" nếu plain_text có độ dài lẻ
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            if i+1 >= len(plain_text):
                pair = (plain_text[i], 'X')
            else:
                pair = (plain_text[i], plain_text[i+1])
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = (cipher_text[i], cipher_text[i+1])
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        # Loại bỏ ký tự 'X' nếu không phải là ký tự cuối cùng và thay 'X' bằng 'J' nếu cần
        banro = ""
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + " " + decrypted_text[i+1]
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2] + decrypted_text[-1]
        return banro