import pymongo
client = pymongo.MongoClient("mongodb+srv://nishi123:nishi123@nishi.t9fo8.gcp.mongodb.net/DataMining?retryWrites=true&w=majority")
db = client['DataMining']
UserRegisterImagesCollection = db['UserRegisterImagesCollection']
