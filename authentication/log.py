from passlib.context import CryptContext
p_context= CryptContext(schemes="bcrypt", deprecated="auto")

plain =input("enter the passord:")
hashed = p_context.hash(plain)

print(f"plani:{plain}")
print(f"hashed:{hashed}")
pas=input("enter password to verify: ")

is_correct= p_context.verify(pas, hashed)
print(f"password corrected:{is_correct}")

is_wrong= p_context.verify(pas, hashed)
print(f"wrong password:{is_wrong}")

hash1 =p_context.hash("pas")
hash2 =p_context.hash("pas")

print(hash1 == hash2)
print(p_context.verify("pas", hash1))
print(p_context.verify("pas", hash1))