import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla y colores
ANCHO, ALTO = 600, 800
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Galaga en Python")
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Cargar imágenes
nave_img = pygame.image.load('nave.png')
enemigo_img = pygame.image.load('enemigo.png')
bala_img = pygame.image.load('bala.png')

# Parámetros de juego
velocidad_nave = 5
velocidad_bala = 7
velocidad_enemigo = 2
enemigos = []
balas = []
puntuacion = 0
vidas = 3
juego_activo = False  # Para manejar el estado del juego

# Configuración de fuentes
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 72)

# Clase de la Nave
class Nave:
    def __init__(self):
        self.image = nave_img
        self.rect = self.image.get_rect(center=(ANCHO // 2, ALTO - 50))
        self.velocidad = velocidad_nave

    def mover(self, dx):
        self.rect.x += dx
        # Limitar a los bordes
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.append(bala)

# Clase de los Enemigos
class Enemigo:
    def __init__(self, x, y):
        self.image = enemigo_img
        self.rect = self.image.get_rect(topleft=(x, y))

    def mover(self):
        self.rect.y += velocidad_enemigo
        if self.rect.top > ALTO:
            self.rect.y = -50
            self.rect.x = random.randint(0, ANCHO - self.rect.width)

# Clase de las Balas
class Bala:
    def __init__(self, x, y):
        self.image = bala_img
        self.rect = self.image.get_rect(center=(x, y))

    def mover(self):
        self.rect.y -= velocidad_bala
        if self.rect.bottom < 0:
            balas.remove(self)

# Función para manejar colisiones
def manejar_colisiones():
    global puntuacion
    for bala in balas:
        for enemigo in enemigos:
            if bala.rect.colliderect(enemigo.rect):
                balas.remove(bala)
                enemigos.remove(enemigo)
                puntuacion += 100
                enemigos.append(Enemigo(random.randint(0, ANCHO - enemigo_img.get_width()), random.randint(-100, -40)))
                break

# Pantalla de inicio
def pantalla_inicio():
    screen.fill(NEGRO)
    texto = fuente_grande.render("Galaga en Python", True, BLANCO)
    texto_iniciar = fuente.render("Presiona ENTER para iniciar", True, BLANCO)
    screen.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    screen.blit(texto_iniciar, (ANCHO // 2 - texto_iniciar.get_width() // 2, ALTO // 2 + 50))
    pygame.display.flip()

# Pantalla de fin de juego
def pantalla_fin():
    screen.fill(NEGRO)
    texto = fuente_grande.render("¡Juego Terminado!", True, BLANCO)
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    texto_reiniciar = fuente.render("Presiona R para reiniciar o ESC para salir", True, BLANCO)
    screen.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - 100))
    screen.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, ALTO // 2))
    screen.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 50))
    pygame.display.flip()

# Reiniciar el juego
def reiniciar_juego():
    global puntuacion, vidas, enemigos, balas, juego_activo
    puntuacion = 0
    vidas = 3
    enemigos = [Enemigo(random.randint(0, ANCHO - enemigo_img.get_width()), random.randint(-100, -40)) for _ in range(5)]
    balas.clear()
    juego_activo = True

# Crear instancias del juego
nave = Nave()
reiniciar_juego()

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    # Control de FPS
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if not juego_activo:
                if event.key == pygame.K_RETURN:
                    reiniciar_juego()
                elif event.key == pygame.K_r:
                    reiniciar_juego()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.key == pygame.K_SPACE:
                nave.disparar()

    # Pantalla de inicio o fin
    if not juego_activo:
        if vidas <= 0:
            pantalla_fin()
        else:
            pantalla_inicio()
        continue

    # Movimiento de la nave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        nave.mover(-nave.velocidad)
    if keys[pygame.K_RIGHT]:
        nave.mover(nave.velocidad)

    # Mover balas y enemigos
    for bala in balas:
        bala.mover()
    for enemigo in enemigos:
        enemigo.mover()

    # Manejar colisiones
    manejar_colisiones()

    # Verificar si algún enemigo ha pasado la nave
    for enemigo in enemigos:
        if enemigo.rect.bottom >= ALTO:
            vidas -= 1
            enemigos.remove(enemigo)
            enemigos.append(Enemigo(random.randint(0, ANCHO - enemigo_img.get_width()), random.randint(-100, -40)))
            if vidas <= 0:
                juego_activo = False

    # Dibujar fondo, nave, balas, enemigos y UI
    screen.fill(NEGRO)
    screen.blit(nave.image, nave.rect)
    for bala in balas:
        screen.blit(bala.image, bala.rect)
    for enemigo in enemigos:
        screen.blit(enemigo.image, enemigo.rect)
    
    # Mostrar puntuación y vidas
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
    screen.blit(texto_puntuacion, (10, 10))
    screen.blit(texto_vidas, (ANCHO - texto_vidas.get_width() - 10, 10))

    # Actualizar pantalla
    pygame.display.flip()
