from pwn import *
from subprocess import check_output



r = process('./main2')
#r = remote("20.244.40.210", 6000)

cookies = check_output(["./result"]).decode().splitlines()

for i in range(100):
    print(f"Round ({i+1}/100)")
    print("Cookie:", cookies[i])
    r.sendline(cookies[i])
    print(r.recv().decode())


r.interactive()
