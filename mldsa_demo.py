from dilithium_py.ml_dsa import ML_DSA_65

# Generate ML-DSA key pair
pk, sk = ML_DSA_65.keygen()

print("Public key:", len(pk), "bytes")
print("Secret key:", len(sk), "bytes")

# Message to sign
message = b"Post-Quantum Cryptography"

# Sign the message
signature = ML_DSA_65.sign(sk, message)
print("Signature:", len(signature), "bytes")

# Verify the signature
valid = ML_DSA_65.verify(pk, message, signature)
print("Signature valid:", valid)

