import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *
import sys

def main():
    pygame.init()

   # Inicializar la pantalla
    Tamaño_pantalla = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption(titulo)

    mostrar_portada = toleportada(3)

    if mostrar_portada:
        iniciar_juego = tolemenu()

        if iniciar_juego:
            print("sisas")
             
            # Crear una instancia del fondo base
            fondo = FondoBase()

            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                screen.blit(fondo.image, fondo.rect)
                pygame.display.update()
    
if __name__ == "__main__":
    main()

