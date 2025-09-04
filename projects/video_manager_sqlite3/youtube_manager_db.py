import sqlite3


conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row) 

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("3. Delete Video: ")

        choice = input("Enter your choices: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            video = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(video, time)
        elif choice == '3':
            video_id = input("Enter video Id to update: ")
            video = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, video, time)
        elif choice == '4':
            video_id = input("Enter video Id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("inavild choice")

    conn.close()





if __name__ == "__main__":
    main()
