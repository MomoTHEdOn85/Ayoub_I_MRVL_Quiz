from PIL import Image
from components import vars 

def total(value):

    if value <= 90:
        vars.characters = vars.characters[0]
        print("It's " + vars.characters)
        images = Image.open("thor.jpg")
        images.show()

    elif value == 180:
        vars.characters = vars.characters[1]
        print("It's " + vars.characters)
        images = Image.open("cap_america.jpg")
        images.show()

    elif value == 230:
        vars.characters = vars.characters[2]
        print("It's " + vars.characters)
        images = Image.open("hulk.jpg")
        images.show()
        

    elif value == 300:
        vars.characters = vars.characters[3]
        print("It's " + vars.characters)
        images = Image.open("black_widow.jpeg")
        images.show()

    else:
        print("Sorry we don't know who you are!")

    

        