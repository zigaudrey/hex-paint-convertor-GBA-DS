import os
import struct

from PIL import Image
from tkinter import filedialog

PAL_path = ""
PAL_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Pal File", filetype=(('BIN file', '*.bin'),("ALL file",'*.*')))

if len(PAL_path) != 0:
    PAL_open = open(PAL_path, 'rb')
    PAL_data = PAL_open.read()
    PAL_open.close()

    if len(PAL_data) == 32:

        PAL_List = []

        R, G, B = 0, 0, 0

        bin_hex = bytearray()
        for i in range(0,len(PAL_data),2):
            Dec_Color = struct.unpack("<L", PAL_data[i:i+2] + b'\x00\x00')[0]
            B = (Dec_Color // 32 // 32 % 32) * 8
            G = (Dec_Color // 32 % 32) * 8
            R = (Dec_Color % 32) * 8
            PAL_List.append((R, G, B))
        
        if PAL_List.count(PAL_List[0]) != 16:

            if PAL_List[0] in PAL_List[1:]:
                print("The first color is doubled. Change to (0, 224, 224).")
                PAL_List[0] = (0, 224, 224)
            
            BIN_name = ""
            BIN_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Sprite Bin File", filetype=(('BIN file', '*.bin'),("ALL file",'*.*')))

            if len(BIN_name) != 0:

                BIN_path = open(BIN_name, "rb")
                BIN_file = BIN_path.read()
                BIN_path.close()

                if len(BIN_file) % 32 == 0:

                    n=len(BIN_name)-5
                    SHORT_name = ""
                    while n!= 0 and BIN_name[n] != '/':
                        SHORT_name = BIN_name[n] + SHORT_name
                        n -= 1

                    tile_COUNT = 0

                    while tile_COUNT == 0:
                        tile_COUNT = int(input("Choose Tile Number (4 to 16)"))
                        if 4 > tile_COUNT or tile_COUNT > 16 :
                            tile_COUNT = 0

                    BIN_len = len(BIN_file) + (len(BIN_file) % (tile_COUNT * 32))
                    w = 8 * tile_COUNT
                    h = BIN_len // (tile_COUNT * 32) * 8

                    OUTCOME= Image.new('RGB', (w , h))

                    Pointer = 0
                    n1, n2 = 0 ,0
                    for y in range(0, h, 8):
                        for x in range (0, w, 8):
                            for iz in range(0, 8):
                                for ix in range(0, 8, 2):
                                    if Pointer < len(BIN_file):
                                        Hex_Data = struct.pack("B", BIN_file[Pointer])[0]
                                        n1 = Hex_Data // 16
                                        n2 = Hex_Data - (n1 * 16)
                                        OUTCOME.putpixel((x+ix,y+iz), PAL_List[n2])
                                        OUTCOME.putpixel((x+ix+1,y+iz), PAL_List[n1])
                                        Pointer += 1

                    if w == 32 and h == 32:
                        OUTCOME.save(SHORT_name + " DS Icon Img.png")
                    else:
                        OUTCOME.save(SHORT_name + "-" + str(tile_COUNT) + " Tiles GBA DS.png")

                    PAL_OUTCOME= Image.new('RGB', (8 , 2))

                    np = 0
                    for y in range(2):
                        for x in range(8):
                            PAL_OUTCOME.putpixel((x,y), PAL_List[np])
                            np += 1

                    PAL_OUTCOME.save(SHORT_name + " Pal.png")

                    print("Image and Pal Datas Files Done!")
                            
                else:
                    print("The Sprite Bin File isn't a divisible of 32")

            else:
                print("No Sprite File Selected")

        else:
            print("Palette File Empty")

    else:

        print("The Palette Bin file has to be 32 long")

else:
    print("No Palette File Selected")
