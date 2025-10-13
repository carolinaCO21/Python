from utils import input_int

def main():
    n = input_int("Número para factorial: ", min_val=0, max_val=20)
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    print(f"{n}! = {factorial}")

if __name__ == "__main__":
    main()
