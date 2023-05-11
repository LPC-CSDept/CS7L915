
gt = (lambda x: x[0] > x[1])
first = (lambda x: x[0])


def main():
    mylist = [5, 10, 15, 25, 20, 55, 40]
    #########################################
    # Code your program here
    #########################################

    zipped = zip(mylist[1:], mylist)
    result = list(filter(gt, zipped))
    result = list(map(first, result))
    print(result)

    #########################################
    # Do not delete the reutrn statement
    return result


if __name__ == '__main__':
    main()
