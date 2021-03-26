#importando biblioteca para reproduzir mp3
from pygame import mixer
mixer.init()
mixer.music.load('Maroon 5 - Memories (Official Video).mp3')
mixer.music.play()
mixer.music.set_volume(0.05)
import time
time.sleep(360)
