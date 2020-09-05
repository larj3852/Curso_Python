"""
Google Text Speach
INFO:   https://buildmedia.readthedocs.org/media/pdf/gtts/latest/gtts.pdf

Todos los idiomas:   $ pgtts-cli --all
"""
#%% Librearias
from gtts import  gTTS
from playsound import playsound

#%% Guardar archivo en mp3
Archivo = "wenas.mp3"
tts = gTTS("uuuuuuueeeeeeennas",lang="es-us")
tts.save(Archivo)

#%% Concatenacion voz con archivo open
tts = gTTS("Abriendo Archivo con el metodo open",lang="es-us")
with open("2-ArchivoOpen.mp3","wb") as archivo:
    tts.write_to_fp(archivo)

# %% Escritura en distintos idiomas
tts_e = gTTS("I am speaking in english",lang="en")
tts_s = gTTS("Estoy hablando español",lang="es-us")
tts_f = gTTS("Bonsoir, Je m'appele Claude",lang="fr")
with open("3-DistintosIdiomas.mp3","wb") as archivo3:
    tts_e.write_to_fp(archivo3)
    tts_s.write_to_fp(archivo3)
    tts_f.write_to_fp(archivo3)


# %% Reproducir en python
playsound("wenas.mp3")

# %% Velocidad del texto
tts5 = gTTS("Estoy hablando mas lento",lang="es-us",slow=)
tts5.save("5 - Hablando lento")


# %%
