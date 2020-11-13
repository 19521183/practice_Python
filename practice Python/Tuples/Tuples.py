if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # convert a list to a tuple
    integer_tuple = tuple(integer_list)
    # create an empty tuple then add items of a list into it
    # integer_tuple = ()
    # for item in integer_list:
    #   integer_tuple += (item,) 
    print(hash(integer_tuple))