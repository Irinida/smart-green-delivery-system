from pymongo import MongoClient

# Connect to MongoDB (use localhost in lab, later change to MongoDB Atlas)
client = MongoClient("mongodb://localhost:27017/")
db = client["smart_green_delivery"]

orders_collection = db["orders"]
clusters_collection = db["clusters"]

print("✅ MongoDB connected successfully!")
