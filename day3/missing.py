def find_missing_element(nums):
    n = len(nums)
    
    # Initialize the result with 0
    result = 0
    
    # XOR all elements in the input sequence
    for i in range(n):
        result ^= nums[i]
    
    # XOR all numbers from 0 to n
    for i in range(1, n + 1):
        result ^= i
    
    return result

def main():
    n = int(input("Enter the length of the sequence: "))
    nums = list(map(int, input("Enter the sequence of numbers separated by commas: ").split(',')))
    
    missing_element = find_missing_element(nums)
    print(f"The missing element is: {missing_element}")

if __name__ == "__main__":
    main()
