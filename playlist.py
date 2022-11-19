

def read_in_data(file_name):
    """
    this function reads in the data from a given file into a list of size n where n is the number of songs with a 0 at
    the start of that list.
    :param file_name:
    :return: list of data from file
    :time complexity: O(N) where N is the number of songs
    :space complexity: O(N) where N is the number of songs
    """
    file = open(file_name)
    lines = file.readlines()
    file.close()
    num_songs = int(lines[0].strip())
    data_list = [0 for _ in range(num_songs + 1)]
    song_duration = lines[1].strip().split(" ")
    for a in range(1, num_songs + 1):
        data_list[a] = int(song_duration[a - 1])
    return data_list


def memoise_playlist_length(list_of_data, length):
    """
    this function memoises the playlist length by first initialising a memo table of size (N + 1) by (T + 1), with False
    values for each cell. Then I iteratively loop from 0 to n, looking at the song duration of the song list at index
    n. If the song duration is less than or equal to T, then we set the row we are currently on and column that
    corresponds to the song duration to be true. Then we iteratively loop from 0 to T, and if the previous row of the
    column we are currently searching is true, then we set the row we are currently on and the column to be true, and
    also the column number plus the song duration at the current row we are on to be true as well if that number is less
    than or equal to the playlist length.
    :param list_of_data
    :param length
    :return: memoised table
    :time complexity: O(NT) where N is the number of houses, and T is the time to reach the destination
    :space complexity: O(NT) where N is the number of houses, and T is the time to reach the destination
    """
    data_length = len(list_of_data)
    memo_table = [[False for _ in range(length + 1)] for _ in range(data_length)]
    for i in range(data_length):
        song_length = list_of_data[i]
        if song_length <= length:
            memo_table[i][song_length] = True
        for j in range(length + 1):
            if memo_table[i-1][j]:
                memo_table[i][j] = True
                if j + song_length <= length:
                    memo_table[i][j + song_length] = True
    return memo_table


def backtrack_playlist_songs(list_data, memo_table, length):
    """
    this function backtracks our memoisation to find the optimal solution. First of all we check if the bottom right
    corner cell is true. If it’s false, then that means we cannot construct a playlist length that exactly matches T.
    Otherwise, we iteratively check each row of that column until the previous row and that specific column we are
    currently on is false. If it is, that means the row we are currently on corresponds to a song that is in the
    playlist. Then we subtract the column number by the corresponding song length of the row we are currently on to the
    backtrack playlist length. Record the song duration along with the id which we determine by the row number we are
    currently on to the solution list. Again, because we require an ascending solution, we iteratively pop and append
    the descending solution into a list. This has time complexity of O(N) and space complexity of O(NT).
    :param list_data
    :param memo_table
    :param length
    :return: none
    :time complexity: O(N) where N is the number of songs
    :space complexity: O(N) where N is the number of songs
    """
    data_length = len(list_data)
    if not memo_table[data_length - 1][length]:
        print("Bad Luck Alice!")
    else:
        descending_solution = []
        value_pointer = length
        for x in range(data_length, 0, -1):
            if not memo_table[x-1][value_pointer]:
                descending_solution.append([str(x), str(list_data[x])])
                value_pointer -= list_data[x]
        solution = []
        for _ in range(len(descending_solution)):
            item = descending_solution.pop()
            solution.append(item)
        print("Playlist")
        for y in range(len(solution)):
            print("ID: {} Duration: {}".format(solution[y][0], solution[y][1]))


if __name__ == '__main__':
    data_in_list = read_in_data("songs.txt")
    trip_length = int(input("Enter trip length: "))
    memoised_table = memoise_playlist_length(data_in_list, trip_length)
    backtrack_playlist_songs(data_in_list, memoised_table, trip_length)

