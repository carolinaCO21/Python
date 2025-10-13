from utils import input_int

def main():
    n = input_int("Introduce un número: ", min_val=1)
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
