import pygame
import os
import sys
import random
import time

pygame.init()
CLOCK = pygame.time.Clock()
pygame.mixer.init()

width = 800
height = 800
position = 350
x = 0
y = 0
scene = pygame.display.set_mode((width, height))
menu = pygame.transform.scale(pygame.image.load('menu.JPG'), (800, 800))
start1 = pygame.transform.scale(pygame.image.load('taptostart.JPG'),(250, 100))
start2 = pygame.transform.scale(pygame.image.load('taptostartdark.JPG'),(250, 100))
end = pygame.transform.scale(pygame.image.load('gameover.JPG'),(800, 800))
button1 = pygame.transform.scale(pygame.image.load('continue.JPG'),(250, 100))
button2 = pygame.transform.scale(pygame.image.load('exit.JPG'),(250, 100))
road = pygame.transform.scale(pygame.image.load('road.JPG'),(400, 800))
grass = pygame.transform.scale(pygame.image.load('grass.JPG'),(275, 800))
ball = pygame.transform.scale(pygame.image.load('ball.PNG'),(110, 110))
tree1 = pygame.transform.scale(pygame.image.load('tree1.PNG'),(150, 200))
tree2 = pygame.transform.scale(pygame.image.load('tree2.PNG'),(150, 200))
tree3 = pygame.transform.scale(pygame.image.load('tree3.PNG'),(150, 200))
car1 = pygame.transform.scale(pygame.image.load('car1.PNG'),(100, 200))
car2 = pygame.transform.scale(pygame.image.load('car2.PNG'),(100, 200))
car3 = pygame.transform.scale(pygame.image.load('car3.PNG'),(100, 200))
car4 = pygame.transform.scale(pygame.image.load('car4.PNG'),(100, 250))
car5 = pygame.transform.scale(pygame.image.load('car5.PNG'),(100, 200))
volumeoff = pygame.transform.scale(pygame.image.load('volumeoff.JPG'),(70, 70))
volumeoffdark = pygame.transform.scale(pygame.image.load('volumeoffdark.JPG'),(70, 70))
continuedark = pygame.transform.scale(pygame.image.load('continuedark.JPG'),(250, 100))
exitdark = pygame.transform.scale(pygame.image.load('exitdark.JPG'),(250, 100))

current_image = start1
current_image1 = volumeoff
current_image2 = button1
current_image3 = button2
cars = [car1, car2, car3, car4, car5]
random_car = random.choice(cars)
trees = [tree1, tree2, tree3]
random_tree = random.choice(trees)
random_tree2 = random.choice(trees[0:2])

font = pygame.font.SysFont(None, 40)
read = open('highscore.txt', 'r')
topScore = float(read.readline())
read.close()

swish = pygame.mixer.Sound("swish.ogg")
pygame.mixer.music.load('song.MP3')
pygame.mixer.music.play(-1)

