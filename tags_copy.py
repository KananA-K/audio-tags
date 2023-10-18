import eyed3
import glob
import os


remove_numbers_in_song_name=1
artist=None
numeration_type=0    # 1 for copy file numerator, 2 numerate in date modified order order

path=os.path.dirname(os.path.realpath(__file__))

def get_files(path):
    list=[]
    for dir__path in os.walk(path):
        return dir__path[2]


# files=get_files(path)
files = list(filter(os.path.isfile, glob.glob(path + "\*")))
  
while True:
    if len(files)==0:
        break
    for k in range( len(files) ):
        if not files[k].endswith('.mp3'):
            continue
        print(k+1,':',end='')
        print(files[k])
    break

c_from=int(input('Copy from:'))
c_to=int(input('Copy to:'))


copy_from=os.path.join(path,files[c_from-1])
copy_to=os.path.join(path,files[c_to-1])

song_from=eyed3.load(copy_from)
song_to=eyed3.load(copy_to)
#copy all tags from song1 to song2 using 1 line
song_to.tag=song_from.tag
song_to.tag.save()