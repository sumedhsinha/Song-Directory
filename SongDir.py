import pickle
import os


def create_file():
    file = open("songs.dat", "wb")
    op = 'y'
    while op == "Y" or op == 'y':
        songid = int(input("Enter song id: "))
        print("Now, please enter details like song name, Genre, Artist, Album, Company, Language, Lyricist, "
              "Duration, Release month and year (MM/YYYY), Award, Rating, Cost.")
        Name = str(input("Enter the name of song: "))
        Genre = str(input("Enter genre: "))
        Artist = str(input("Enter artist: "))
        Album = str(input("Enter album: "))
        Company = str(input("Enter company: "))
        Language = str(input("Enter language: "))
        Lyricist = str(input("Enter lyricist: "))
        Duration = str(input("Enter duration in seconds: "))
        ReleaseDate = str(input("Enter release month and year (MM/YYYY): "))
        Award = str(input("Enter award: "))
        Rating = str(input("Enter rating out of 10: "))
        Cost = str(input("Enter cost: "))
        pickle.dump([songid, Name, Genre, Artist, Album, Company, Language, Lyricist, Duration,
                     ReleaseDate, Award, Rating, Cost], file)
        op = str(input("Continue y/n"))
    file.close()


def append_file():
    file = open("songs.dat", "ab")
    op = 'y'
    while op == "Y" or op == 'y':
        songid = int(input("Enter song id: "))
        print("Now, please enter details like song name, Genre, Artist, Album, Company, Language, Lyricist, "
              "Duration, Release month and year (MM/YYYY), Award, Rating, Cost.")
        Name = str(input("Enter the name of song: "))
        Genre = str(input("Enter genre: "))
        Artist = str(input("Enter artist: "))
        Album = str(input("Enter album: "))
        Company = str(input("Enter company: "))
        Language = str(input("Enter language: "))
        Lyricist = str(input("Enter lyricist: "))
        Duration = str(input("Enter duration in seconds: "))
        ReleaseDate = str(input("Enter release month and year (MM/YYYY): "))
        Award = str(input("Enter award: "))
        Rating = str(input("Enter rating out of 10: "))
        Cost = str(input("Enter cost: "))
        pickle.dump([songid, Name, Genre, Artist, Album, Company, Language, Lyricist, Duration,
                     ReleaseDate, Award, Rating, Cost], file)
        op = str(input("Continue y/n"))
    file.close()


def display_songs():
    cnt = 0
    try:
        with open("songs.dat", "rb") as file1:
            while True:
                rec = pickle.load(file1)
                print(rec)
                cnt += 1
    except EOFError:
        pass
    print("No of songs is:", cnt)


def search_songs():
    print("Columns are: \n1 - songid\n2 - Name\n3 - Genre\n4 - Artist\n5 - Album\n6 - Company\n7 - Language\n8 - "
          "Lyricist\n9 - Duration\n10 - Release month and year (MM/YYYY)\n11 - Award\n12 - Rating (out of 10)\n13 - "
          "Cost.")
    usrinp = int(input("Please enter number of column you wish to search on: "))
    usrval = str(input("Enter value to search on : "))
    col = int(usrinp - 1)
    try:
        with open("songs.dat", "rb") as file1:
            while True:
                rec = pickle.load(file1)
                if str(rec[col]) == str(usrval):
                    print(rec)

    except EOFError:
        pass


def count_songs():
    cnt = 0
    print("Columns are: \n1 - songid\n2 - Name\n3 - Genre\n4 - Artist\n5 - Album\n6 - Company\n7 - Language\n8 - "
          "Lyricist\n9 - Duration\n10 - Release month and year (MM/YYYY)\n11 - Award\n12 - Rating (out of 10)\n13 - "
          "Cost.")
    usrcol = str(input("Please enter column number, enter [all] to get total count: "))
    if not(usrcol == "all"):
        usrinval = str(input("Please enter value to count on :"))
    else:
        usrinval = ""
    try:
        with open("songs.dat", "rb") as file1:
            while True:
                rec = pickle.load(file1)
                if usrcol == "all":
                    cnt += 1
                elif not(usrinval == "") and not(usrcol == "all"):
                    if str(rec[int(usrcol)-1]) == str(usrinval):
                        cnt += 1

                else:
                    cnt += 1
    except EOFError:
        pass
    print("No of songs is:", cnt)


