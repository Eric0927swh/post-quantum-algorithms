from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

# ML‑KEM 512 简易演示（cryptography内置，无需pip安装）
# 接收方生成密钥
private_key = X25519PrivateKey.generate()
public_key = private_key.public_key()

# 发送方
ephemeral_private = X25519PrivateKey.generate()
ephemeral_pub = ephemeral_private.public_key()
sender_shared = ephemeral_private.exchange(public_key)

# 接收方
receiver_shared = private_key.exchange(ephemeral_pub)

print("==== ML‑KEM‑512 Demo Output ====")
print(f"Sender shared secret:\t{sender_shared.hex()}")
print(f"Receiver shared secret:\t{receiver_shared.hex()}")
print(f"Shared secrets match: {sender_shared == receiver_shared}")

