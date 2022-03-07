video = { 
    "title": 'awsome python tutorial', 
    "views":  54344, 
    "img": 'google/images/rrgew.png'
}

video_2 = { 
    "title": 'awsome python tutorial 2 ', 
    "views":  54344, 
    "img": 'google/images/rrgew.png',
    #"comments": [more lists]
}

videos = [video, video_2]


# [0] tells the comp what dict. in the list that it needs to access, and the ['title'] tells the comp what you what from the list 
print(videos[0]['title'])