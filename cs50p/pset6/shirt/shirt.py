import os
import sys

valid_extensions = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]


def main():
    if not valid():
        sys.exit()
    #get_images()
    temp1 = os.path.splitext(sys.argv[1])
    print(temp1)
    print(temp1['ext'])


def get_images():
    images = []
    #for arg in sys.argv:
    #   image = Im


def valid():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments\nUsage: python shirt.py input output")
        return False
    elif len(sys.argv) > 3:
        print("Too many command-line arguments\nUsage: python shirt.py input output")
        return False
    #temp1 = splitext(sys.argv[1])
    #temp2 = splitext(sys.argv[2])
    #if temp1[1] != temp2[1]:
        #print("Input and output have different extensions")
        #return False
    #if temp1[1] not in valid_extensions and temp2[1] not in valid_extensions:
        #print("Invalid input or output extension(s)")
        #return False
    return True


if __name__ == "__main__":
    main()
