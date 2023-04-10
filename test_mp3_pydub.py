from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("sample-15s.mp3")

# boost volume by 6dB
# louder_song = song + 6

# reduce volume by 3dB
quieter_song = song - 10

#Play song
quieter_song.export("sample-15s-reduce.mp3", format='mp3')