import pygame
from time import time
from ruta.assets.herramientas import *
from ruta.figuras import *


class AudioPregunta:
    def __init__(self, audio, letraRespuesta):
        pygame.mixer.init()
        self.audio = pygame.mixer.Sound(obtenerPathAbsoluto(audio, __file__))
        self.letraRespuesta = letraRespuesta
        self.estadoReproducion = True

    def reproducir(self, camino, opciones):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] and camino.notificar() == False:
            self.estadoReproducion = False
            for opcion in opciones:
                if opcion.obtenerVisibilidad() == False:
                    opcion.setVisibilidad(True)
        
        if self.estadoReproducion and camino.notificar() == False:
            self.audio.play()

        if self.estadoReproducion == False and camino.notificar() == False:
            pygame.mixer.stop()
    
    def setEstadoReproducido(self, value):
        self.estadoReproducion = value
    
    def obtenerLetraRespuesta(self):
        return self.letraRespuesta


class ListaAudiosPreguntas:

    _preguntas = []

    def añadirAudioPregunta(self, pregunta):
        if isinstance(pregunta, AudioPregunta):
            self._preguntas.append(pregunta)

    def quitarAudioPregunta(self, pregunta):
        self._preguntas.remove(pregunta)
    
    def obtenerAudiosPreguntas(self):
        return self._preguntas