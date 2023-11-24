from PIL import Image

class Basefilter:
    def __init__(self, *args, **kwargs):
        self.name = ""
        self.description = ""
class BlueFilter(Basefilter):
    def __init__(self):
        super().__init__()
        self.name = "Синий Фильтр"
        self.description = "Делает картину более синей"

    def apply(self, image: Image):
        for x in range(image.width):
            for y in range(image.height):
                r, g, b = image.getpixel((x, y))
                b = min(255, int(b * 2))
                image.putpixel((x, y), (r, g, b))
        return image