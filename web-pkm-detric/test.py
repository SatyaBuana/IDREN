from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017')

# Beralih ke database 'pp'
db = client['pp']

# Mengakses koleksi 'strings'
strings_collection = db['strings']

# Menambahkan dokumen string
result = strings_collection.insert_one({ 'text': 'Ini adalah contoh data string' })
print(f'Dokumen berhasil ditambahkan dengan ID: {result.inserted_id}')
