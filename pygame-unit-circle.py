import pygame, math

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont("consolas", 18)

x,y = 400,300
theta = 0
s = 4

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60) # cap at 60FPS
    get_fps = int(clock.get_fps())

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    k = pygame.key.get_pressed()

    # rotation
    if k[pygame.K_d]:
        theta -= 0.05

    if k[pygame.K_a]:
        theta += 0.05

    # movement
    # important fix: y screen = -y math
    if k[pygame.K_w]:
        x += math.cos(theta) * s
        y -= math.sin(theta) * s

    if k[pygame.K_s]:
        x -= math.cos(theta) * s
        y += math.sin(theta) * s

    screen.fill((150,150,150))

    # player circle
    pygame.draw.circle(screen, (0,0,0), (int(x),int(y)), 10)

    # player arrow
    px = x + math.cos(theta) * 45
    py = y - math.sin(theta) * 45
    pygame.draw.line(screen, (255,0,0), (px,py), (x,y), 3)

    # unit circle
    pygame.draw.circle(screen, (100,100,100), (400,300), 200, 3)

    # unit circle arrow
    ux = 400 + math.cos(theta) * 200
    uy = 300 - math.sin(theta) * 200
    pygame.draw.line(screen, (255,0,0), (400,300), (ux,uy), 3)

    # stats
    fps = font.render(f"FPS {get_fps}", True, (0,0,0))
    vec = font.render(f"vector (cos(theta),sin(theta)) ({round(math.cos(theta),5)}, {round(math.sin(theta),5)})", True, (0,0,0))
    theta_rad = font.render(f"theta {round(theta, 5)} rad", True, (0,0,0))
    theta_deg = font.render(f"theta {round(math.degrees(theta), 5)} deg", True, (0,0,0))

    screen.blit(fps, (20, 20))
    screen.blit(vec, (20, 45))
    screen.blit(theta_rad, (20, 70))
    screen.blit(theta_deg, (20, 95))

    pygame.display.update()

pygame.quit()


