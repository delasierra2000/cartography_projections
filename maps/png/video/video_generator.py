import subprocess


name="transverse_mercator_animation"
fps=30


subprocess.run([
    'ffmpeg',
    '-framerate', str(fps),           # FPS
    '-i', '../all_maps/%d.png', # Entrada (formato numérico)
    '-c:v', 'libx264',
    '-vf', 'scale=1920:1080',
    '-pix_fmt', 'yuv420p',
    './animations/'+name+'.mp4'
])