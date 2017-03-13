import os

base = '/home/august/data/VOCdevkit_STEAMWORKS/GearData'
for fname in os.listdir(base + '/Annotations'):
    if "_out" in fname:
        try:
            idx = fname.index("_out")
        except Exception as e:
            continue
        folder = fname[:idx] + '/'
        img_name = fname[idx+1:].replace('.xml', '.jpg')
    else:
        folder = ''
        img_name = fname.replace(".xml", ".jpg")

    first = 'GearData/JPEGImages/' + folder + img_name
    second = 'GearData/Annotations/' + fname
    print(first + ' ' + second)
