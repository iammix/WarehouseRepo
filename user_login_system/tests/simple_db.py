import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['mydatabase']
print(myclient.list_database_names())

mycollection = mydb['customers']
mydict = {
    "name": "John",
    "address": "Highway 37"
    }
x = mycollection.insert_one(mydict)
print(x.inserted_id)





# Check if database exists
dblist = myclient.list_database_names()
if 'mydatabase' in dblist:
    print('The database exists.')
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")


else:
    print('Database never created')