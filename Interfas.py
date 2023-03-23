from tkinter import*
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init()  #Iniciamos modulo de Pygame
#Funcion abrir cancion
def abrirarchivo():
    cancion = filedialog.askopenfilename() #Guardar el nombre de la cancion
    print(cancion)
    pygame.mixer.music.load(cancion)

def playsong():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def volmas():
    VolUp = pygame.mixer.music.get_volume()+0.5
    print(volmas)
    pygame.mixer.music.set_volume(VolUp)


def volMenos():
    VolLow = pygame.mixer.music.get_volume()-0.5
    print(volmas)
    pygame.mixer.music.set_volume(VolLow)


raiz = Tk() #Instanciar con objeto Tk
raiz.title("Reproductor MP3 _ GUI") #Asigna el titulo de la ventana
#raiz.iconbitmap("disk-jockey.ico")
raiz.geometry("500x500")
raiz.resizable(0,0)

# Crear fream
framePrincipal = Frame(raiz,bg="#4A4A4A")
framePrincipal.pack(fill="both",expand=1)         #FBFBFB                                    
#Etiqueta Titulo para el reproductor                                                 #bold es par negritas
tituloReproductor = Label(framePrincipal, text="ROCOLA KOMANDER", font=("Roboto",30,"bold"),bg="#4A4A4A",fg="#FBFBFB")
tituloReproductor.place(relx=0.12,rely=0.3)
#HACER LOS BOTONES     Boton de abror el son 1                                           fONT PARA CAMBIAR LA FUENTE
botonOpenSong = Button(framePrincipal,text="Open Song",bg="#42AB49",fg="#FBFBFB",font=("Roboto",15,"bold"),width=12,height=2,command=abrirarchivo)
botonOpenSong.place(relx=0.1,rely=0.5)
#Boton Play Song  2
botonPLaySong = Button(framePrincipal,text="Puchale pley",bg="#1DD4AA",fg="#FBFBFB",font=("Roboto",15,"bold"),width=12,height=2,command=playsong)
botonPLaySong.place(relx=0.1,rely=0.8)
#Stop   3
botonStop = Button(framePrincipal,text="Stop",bg="#1DD4AA",fg="#FBFBFB",font=("Roboto",15,"bold"),width=12,height=2,command=stop)
botonStop.place(relx=0.6,rely=0.5)
#Resume  4
botonResume = Button(framePrincipal,text="Resume",bg="#FF69B4",fg="#e2504c",font=("Roboto",15,"bold"),width=12,height=2,command=resume)
botonResume.place(relx=0.6,rely=0.8) 
#Pause
botonPause = Button(framePrincipal,text="Pause",bg="#1DD4AA",fg="#550099",font=("Roboto",15,"bold"),width=12,height=2,command=pause)
botonPause.place(relx=0.35,rely=0.65) 
#Volumen +
botonVolumenmas= Button(framePrincipal,text="Vol. +",bg="#808080",fg="#550099",font=("Roboto",15,"bold"),width=12,height=2,command=volmas)
botonVolumenmas.place(relx=0.15,rely=0.05)
#Volumen -
botonVolumenmenos = Button(framePrincipal,text="Vol. -",bg="#808080",fg="#550099",font=("Roboto",15,"bold"),width=12,height=2,command=volMenos)
botonVolumenmenos.place(relx=0.6,rely=0.05)  


raiz.mainloop()