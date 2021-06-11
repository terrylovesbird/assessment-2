import csv

class Inventory:
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

    #load all video infos in the store inventory
    @classmethod
    def all_videos(cls):
        videos = []
        with open("./data/inventory.csv") as videos_file:
            data = csv.reader(videos_file)
            for line in data:
                id = line[0]
                title = line [1]
                rating = line [2] 
                copies_available = line [3] 

                video = cls(id, title, rating, copies_available)
                videos.append(video)
            
        return videos