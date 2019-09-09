import random

def main():
    rand1 = random.randint(0,100)
    rand2 = random.randint(0,100)
    sum = rand1 + rand2
    print("Victor")
    print(rand1)
    print(rand2)
    print("Sum =", sum)
    print("Average =", sum / 2)

if __name__ == '__main__':
    main()