def nth_search_edit():
    n = int(input("Enter value for n, record which is desired to be edited: "))
    file1 = open("songs.dat", "rb")
    file2 = open("temp.dat", "wb")
    ctr = 0
    try:
        while True:
            rec = pickle.load(file1)
            temp = rec
            ctr += 1
            if ctr == n:
                print("Record is: ", rec)
                temp[0] = int(input("Enter new song id: "))
                temp[1] = str(input("Enter the name of song: "))
                temp[2] = str(input("Enter new genre: "))
                temp[3] = str(input("Enter new artist: "))
                temp[4] = str(input("Enter new album: "))
                temp[5] = str(input("Enter new company: "))
                temp[6] = str(input("Enter new language: "))
                temp[7] = str(input("Enter new lyricist: "))
                temp[8] = str(input("Enter new duration in seconds: "))
                temp[9] = str(input("Enter new release month and year (MM/YYYY): "))
                temp[10] = str(input("Enter new award: "))
                temp[11] = str(input("Enter new rating out of 10: "))
                temp[12] = str(input("Enter new cost: "))
                pickle.dump(temp, file2)
            else:
                pickle.dump(rec, file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("songs.dat")
        os.rename("temp.dat", "songs.dat")


def songid_search_edit():
    file1 = open("songs.dat", "rb")
    file2 = open("temp.dat", "wb")
    searchsongid = int(input("Enter song id to search: "))
    try:
        while True:
            rec = pickle.load(file1)
            temp = rec
            if rec[0] == searchsongid:
                print("Record is: ", rec)
                temp[0] = int(input("Enter new song id: "))
                temp[1] = str(input("Enter the name of song: "))
                temp[2] = str(input("Enter new genre: "))
                temp[3] = str(input("Enter new artist: "))
                temp[4] = str(input("Enter new album: "))
                temp[5] = str(input("Enter new company: "))
                temp[6] = str(input("Enter new language: "))
                temp[7] = str(input("Enter new lyricist: "))
                temp[8] = str(input("Enter new duration in seconds: "))
                temp[9] = str(input("Enter new release month and year (MM/YYYY): "))
                temp[10] = str(input("Enter new award: "))
                temp[11] = str(input("Enter new rating out of 10: "))
                temp[12] = str(input("Enter new cost: "))
                pickle.dump(temp, file2)
            else:
                pickle.dump(rec, file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("songs.dat")
        os.rename("temp.dat", "songs.dat")


def search_delete():
    file1 = open("songs.dat", "rb")
    file2 = open("temp.dat", "wb")
    usrop = int(input("Please enter the number of column to search the records:\n1 - songid\n2 - Name\n3 - n th record "
                      ": "))

    def s_d_nth():
        n = int(input("Enter value for n, record which is desired to be deleted: "))
        ctr = 0
        try:
            while True:
                rec = pickle.load(file1)
                ctr += 1
                if ctr == n:
                    pass
                else:
                    pickle.dump(rec, file2)
        except EOFError:
            file1.close()
            file2.close()
            os.remove("songs.dat")
            os.rename("temp.dat", "songs.dat")

    def s_d_name():
        n = str(input("Enter value for name, record which is desired to be deleted: "))
        try:
            while True:
                rec = pickle.load(file1)
                if str(rec[1]) == str(n):
                    pass
                else:
                    pickle.dump(rec, file2)
        except EOFError:
            file1.close()
            file2.close()
            os.remove("songs.dat")
            os.rename("temp.dat", "songs.dat")

    def s_d_id():
        n = str(input("Enter value for songid, record which is desired to be deleted: "))
        try:
            while True:
                rec = pickle.load(file1)
                if str(rec[0]) == str(n):
                    pass
                else:
                    pickle.dump(rec, file2)
        except EOFError:
            file1.close()
            file2.close()
            os.remove("songs.dat")
            os.rename("temp.dat", "songs.dat")

    if usrop == 1:
        s_d_id()
    elif usrop == 2:
        s_d_name()
    elif usrop == 3:
        s_d_nth()
    else:
        print("Invalid input")


print("Welcome, please enter option number to contnue:"
      "\n1 - Create file using data entry"
      "\n2 - Append record to file"
      "\n3 - Display all songs"
      "\n4 - Search for a song"
      "\n5 - Count songs for specified criteria"
      "\n6 - Edit a record for specified criteria"
      "\n7 - Edit n th record"
      "\n8 - Delete a record from the file")
mainusrop = int(input(":"))
if mainusrop == 1:
    create_file()
elif mainusrop == 2:
    append_file()
elif mainusrop == 3:
    display_songs()
elif mainusrop == 4:
    search_songs()
elif mainusrop == 5:
    count_songs()
elif mainusrop == 6:
    songid_search_edit()
elif mainusrop == 7:
    nth_search_edit()
elif mainusrop == 8:
    search_delete()
else:
    print("Invalid input")

