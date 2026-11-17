
# Function to find maximum product of any two elements
def maxProduct(arr):
    n = len(arr)

    # If there are less than 2 elements, no pair exists
    if n < 2:
        return -1

    # Initialize maximum product with smallest possible value
    maxProd = float('-inf')

    # Traverse all possible pairs
    for i in range(n):
        for j in range(i + 1, n):

            # Calculate product of current pair
            product = arr[i] * arr[j]

            # Update maximum product if needed
            maxProd = max(maxProd, product)

    return maxProd

# import sys
# input = sys.stdin.readline()
# input = sys.stdin.readline()
# tokens = input.split()
arr= input()
arr= input()
tokens= arr.split()
int_tokens = list(map(int, tokens))
maxProd = maxProduct(int_tokens)
print(maxProd)
