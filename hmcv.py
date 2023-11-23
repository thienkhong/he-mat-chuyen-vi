def permute(arr, perm):
    return [arr[i - 1] for i in perm]

def encode(plain_text, perm):
    plain_text = plain_text.replace(" ", "")
    n = len(plain_text)
    m = len(perm)
    k = n // m
    cipher_text = ""
    for i in range(k):
        block = plain_text[i * m : (i + 1) * m]
        cipher_text += "".join(permute(block, perm))
    return cipher_text

def decode(cipher_text, perm_inv):
    n = len(cipher_text)
    m = len(perm_inv)
    k = n // m
    plain_text = ""
    for i in range(k):
        block = cipher_text[i * m : (i + 1) * m]
        plain_text += "".join(permute(block, perm_inv))
    return plain_text

plain_text = "asecondclasscarriageonthetrain"
perm = [3, 5, 1, 6, 4, 2]
perm_inv = [3, 6, 1, 5, 2, 4]
cipher_text = encode(plain_text, perm)
print(f"Mã hóa: {cipher_text}")
plain_text = decode(cipher_text, perm_inv)
print(f"Giải mã: {plain_text}")