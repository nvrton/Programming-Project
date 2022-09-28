v = "Hi"


def main(): 
    def main2():
        global v
        v = "Hello"
        print (v)
    main2()


def main3():
    print(v)


main()
main3()