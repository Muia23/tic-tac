import pygame
from grid import Grid

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe client-2')

import threading

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

import socket

HOST = '127.0.0.1'
PORT = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def receive_data():
    while True:
        data = sock.recv(2048).decode() #blocking command 
        print(data)

create_thread(receive_data)


grid = Grid()

running = True
player = "x"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cellX, cellY = pos[0] // 200, pos[1] // 200               
                grid.get_mouse(cellX, cellY, player)
                send_data = '{}-{}'.format(cellX, cellY).encode()
                sock.send(send_data)
                if player == "x":
                    player = "o"                    
                else:
                    player = "x"

                grid.print_grid()

    surface.fill((0,0,0))

    grid.draw(surface)

    pygame.display.flip()