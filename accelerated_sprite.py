import pygame
import math
pygame.init()
class Object:
    def __init__(self,**kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.velocity_ = kwargs['vel']
        self.angle = 0
        self.velocity = 0
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.image = pygame.image.load(kwargs["image"]).convert_alpha()
        self.angularvel = kwargs["angularvel"]
        self.acceleration = kwargs["acceleration"]
    def show(self,window):
        img = pygame.transform.rotozoom(self.image,-self.angle,1).convert_alpha()
        imgr = img.get_rect(center = self.rect.center)
        window.blit(img,imgr)

    def move(self,win_w,win_h):
        if self.rect.x >= win_w-self.width :
            self.rect.x = win_w-self.width
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y >= win_h-self.height :
            self.rect.y = win_h-self.height
        if self.rect.y <= 0:
            self.rect.y = 0
        self.rect.x += self.velocity*math.cos(self.angle*(math.pi/180))
        self.rect.y += self.velocity*math.sin(self.angle*(math.pi/180))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not self.velocity >= self.velocity_:
                self.velocity += self.acceleration
        if keys[pygame.K_DOWN]:
            if not self.velocity <= -self.velocity_:
                self.velocity -= self.acceleration
        if keys[pygame.K_RIGHT]:
            self.angle += self.angularvel
        if keys[pygame.K_LEFT]:
            self.angle -= self.angularvel
        if keys[pygame.K_SPACE]:
            self.velocity = 0



width = 1200
height = 700
dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("Thrust Mechanics")
clock = pygame.time.Clock()
fps  = 60
rect = Object(x = 100, y = 300, width=50, height=50, vel=15, image="untitled.png"
              , angularvel = 4, acceleration=0.125)
rect.rect.center = width//2,height//2
run = True
while run:
    dis.fill((0,0,0))
    rect.show(dis)
    rect.move(width,height)
    rect.update()
    clock.tick(fps)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                run = False
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
