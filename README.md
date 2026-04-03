```
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀```


## Analysis & Methodology

Zombie Zip is an evasion technique based on corrupting the header of a ZIP file. The antivirus program examines the header to determine the file’s contents and check for signatures that match its database.
If that’s the case, it flags it and declares it malicious. To look inside the compressed file, it must use the same method that was used for compression. In our case, that’s Stored.
So it will find our “eicar” file, which is flagged by antivirus software. To get around this, we compress the file ourselves using a different method (DEFLATE in our case) so that the antivirus encounters something that makes no sense to it.
This allows us to create something that bypasses the antivirus. To retrieve our payload, we can force our script to decompress the file using a specific method.

You can have fun analyzing the two files on VirusTotal. You’ll see how effective this evasion method is.

**Methods to use**:
```Compression Method = 0 (STORED)
Actual data = DEFLATE compressed```

**Malicious methods**:
```AV Engine:  Reads Method 0 → Scans compressed noise → No detection
Attacker:   Ignores Method field → Decompresses as DEFLATE → Recovers payload```

## Test

| File | VirusTotal |
|:----------|:------|
| eicar_flag.zip | 57/66 |
| zombie.zip | 0/64 |

## License 

MIT (For authorized security research only)
