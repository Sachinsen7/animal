import json

def load_data():
    try:
      with open('youtube.txt', 'r') as file:
          return json.load(file)
    except FileNotFoundError:
        print('An exception occurred')
        return  []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}, {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 50)

def add_videos(video):
    name = input("Enter video name: ")
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else: 
        print("Inavlid index selected")



def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Inavalid index selected")



def main():
    

    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. Add Video: ")
        print("2. Edit Video: ")
        print("3. Delete Video: ")
        print("4. View Video: ")
        print("5. View All Videos: ")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

    if __name__ == "__main":
        main()
