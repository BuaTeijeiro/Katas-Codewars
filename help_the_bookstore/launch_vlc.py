from subprocess import Popen

def launch_vlc(file):
    Popen(['C:/Program Files/VideoLAN/VLC/vlc.exe',file])
    
if __name__ == '__main__':
    launch_vlc('../XML/prueba.xspf')