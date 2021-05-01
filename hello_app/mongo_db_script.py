import pymongo 

class MongoDB():
    
    classic_collection = []
    detectiv_collection = []
    fantasy_collection = []
    kids_collection = []
    mystic_collection = []
    romance_collection = []

    def __init__(self, *args):
        

        try:
            # Create the client
            client = pymongo.MongoClient('localhost', 27017)

            # Connect to our database
            db = client['booksdb']

            # Fetch our series collection
            self.classic_collection = db['CLASSIC']

            self.detectiv_collection = db['DETECTIV']

            self.fantasy_collection = db['FANTASY']

            self.kids_collection = db['KIDS']

            self.mystic_collection = db['MYSTIC']

            self.romance_collection = db['ROMANCE']

        except Exception as e:
            print(e)

    

