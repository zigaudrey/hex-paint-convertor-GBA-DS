![Paint Hex Convertor GBA DS 16-Colors Icon BANNER](https://github.com/zigaudrey/hex-paint-convertor-GBA-DS/assets/129554573/5503bde3-7e5e-42f1-b81e-ede94acd75c0)
# Paint-Hex Convertor (Gameboy Advance/DS 16-colors)
Python Scripts that convert Picture into Bin file and vice-versa for GameBoy Advance, DS 16-Colors Sprites and Icon Editing.

## Ressource
### Gameboy Advance
* For the sprite, **use [CHR-YY](https://www.romhacking.net/utilities/119/) to locate** and create bin file with an Hex Editor. **Don't forget to mention the offset when you will replace in the ROM.**
* For the palette, **use [mGBA](https://mgba.io/) and open Tool > Game State View > Palette**. **The bytes pair are swapped** (eg: 01 EA to EA 01), **write them in order then use it to find the whole palette in the ROM.**
### DS (16-colors)
* **Use [Tinke](https://www.romhacking.net/utilities/817/) to extract NCGR and NCLR files.** The NCGR's header shows 03 00 00 00 like below.
![NCGR Header Depth Showing](https://github.com/zigaudrey/hex-paint-convertor-GBA-DS/assets/129554573/b12182d3-27ad-4fb5-8208-9957dcc6e3f8)
### DS Icon
* Use [Tinke](https://www.romhacking.net/utilities/817/) to extract the banner.bin. **The icon is at 20-21F(hex) and the palette is at 220-23F(hex).**

## Setups
1. If you don't have PIL, **open the command prompt and install it with PIP**
2. Open one of the scripts in **command prompt for PIL lib to work**

## Paint-to-hex Script
3. Choose a palette (image). **It have to have a total of 16 pixels**
3. Choose a sprite sheet (image). **Its dimensions should both be a divisible of 8**
3. **Two bin files will be created**, ready to replace data in the ROM or DS Files

## Hex-to-paint Script
3. Choose a palette (bin file). **Its lenght has to be 32**. If you use a NCLR palette with multiple palettes, **choose the right one to edit**
3. Choose a sprite sheet (bin file). **Its lenght has to be a divisble of 32 (one tile)**
3. **Choose the number of tiles for the width**
3. **Two images files will be created**, ready to be edited in drawing tools

## Update
* **15 December of 2023**: Added compatibility to Nitro DS files (Hex-to-paint) and ability to create them (Paint-to-hex).

## Similar Tool
+ [Paint-Hex Convertor (Sega Genesis/Megadrive)](https://github.com/zigaudrey/paint-hex-convertor-MSX)
+ [Paint - Hex Convertor DS-256 colors](https://github.com/zigaudrey/paint-hex-convertor-DS-256/tree/main)
