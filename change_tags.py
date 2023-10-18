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

def listdirs(rootdir):
    list=[]
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            list.append(file)
    return list
            
while True:
    folders=listdirs(path)
    if len(folders)==0:
        break
    for k in range( len(folders) ):
        print(k+1,':',end='')
        print(folders[k])
    folder_num=int(input('Enter:'))
    # folder_num=2

    path=os.path.join(path,folders[folder_num-1])


# files=get_files(path)
files = list(filter(os.path.isfile, glob.glob(path + "\*")))
  
# Sorting file list based on the creation time of the files
files.sort(key=os.path.getctime)
songs_dir=list( map( lambda g:os.path.join( path, g ), files ) ) 
# print(get_files(path))



string_replace='[SPOTIFY-DOWNLOADER.COM]'

# for file in files:
#     file_new=file.replace(string_replace,'')
#     # dir_file_new=f"{path}/{file_new}"
#     # dir_file=f"{path}/{file}"
#     os.rename(file, file_new)


n=0
#numeration
for file in files:
    n+=1
    
    song_dir=os.path.join( path, file )
    if not song_dir.endswith('.mp3'):
        continue
    song=eyed3.load(song_dir)

    if numeration_type==1:
        num=int(file[0:2])
        song.tag.track_num=tuple([num, None] )
    elif numeration_type==2:
        song.tag.track_num=n
    else:
        break


for file in files:
    song_dir=os.path.join( path, file )
    if not song_dir.endswith('.mp3'):
        continue
    song=eyed3.load(song_dir)
    # song=eyed3.load(song_dir.decode("utf-8"))
    title=song.tag.title
    if title!=None:
        title=song.tag.title.lstrip('0123456789.- ')
        # title=title.replace(' | Hiphopde.com','')
        
        # title=file[15:-11]
        song.tag.title=title
        if artist != None:
            song._tag.album_artist=artist   #Album artist
    else:
        # title=file[15:-11]
        song.tag.title=title
    song.tag.genre='Hip-Hop'
    print(title)
    song.tag.save()


if remove_numbers_in_song_name:   #remove numbers from song name

    for file in files:
        song_dir=os.path.join( path, file )
        if not song_dir.endswith('.mp3'):
            continue
        song=eyed3.load(song_dir)
        # song=eyed3.load(song_dir.decode("utf-8"))
        title=song.tag.title
        if title!=None:
            title=song.tag.title
            # title=title.replace(' | Hiphopde.com','')
            # title=file[15:-11]
            song.tag.title=title
        
            if '.' in title[0:2]:
                #delete first 2 chars
                title=title[2:]
            else:
                title=title[2:]
                title=title.replace('.','',1)
            song.tag.title=title


for file in songs_dir:
    os.rename(file, file.replace(string_replace,''))
