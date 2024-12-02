code = bytearray([
    0xa9, 0xff,
    0x8d, 0x02, 0x60,
    
    0xa9, 0x55, 
    0x8d, 0x00, 0x60,

    0xa9, 0xaa,
    0x8d, 0x00, 0x60,

    0x4c, 0x05, 0x80,  #jump to 8000
])


rom = code + bytearray([0xea]* (32768-len(code)))


rom[0x7ffc]=0x00
rom[0x7ffd]=0x80


with open("rom.bin", "wb") as out_file:
    out_file.write(rom);