def start():
    while(1):
        global current_image, current_image1
        scene.blit(menu, (0, 0))
        scene.blit(current_image, (270, 600))
        scene.blit(current_image1, (45, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if(270 < mouse[0] < 470 and 500 < mouse[1] < 710):
            current_image = start2
            if click[0] == 1:
                return 1
        else:
            current_image = start1
        if(45 < mouse[0] < 100 and 20 < mouse[1] < 150):
            current_image1 = volumeoffdark
            if click[0] == 1:
                pygame.mixer.music.stop()
        else:
            current_image1 = volumeoff
        pygame.display.update()
        command = pygame.event.poll()
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()
def gameover():
    while(1):
        global current_image2
        global current_image3
        scene.blit(end, (0, 0))
        scene.blit(current_image2, (100, 600))
        scene.blit(current_image3, (450, 600))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if(100 < mouse[0] < 300 and 600 < mouse[1] < 650):
            current_image2 = continuedark
            if click[0] == 1:
                return 1
        else:
            current_image2 = button1
        if(450 < mouse[0] < 650 and 600 < mouse[1] < 650):
            current_image3 = exitdark
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            current_image3 = button2
        pygame.display.update()
        command = pygame.event.poll()
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()
start()

while(1):
    a = 0
    b = 0
    fps = 40
    fps_change = 0
    score = 0
    running = 1
    obstacle = random.randint(0, 6)
    while (running):
        i = 0
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if position == 615:
                    pygame.mixer.Sound.play(swish)
                    position = 115
                else:
                    pygame.mixer.Sound.play(swish)
                    position = position + 250
            if event.key == pygame.K_a:
                if position == 115:
                    pygame.mixer.Sound.play(swish)
                    position = 615
                else:
                    pygame.mixer.Sound.play(swish)
                    position = position - 250

        rel_y = y%road.get_rect().height
        scene.blit(road, (200, rel_y - road.get_rect().height))
        if(rel_y < height):
            scene.blit(road, (200, rel_y))
        scene.blit(grass, (10, rel_y - grass.get_rect().height))
        if(rel_y < height):
            scene.blit(grass, (10,rel_y))
        scene.blit(grass,(515,rel_y - grass.get_rect().height))
        if(rel_y < height):
            scene.blit(grass, (515,rel_y))
        y += 10
        
        scene.blit(ball,(position, 650))
        if(obstacle == 0):
            scene.blit(random_tree, (30, a-500))
            a += 10
            if(a > 1300):
                a = 0
                random_tree = random.choice(trees)
                obstacle = random.randint(0, 6)
            if (position == 100 and a-500 == 500 ):
                running = 0
        if(obstacle == 1):
            scene.blit(random_car, (350, a-200))
            a += 15
            if(a > 900):
                a = 0
                random_car = random.choice(cars)
                obstacle = random.randint(0, 6)
            if(position == 350 and a - 200 >= 415 and a - 200 <= 550):
                running = 0
        if(obstacle == 2):
            scene.blit(random_tree2, (550, a-500))
            a += 10
            if(a > 1300):
                a = 0
                random_tree2 = random.choice(trees[0:2])
                obstacle = random.randint(0, 6)
            if(position == 600 and a-500 == 500):
                running = 0
        if(obstacle == 3):
            scene.blit(random_tree2, (550, a-500))
            scene.blit(random_tree, (30, a-500))
            a += 10
            if(a > 1300):
                chek = 1
                a = 0
                random_tree = random.choice(trees)
                random_tree2 = random.choice(trees[0:2])
                obstacle = random.randint(0, 6)
            if((position == 600 and a-500 == 500) or (position == 100 and a-500 == 500)):
                running = 0
        if(obstacle == 4):
            scene.blit(random_car, (350, b-200))
            b += 15
            scene.blit(random_tree, (30, a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_tree = random.choice(trees)
                random_car = random.choice(cars)
                obstacle = random.randint(0, 6)
            if((position == 350 and b-200 >= 415 and b-200 <= 550) or (position == 100 and a-500 == 500)):
                running = 0
        if(obstacle == 5):
            scene.blit(random_car,(350, b-200))
            b += 15
            scene.blit(random_tree2,(550, a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_tree2 = random.choice(trees[0:2])
                random_car = random.choice(cars) 
                obstacle = random.randint(0, 6)
            if((position == 350 and b-200 >= 415 and b-200 <= 550) or (position == 600 and a-500 == 500)):
                running = 0
        if(obstacle == 6):
            scene.blit(random_car,(350,b-200))
            b += 15
            scene.blit(random_tree,(30,a-500))
            scene.blit(random_tree2,(550,a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_tree = random.choice(trees)
                random_tree2 = random.choice(trees[0:2])
                random_car = random.choice(cars)
                obstacle = random.randint(0,6)
            if((position == 350 and b-200 >= 415 and b-200 <= 550) or ((position == 100 or position == 600) and a-500 == 500)):
                running = 0

        score += 0.1
        score_value = font.render('Score: ' + str(round(score, 2)), 1, (0, 0, 0))
        high_score = font.render('Top score: ' + str(round(topScore, 2)), 1, (0, 0, 0))
        scene.blit(score_value,(10,10))
        scene.blit(high_score,(10,40))
        pygame.display.update()
        fps_change += 1
        if(fps_change%200 == 0):
            fps += 5
        CLOCK.tick(fps)
        if score > topScore:
            Change=open("highscore.txt",'w')
            Change.write(str(score))
            Change.close()
            topScore = score
    gameover()