import pygame
import sys
import os

class Game:
    def __init__(self):
        pygame.init()
        self.originalTileSize = 16
        self.scale = 3
        self.tileSize = self.originalTileSize * self.scale
        self.maxScreenCol = 50
        self.maxScreenRow = 50
        self.screenWidth = 16 * self.tileSize
        self.screenHeight = 12 * self.tileSize 
        self.realScreenWidth = self.maxScreenCol * self.tileSize
        self.realScreenHeight = self.maxScreenRow * self.tileSize
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("TileTXT")

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.imagesName,self.images = self.load_images()
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 16)
        self.map = [[0 for _ in range(self.maxScreenRow)] for _ in range(self.maxScreenCol)]
        self.mapObject = [[-1 for _ in range(self.maxScreenRow)] for _ in range(self.maxScreenCol)]
        self.load_map("MAPA.txt")
        self.load_mapObject("MAPAObject.txt")

        self.block = 0
        self.maxBlocks = len(self.images) - 1
        self.mouseClick = False
        self.mX, self.mY = (0, 0)
        self.brushLenght = 1

        self.camera_x, self.camera_y = 0, 0
        self.zoom = 1

    def load_images(self):
        base_paths = ["res/objects","res/Tiles"]
        names=[]
        paths = []
        for base_path in base_paths:
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    if file.endswith('.png'):
                        #GET PATHS
                        path = root.replace("\\","/") +"/" + file
                        paths.append(path)

                        #GET NAMES
                        fileName,_ = os.path.splitext(file)
                        fileName = fileName.split("_")[1].capitalize()
                        names.append((fileName,base_path))

        images = [pygame.image.load(path) for path in paths]
        images = [pygame.transform.scale(img, (self.tileSize, self.tileSize)) for img in images]
        return names,images

    def load_map(self, filename):
        with open(filename, "r") as f:
            for i, col in enumerate(f):
                line = col.split(" ")
                for row, k in enumerate(line):
                    self.map[row][i] = int(k)
    
    def load_mapObject(self, filename):
        with open(filename, "r") as f:
            for i, col in enumerate(f):
                line = col.split(" ")
                for row, k in enumerate(line):
                    self.mapObject[row][i] = int(k)

    def draw_cells(self):
        # TILES
        for x, rows in enumerate(self.map):
            for y, ind in enumerate(rows):
                xx = round((x * self.tileSize - self.camera_x) * self.zoom)
                yy = round((y * self.tileSize - self.camera_y) * self.zoom)
                cell_size = round(self.tileSize * self.zoom)
                if 0 <= ind < len(self.images):
                    img = pygame.transform.scale(self.images[ind], (cell_size, cell_size))
                    self.screen.blit(img, (xx, yy))
                rect = pygame.Rect(xx, yy, cell_size, cell_size)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

        # OBJECTS
        for x, rows in enumerate(self.mapObject):
            for y, ind in enumerate(rows):
                xx = round((x * self.tileSize - self.camera_x) * self.zoom)
                yy = round((y * self.tileSize - self.camera_y) * self.zoom)
                cell_size = round(self.tileSize * self.zoom)
                if 0 <= ind < len(self.images):
                    img = pygame.transform.scale(self.images[ind], (cell_size, cell_size))
                    self.screen.blit(img, (xx, yy))
                rect = pygame.Rect(xx, yy, cell_size, cell_size)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

    def paint(self, wd):
        xx = int((self.mX / self.zoom + self.camera_x) // self.tileSize)
        yy = int((self.mY / self.zoom + self.camera_y) // self.tileSize)
        if 0 <= xx < self.maxScreenCol and 0 <= yy < self.maxScreenRow:
            if wd == 1:
                if "Tiles" in self.imagesName[self.block][1]:
                    self.map[xx][yy] = self.block
                else:
                    self.mapObject[xx][yy] = self.block
            else:
                for i in range(-wd + 1, wd):
                    for j in range(-wd + 1, wd):
                        xw = xx + i
                        yw = yy + j
                        if 0 <= xw < self.maxScreenCol and 0 <= yw < self.maxScreenRow:
                            if "Tiles" in self.imagesName[self.block][1]:
                                self.map[xw][yw] = self.block
                            else:
                                self.mapObject[xw][yw] = self.block

    def save(self):
        stringTile = ""
        stringObject = ""
        for r in range(self.maxScreenRow):
            for c in range(self.maxScreenCol):

                stringTile += str(self.map[c][r]) + " "

                stringObject += str(self.mapObject[c][r]) + " "

            stringTile = stringTile[:-1]
            stringObject = stringObject[:-1]
            stringTile += "\n"
            stringObject += "\n"
        stringObject = stringObject[:-1]
        stringTile = stringTile[:-1]
        with open("MAPA.txt", "w") as f:
            f.write(stringTile)
        with open("MAPAObject.txt", "w") as f:
            f.write(stringObject)
        print("CREATED")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouseClick = True
                    if event.button == 2:
                        self.save()
                    elif event.button == 4:
                        if self.block < self.maxBlocks:
                            self.block += 1
                    elif event.button == 5:
                        if self.block > 0:
                            self.block -= 1
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.mouseClick = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.camera_y >= 0:
                        self.camera_y -= self.tileSize
                    elif event.key == pygame.K_DOWN and self.camera_y <= self.realScreenHeight:
                        self.camera_y += self.tileSize
                    elif event.key == pygame.K_LEFT and self.camera_x >= 0:
                        self.camera_x -= self.tileSize
                    elif event.key == pygame.K_RIGHT and self.camera_x <= self.realScreenWidth:
                        self.camera_x += self.tileSize
                    elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                        self.zoom = min(self.zoom + 0.2, self.scale)
                        self.zoom = round(self.zoom, 2)
                    elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                        self.zoom = max(self.zoom - 0.2, 0.2)
                        self.zoom = round(self.zoom, 2)
                    elif event.key == pygame.K_p:
                        xx = int((self.mX / self.zoom + self.camera_x) // self.tileSize)
                        yy = int((self.mY / self.zoom + self.camera_y) // self.tileSize)
                        print(xx, yy)

            self.mX, self.mY = pygame.mouse.get_pos()
            texto_mouse = self.font.render(f"BLOCK: {self.imagesName[self.block][0]} ZOOM:{self.zoom} CAM({self.camera_x},{self.camera_y})", True, self.BLACK)
            if self.mouseClick:
                self.paint(self.brushLenght)
            self.screen.fill(self.WHITE)
            self.draw_cells()
            self.screen.blit(texto_mouse, (self.mX, self.mY))
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
