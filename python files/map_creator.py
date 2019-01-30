from PIL import Image


def create_map(im_loc,im_save, b_thresh):
    # im = Image.open('networks/mesh_1000W_2m/0128210631_ABC.4326.png') # Can be many different formats.
    im = Image.open(im_loc)  # Can be many different formats.
    pix = im.load()
    print(im.size)
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            # if pix[x, y] != (255, 255, 255, 0) and (pix[x, y][0] >= 235):
            # if pix[x,y] != (255,255,255, 0) and (pix[x,y][0] > 0 or pix[x,y][2] <= 30):
            if pix[x, y] != (255, 255, 255, 0) and (pix[x, y][0] > 0 or pix[x, y][2] <= b_thresh):
                # print(pix[x, y])
                pix[x,y] = (255, 0, 0)
                # print(pix[x,y])
            else:
                pix[x, y] = (255, 255, 255, 0)
    # im.show()
    # im.save('networks/mesh_1000W_2m/0128225136_gav_1000W_2m.4326.png')  # Save the modified pixels as .png
    im.save(im_save)  # Save the modified pixels as .png

def create_cel_map(im_loc,im_save):
    # im = Image.open('networks/mesh_1000W_2m/0128210631_ABC.4326.png') # Can be many different formats.
    im = Image.open(im_loc)  # Can be many different formats.
    pix = im.load()
    print(im.size)
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if pix[x, y] != (255, 255, 255, 0) and (pix[x, y][0] >= 235):
            # if pix[x,y] != (255,255,255, 0) and (pix[x,y][0] > 0 or pix[x,y][2] <= 30):
            # if pix[x, y] != (255, 255, 255, 0) and (pix[x, y][0] > 0 or pix[x, y][2] <= b_thresh):
                # print(pix[x, y])
                pix[x,y] = (255, 0, 0)
                # print(pix[x,y])
            else:
                pix[x, y] = (255, 255, 255, 0)
    # im.show()
    # im.save('networks/mesh_1000W_2m/0128225136_gav_1000W_2m.4326.png')  # Save the modified pixels as .png
    im.save(im_save)  # Save the modified pixels as .png
