# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105

from pathlib import Path
import os
from Profile import Profile, Post


def check_ip(theip):
    periods = theip.split('.')
    if len(periods) != 4:
        return False
    for space in periods:
        try:
            thenumber = int(space)
            if thenumber < 0 or thenumber > 255:
                return False
        except ValueError:
            return False
    return True


def setting_directory(thePath, find_directory=True, find_file=None, extension=None):
    data_inside = list(thePath.iterdir())
    for data in data_inside:
        if data.is_dir():
            data_inside.append(data)
            data_inside.remove(data)
    for currentPath in data_inside:
        if currentPath.is_dir():
            if find_directory:
                print(currentPath)
            setting_directory(currentPath, find_directory, find_file, extension)
        else:
            if find_file:
                if currentPath.name == find_file:
                    print(currentPath)
            elif extension:
                if extension == currentPath.suffix[1:]:
                    print(currentPath)
            else:
                print(currentPath)


def all_directories(thePath):
    thelist = []
    for currentPath in thePath.iterdir():
        if os.path.isfile(currentPath):
            print(currentPath)
        else:
            thelist.append(currentPath)
    for thedirectories in thelist:
        print(thedirectories)


def taking_file(thePath, find_file=None, extension=None):
    for currentPath in thePath.iterdir():
        if find_file:
            if currentPath.name == find_file:
                print(currentPath)
        elif extension:
            if currentPath.suffix[1:] == extension:
                print(currentPath)
        else:
            if currentPath.is_file():
                print(currentPath)


def second_ep_commands(thePath, command):
    if command[1] != 'Q':
        profile = Profile()
        profile.load_profile(f'{thePath}')
        if command[1] == 'E':
            print("\nEditing Profile")
            print("Enter the word 'done' when finished editing.\n")
            while True:
                param = input("Enter the parameter to edit the username, password, bio, addpost, and delpost)")
                if param == 'done':
                    break
                if param == 'username':
                    new_username = input("Enter a username for your file: ")
                    profile.username = new_username
                    print("The username has been updated.")
                elif param == 'password':
                    new_password = input("Enter a password")
                    profile.password = new_password
                    print("The password has been updated.")
                elif param == 'bio':
                    new_bio = input("Enter a new bio: ")
                    profile.bio = new_bio
                    print("Bio has been updated.")
                elif param == 'addpost':
                    print("You can use two keywords which are @weather (for the weather) and @lastfm (for top music artist) in your post")
                    new_post = input("Enter a new post for the content: ")
                    post = Post(new_post)
                    profile.add_post(post)
                    print("The post has been added:", post)
                    publishing = input("Do you want to publish this post onto ther server? (Type yes)")
                    if publishing == 'yes':
                        ds_client.send(profile.dsuserver, 3021, profile.username, profile.password, Post.get_entry(post))
                    else:
                        print("Error! Did not send a post online")
                elif param == '-delpost':
                    try:
                        post_index = int(input("Enter a post index for deletion: "))
                        deleted_post = profile.del_post(post_index)
                        print("The post has been delete:", deleted_post)
                    except (IndexError, ValueError):
                        print("The index for the post does not exist")
                profile.save_profile(f'{thePath}')
        else:
            print("Invalid Command")
            profile.save_profile(f'{thePath}')
    if command[1] == 'P':
        print("\nEditing Profile")
        print("Enter the word 'finish' when finished editing.\n")
        while True:
            param = input("Enter the parameter to edit the username, password, bio, posts, post, and -all")
            if param == 'finish':
                break
            if param == 'username':
                new_username = input("Enter a new username:" + profile.username)
            if param == 'password':
                new_password = input("Enter new password:" + profile.password)
                profile.password = new_password
            if param == 'bio':
                new_bio = input("Enter new bio:" + profile.bio)
                profile.bio = new_bio
            if param == 'posts':
                posts = profile.get_posts()
                print('Posts: ', posts)
            if param == 'post':
                try:
                    index = int(command[1].index('post')) + 1
                    index = int((command[1])[index])
                    print('Post:', profile.get_posts()[index])
                except IndexError:
                    print("The index for the post does not exist, find another index")
            if param == '-all':
                print('DSU Server: ' + profile.dsuserver)
                print('Username: ' + profile.username)
                print('Password: ' + profile.password)
                print('Bio: ' + profile.bio)
                posts = profile.get_posts()
                print('All Posts:', posts)
    else:
        print("Invalid Command")


def ep_commands(thePath):
    while True:
        user_input = input("Please input a command (E/P)").split()
        user_input1 = ["Fill"] + user_input
        if user_input1[1] == 'Q':
            break
        second_ep_commands(thePath, user_input1)
    print("You are now back to the main terminal.\nPlease press the letter Q again if you want to quit the program.")


