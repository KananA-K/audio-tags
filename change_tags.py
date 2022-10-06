import eyed3
import os

path=os.curdir

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

files=get_files(path)
songs_dir=list( map( lambda g:os.path.join( path, g ), files ) ) 
# print(get_files(path))

for file in files:
    file_new=file.replace(' - Hiphopde.com','')
    dir_file_new=f"{path}/{file_new}"
    dir_file=f"{path}/{file}"
    os.rename(dir_file, dir_file_new)

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
        num=int(file[0:2])
        song.tag.track_num=tuple([num, None] )
        # song._tag.album_artist='Kendrick Lamar'   #Album artist
    else:
        # title=file[15:-11]
        song.tag.title=title
    song.tag.genre='Hip-Hop'
    print(title)
    song.tag.save()

for file in songs_dir:
    os.rename(file, file.replace('__FlexyOkay.com',''))
    # os.rename(file, file.decode("utf-8").replace('__FlexyOkay.com',''))