import pyscreenshot as ImageGrab

if __name__ == "__main__":
    def screenshot(x1,y1,x2,y2):
        im = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        im.show()

screenshot(0,0,5000,5000)