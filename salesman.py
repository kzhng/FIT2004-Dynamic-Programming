

def read_in_data(file_name):
    """
    this function reads in the data from a given file into a list of size n where n is the number of houses with a 0 at
    the start of that list.
    :param file_name:
    :return: list of data from file
    :time complexity: O(N) where N is the number of houses
    :space complexity: O(N) where N is the number of houses
    """
    file = open(file_name)
    lines = file.readlines()
    file.close()
    num_houses = int(lines[0].strip())
    data_list = [0 for _ in range(num_houses + 1)]
    item_buying_prices = lines[1].strip().split(" ")
    for a in range(1, num_houses + 1):
        data_list[a] = int(item_buying_prices[a - 1])
    return data_list


def memoise_maximum_salesman_profit(list_of_data):
    """
    this function finds the maximum profit of the salesman by iteratively looping through the list, and only looking at
    the left most non-neighbour of the house we are currently checking for. Keeping track of the largest profit of the
    house that is not a neighbour, The left most non-neighbour j is such that i-j > k, where i is the house we are
    currently checking for and k is the set number of houses that are considered neighbours on one side. Checking to see
    if the profit of j is bigger than the variable with the largest profit that is not the neighbour of the previous
    house. If it is, we add the profit of j to the memo list at index I, to memoise it. Then we update the largest
    profit variable to be equal to the profit at j, otherwise we add the largest profit variable to the memo list at
    index i.
    :param list_of_data
    :return: memoised list
    :time complexity: O(N) where N is the number of houses
    :space complexity: O(N) where N is the number of houses
    """
    k = int(input("Enter value of k: "))
    memo = [x for x in list_of_data]
    largest_profit_not_neighbour = memo[0]
    memo_length = len(memo)
    for i in range(1, memo_length):
        j = i - k - 1
        if j >= 1:
            if memo[j] > largest_profit_not_neighbour:
                memo[i] += memo[j]
                largest_profit_not_neighbour = memo[j]
            else:
                memo[i] += largest_profit_not_neighbour
    return memo


def backtrack_optimal_solution(list_data, memo_list):
    """
    this function backtracks our memoised list to find the optimal solution. Firstl, we do a linear scan to find the max
    profit in the memo list. Once we have done that, we then keep track of the max profit and add the house number to a
    list. To find the other houses, we subtract the max profit from the corresponding house profit in the data list,
    let’s call backtrack max profit, and then move left in the memo list till we find a number that matches backtrack
    max profit and then do the same. Then, because we require an ascending solution, we iteratively pop and append the
    descending solution into a list.
    :param list_data
    :param memo_list
    :return: none
    :time complexity: O(N) where N is the number of houses
    :space complexity: O(!) constant space
    """
    max_profit = 0
    length_memo = len(memo_list)
    max_profit_index = 0
    for s in range(1, length_memo):
        if memo_list[s] > max_profit:
            max_profit = memo_list[s]
            max_profit_index = s
    descending_solution = []
    backtrack_max_profit = max_profit
    backtrack_max_profit -= list_data[max_profit_index]
    descending_solution.append(max_profit_index)
    for t in range(max_profit_index - 1, 0, -1):
        if memo_list[t] == backtrack_max_profit:
            backtrack_max_profit -= list_data[t]
            descending_solution.append(t)
    solution = []
    for _ in range(len(descending_solution)):
        item = descending_solution.pop()
        solution.append(item)
    solution = [str(y) for y in solution]
    string_of_solution = " ".join(solution)
    print("Houses: {}".format(string_of_solution))
    print("Total Sale: {}".format(max_profit))


if __name__ == '__main__':
    data_in_list = read_in_data("houses.txt")
    memoisation = memoise_maximum_salesman_profit(data_in_list)
    backtrack_optimal_solution(data_in_list, memoisation)

