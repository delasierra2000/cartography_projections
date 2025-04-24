import subprocess
import os


name="stereographic_animation"
fps=60

if not os.path.exists('./animations/'):
    os.makedirs('./animations/')


subprocess.run([
    'ffmpeg',
    '-framerate', str(fps),           # FPS
    '-i', '../png/all_maps/%d.png', # Entrada (formato numérico)
    '-c:v', 'libx264',
    '-vf', 'scale=1080:1080',
    '-pix_fmt', 'yuv420p',
    './animations/'+name+'.mp4'
])