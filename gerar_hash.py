import bcrypt

senha = "123456".encode()

hash = bcrypt.hashpw(
    senha,
    bcrypt.gensalt()
)

print(hash.decode())