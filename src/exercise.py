def main():
    #write your code below this line
    sum = 0

    while True:
        number = int(input("Give a number:"))

        if number == 0:
            break

        sum += number

    print("Sum of the numbers: " + str(sum))

if __name__ == '__main__':
    main()
