"""
Texto a voz con la libreria pyttsx3
INFO https://buildmedia.readthedocs.org/media/pdf/pyttsx3/latest/pyttsx3.pdf
PyAutoGUI 
DESCRIPCION: PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.
The API is designed to be as simple.   
INFO https://readthedocs.org/projects/pyautogui/downloads/pdf/latest/
     https://pyautogui.readthedocs.io/en/latest/
"""
#%%
import pyttsx3 as Habla
lupita = Habla.init()

#%%
help(lupita)
# %% Acentos
acentos= lupita.getProperty('voices')
for acento in acentos:
    print(acento.id)
#%%
lupita.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")

# %%
lupita.say("Soy Lupita y estoy instalada en Microsoft")
lupita.setProperty("rate",50) #words/min
lupita.runAndWait()
# %%
