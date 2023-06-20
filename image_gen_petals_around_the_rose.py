from PIL import Image, ImageDraw, ImageFont
import random

def drawCircle(x, y, r, TrueOrFalse):
    global Dot_Color, BG_Color
    r = int(r / 2) + 1
    try:
        for i in range(-r, r):
            for j in range(-r, r):
                if i**2 + j**2 <= (r * 0.95)**2:
                    if TrueOrFalse:
                        pixel[i + x, j + y] = Dot_Color
                    else:
                        pixel[i + x, j + y] = BG_Color
                else:
                    pixel[i + x, j + y] = BG_Color
    except:
        return

    return

def drawDice(area, number):
    global size1, Buffer
    diceGrid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    if number == 1:
        diceGrid[1][1] = 1
    if number == 2:
        diceGrid[0][0] = diceGrid[2][2] = 1
    if number == 3:
        diceGrid[0][0] = diceGrid[1][1] = diceGrid[2][2] = 1
    #Does all four corners
    if number == 4 or number == 5 or number == 6:
        diceGrid[0][0] = diceGrid[0][2] = diceGrid[2][0] = diceGrid[2][2] = 1
    if number == 5:
        diceGrid[1][1] = 1
    if number == 6:
        diceGrid[1][0] = diceGrid[1][2] = 1

    sizeWithBuffer = size1[1] * (1 - Buffer)

    for i in range(0, 3):
        for j in range(0, 3):
            if diceGrid[i][j] == 1:
                drawCircle(area + j * (sizeWithBuffer / 3) + (size1[1] * Buffer * 0.5) + (sizeWithBuffer / 6), i * (sizeWithBuffer / 3) + (sizeWithBuffer / 6) + (size1[1] * Buffer * 0.5), (sizeWithBuffer / 3), True)
            else:
                drawCircle(area + j * (sizeWithBuffer / 3) + (size1[1] * Buffer * 0.5) + (sizeWithBuffer / 6), i * (sizeWithBuffer / 3) + (sizeWithBuffer / 6) + (size1[1] * Buffer * 0.5), (sizeWithBuffer / 3), False)
    return

# def drawNum():

size1 = (1000, 200)
size2 = (1200, 200)
Dot_Color = (0, 0, 0, 255)
BG_Color = (255, 255, 255, 255)
#Percent
Buffer = 0.05

#fnt = ImageFont.truetype(font="Lobster-Regular.ttf", size=200)
#fnt = ImageFont.truetype(font="1942.ttf", size=150)
fnt = ImageFont.truetype(font="Selectric Script.ttf", size=200)

for imageNo in range(1, int(input("Amount to Generate: ")) + 1):

    image = Image.new("RGBA", size1, (255, 150, 180, 175))
    pixel = image.load()

    pedalTotal = 0

    numbers = []

    for i in range(5):
        randno = random.randint(1, 6)
        # randno = 5
        drawDice(size1[1] * i, randno)
        numbers.append(randno)
        if randno == 5 or randno == 3:
            pedalTotal += (randno - 1)

    image.save("Image {} Hid.png".format(imageNo))


    image = Image.new("RGBA", size2, (255, 150, 180, 175))
    pixel = image.load()

    d = ImageDraw.Draw(image)

    for i in range(5):
        drawDice(size1[1] * i, numbers[i])

    if len(str(pedalTotal)) == 2:
        d.text((size1[1] * 5, -(size1[1] / 6) * 0), str(pedalTotal), font=fnt, fill=(0, 0, 0, 255))
    else:
        d.text((size1[1] * 5.25, -(size1[1] / 6) * 0), str(pedalTotal), font=fnt, fill=(0, 0, 0, 255))

    image.save("Image {} View.png".format(imageNo))

    print("Image No{} is Done! With {} Pedals".format(imageNo, pedalTotal))

