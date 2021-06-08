from pytube import YouTube
link = input("enter ur youtube url: ")
yt = YouTube(link)
videos = yt.streams.filter(mime_type="video/mp4")
#это будет передавать все доступные форматы
video = list(enumerate(videos))
#пронумерует все доступные форматы начиная с нуля
for i in video:
    print(i)
    #покажет все доступные форматы пронумерованные
print("enter the desired option to download the format")
dn_option = int(input("enter the option: "))
#спросит пользователя какой формат видео он хочет загрузить 
dn_video = videos[dn_option] 
dn_video.download() #метод для загрузки видео

print("download successfully")
