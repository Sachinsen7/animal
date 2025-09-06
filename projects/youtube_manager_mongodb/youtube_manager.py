from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.4xnsc.mongodb.net/ytmanager", tlsAllowInvalidCertificates=True)

print(client)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time" : time})



def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]} nd  Time: {video["time"]}")



def update_video(video_id, new_time, new_name):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name":new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})




def main():
    while True:
        print("\n Youtube manager appp")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter Your Choices: ")


        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name")
            time = input("Enter the video time")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name")
            time = input("Enter the updated video time")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Inavlid Choice")


if __name__ == "__main__":
    main()