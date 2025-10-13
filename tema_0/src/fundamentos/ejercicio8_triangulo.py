from utils import input_int

def main():
    n = input_int("Base del triángulo: ", min_val=1, max_val=20)
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

if __name__ == "__main__":
    main()
