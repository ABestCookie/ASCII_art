import pytube

#​YouTube('放要下載的youtube影片網址')
yt=pytube.YouTube('https://www.youtube.com/watch?v=FtutLA63Cp8')

#下載的程式碼​
yt.streams.first().download()
