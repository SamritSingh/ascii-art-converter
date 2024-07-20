from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # open and get image size
    img = Image.open(image)
    original_w, original_h = img.size
    print(f"Original Image Size: {original_w}x{original_h}")

    # resize image (downscale)
    img.resize((original_w // scale, original_h // scale)).save("resized.%s" % type)

    # open new image
    img = Image.open("resized.%s" % type)
    resized_w, resized_h = img.size  # get new width and height
    print(f"Resized Image Size: {resized_w}x{resized_h}")

    # list with correct length and height (same as resized image)
    grid = []
    for i in range(resized_h):
        grid.append(["X"] * resized_w)

    # load pixel data 
    pix = img.load()

    # pixel to ascii conversion, pixel brightness(sum of RGB values) to ASCII character
    for y in range(resized_h):
        for x in range(resized_w):
            if sum(pix[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x, y]) in range(1, 100):
                grid[y][x] = "X"
            elif sum(pix[x, y]) in range(100, 200):
                grid[y][x] = "%"
            elif sum(pix[x, y]) in range(200, 300):
                grid[y][x] = "&"
            elif sum(pix[x, y]) in range(300, 400):
                grid[y][x] = "*"
            elif sum(pix[x, y]) in range(400, 500):
                grid[y][x] = "+"
            elif sum(pix[x, y]) in range(500, 600):
                grid[y][x] = "/"
            elif sum(pix[x, y]) in range(600, 700):
                grid[y][x] = "("
            elif sum(pix[x, y]) in range(700, 750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "

    with open(saveas, "w") as art:
        for row in grid:
            art.write("".join(row) + "\n")

    print(f"ASCII art saved as '{saveas}'")

if __name__ == '__main__':
    # Create a Tkinter root window and hide it
    root = Tk()
    root.withdraw()

    # Ask the user to select an image file
    image_path = askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

    # If the user selected a file, proceed with the conversion
    if image_path:
        asciiConvert(image_path, "jpg", "output_ascii_art.txt", 1)
    else:
        print("No file selected!")