def setting_options(user_input):
    list_of_commands = ["L", "-f", "-r", "-s", "-e", "C", "O", "D", "R"]
    user_input = ["Fill"] + user_input.split(" ")
    if len(user_input) < 3:
        print("Please provide a command and a path in order to go to the directory.")
        return
    command = user_input[1].upper()
    if command not in list_of_commands:
        print("Please provide a valid command from the list which are: L, -f, -r, -s, or -e")
        return
    directory_path = f'{user_input[2]}'
    try:
        myPath = Path(directory_path)
    except FileNotFoundError:
        print("Please provide a path that works for the directory.")
        return
    if command == 'L':
        try:
            all_directories(myPath)
        except FileNotFoundError:
            print("The directory does not exist, the file is not found.")
    elif command == '-f':
        taking_file(myPath)
    elif command == '-r':
        if len(user_input) > 3:
            recursive_command = user_input[3]
            if recursive_command == '-s':
                find_file = str(' '.join(list(user_input)[4:]))
                setting_directory(myPath, False, str(find_file))
            elif recursive_command == '-e':
                extension = str(' '.join(list(user_input)[4:]))
                setting_directory(myPath, False, None, str(extension))
            elif recursive_command == '-f':
                setting_directory(myPath, False)
        else:
            setting_directory(myPath)
    elif command == '-s':
        if len(user_input) < 4:
            print("Please provide a proper command term.")
            return
        find_file = str(' '.join(list(user_input)[3:]))
        taking_file(myPath, find_file)
    elif command == '-e':
        if len(user_input) < 4:
            print("Provide a correct file extension.")
            return
        extension = str(' '.join(list(user_input)[3:]))
        taking_file(myPath, None, extension)

    elif command == 'C':
        recursive_command = user_input[3]
        if recursive_command == '-n' and len(user_input) == 5:
            a_new_file = f'{user_input[4]}.dsu'
            c_command = str(user_input[2]) + a_new_file
            if os.path.exists(c_command):
                if os.path.getsize(c_command) != 0:
                    with open(f'{c_command}', 'r') as the_file:
                        print('THE DSU FILE' + c_command.split("\\")[-1] + 'HAS BEEN LOADED')
                else:
                    print('THE DSU FILE' + c_command.split('\\')[-1] + 'HAS BEEN LOADED')
                    print('The file does not exist and is empty.')
                ep_commands(c_command)
            else:
                print('Please enter an username')
                username_inp = str(input())
                print('Please enter a password')
                password_inp = str(input())
                dsuserver = str(input('Enter a DSU server: '))
                cond = check_ip(dsuserver)
                if cond is True:
                    with open(f'{user_input[4]}.dsu', 'x'):
                        profile = Profile(dsuserver, username_inp, password_inp)
                        profile.save_profile(f'{c_command}')
                        print('You created the DSU file:' + c_command.split("\\")[-1])
                        ep_commands(c_command)
                else:
                    print('The Dsu Server does not exist:', dsuserver)
        else:
            print("ERROR: Invalid input, need to use 'C -n filename' to create a DSU file")
    elif command == 'O':
        try:
            o_command = str(myPath).split("\\")
            file = o_command[-1]
            if file[-3:] == 'dsu':
                if os.path.getsize(myPath) != 0:
                    with open(f'{myPath}', 'r') as the_file:
                        print('THE DSU FILE LOADED SUCCESSFULLY')
                else:
                    print('THE DSU FILE LOADED SUCCESSFULLY')
                    print('The file does not exist and is empty')
                ep_commands(myPath)
            else:
                print("ERROR: Invalid type of file, only dsu files.")
        except FileNotFoundError:
            print("ERROR: The files is not found.")
    elif command == 'D':
        d_command = myPath
        try:
            d_command.unlink()
            print(f'{d_command} has been DELTED')
        except FileNotFoundError:
            print("ERROR: The file is not found")
        while r_file[-4:] != '.dsu':
            print("ERROR: Invalid type of file, only dsu files.")
            user_input = input("Enter the path")
            myPath = Path(f'{user_input}')
            d_command = str(myPath).split('\\')
            r_file = d_command[-1]
        d_command = myPath.unlink()
        print(f'{d_command} has been DELETED')

    elif command == 'R':
        r_command = str(myPath).split('\\')
        r_file = r_command[-1]
        try:
            if r_file[-3:] == '.dsu':
                if os.path.getsize(myPath) != 0:
                    with open(f'{myPath}', 'r') as the_file:
                        read_line = the_file.read()
                        read_line = read_line.rstrip('\n')
                        print(read_line)
                else:
                    print("EMPTY")
            else:
                while r_file[-4:] != '.dsu':
                    print("Please enter the name of the dsu file that needs to be read")
                    user_input = input("Enter the path")
                    myPath = Path(f'{user_input}')
                    r_command = str(myPath).split('\\')
                    r_file = r_command[-1]
        except FileNotFoundError:
            print("ERROR: The file is not found")
    else:
        print("ERROR: invalid command, please put a correct one")


def run():
    while True:
        print("Welcome to the DSU program!")
        print("To start please enter one of the following commands that are listed:")
        print("L <path> [-f] [-r [-s <search string>] [-e <extension>]] - These are to list the files and directories")
        print("C <path> -n <file name> - To create a DSU file")
        print("O <path> - To open a DSU file")
        print("D <path> - To delete a DSU file")
        print("R <path> - To read a DSU file")
        runcode = input("Write a command to start the code: ")
        if runcode == 'admin':
            run(admin.run())
        if runcode == 'Q':
            break
        setting_options(runcode)


if __name__ == '__main__':
    run()
