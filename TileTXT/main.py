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
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight + 50))  # Extra space for toolbar
        pygame.display.set_caption("TileTXT")

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)

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

        self.isBrush = True  # True for brush, False for eraser

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
            if self.isBrush:
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
            else:
                if wd == 1:
                    self.map[xx][yy] = -1
                    self.mapObject[xx][yy] = -1
                else:
                    for i in range(-wd + 1, wd):
                        for j in range(-wd + 1, wd):
                            xw = xx + i
                            yw = yy + j
                            if 0 <= xw < self.maxScreenCol and 0 <= yw < self.maxScreenRow:
                                self.map[xw][yw] = -1
                                self.mapObject[xw][yw] = -1

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

    def draw_toolbar(self):
        toolbar_height = 50
        pygame.draw.rect(self.screen, self.GRAY, (0, self.screenHeight, self.screenWidth, toolbar_height))
        
        brush_button_rect = pygame.Rect(10, self.screenHeight + 10, 100, 30)
        pygame.draw.rect(self.screen, self.WHITE if self.isBrush else self.BLACK, brush_button_rect)
        brush_text = self.font.render("Brush" if self.isBrush else "Eraser", True, self.BLACK if self.isBrush else self.WHITE)
        self.screen.blit(brush_text, (20, self.screenHeight + 15))

        # Block size buttons
        size_decrease_rect = pygame.Rect(130, self.screenHeight + 10, 30, 30)
        size_increase_rect = pygame.Rect(170, self.screenHeight + 10, 30, 30)
        pygame.draw.rect(self.screen, self.WHITE, size_decrease_rect)
        pygame.draw.rect(self.screen, self.WHITE, size_increase_rect)
        self.screen.blit(self.font.render("-", True, self.BLACK), (140, self.screenHeight + 15))
        self.screen.blit(self.font.render("+", True, self.BLACK), (180, self.screenHeight + 15))

        # Block size display
        block_size_text = self.font.render(f"Size: {self.brushLenght}", True, self.BLACK)
        self.screen.blit(block_size_text, (210, self.screenHeight + 15))

        
        # Display the selected image
        pygame.draw.rect(self.screen, self.block, (285, self.screenHeight, self.tileSize+10, toolbar_height))

        selected_image = pygame.transform.scale(self.images[self.block], (self.tileSize, self.tileSize))
        self.screen.blit(selected_image, (290, self.screenHeight+1))
        xx = int((self.mX / self.zoom + self.camera_x) // self.tileSize)
        yy = int((self.mY / self.zoom + self.camera_y) // self.tileSize)
        texto_mouse = self.font.render(f"ZOOM:{self.zoom}   CAM({self.camera_x},{self.camera_y})  MOUSE({xx},{yy})", True, self.BLACK)
        self.screen.blit(texto_mouse, (370, self.screenHeight+20))



    def handle_toolbar_events(self,):
        if 10 <= self.mX <= 110 and self.screenHeight + 10 <= self.mY <= self.screenHeight + 40:
            self.isBrush = not self.isBrush
        elif 130 <= self.mX <= 160 and self.screenHeight + 10 <= self.mY <= self.screenHeight + 40:
            self.brushLenght = max(1, self.brushLenght - 1)
            self.mouseClick = False
        elif 170 <= self.mX <= 200 and self.screenHeight + 10 <= self.mY <= self.screenHeight + 40:
            self.brushLenght = min(10, self.brushLenght + 1)
            self.mouseClick = False

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
                    

            self.mX, self.mY = pygame.mouse.get_pos()
            if self.mouseClick:
                if self.mY < self.screenHeight:
                    self.paint(self.brushLenght)
                self.handle_toolbar_events()
            self.screen.fill(self.WHITE)
            self.draw_cells()
            self.draw_toolbar()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
