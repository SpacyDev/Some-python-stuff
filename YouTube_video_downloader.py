import pytube

url = input("input URL: ")
video = pytube.YouTube(url).streams.get_highest_resolution().download()
