def knapSack(W, wt, val, n):    
    dp = [0 for i in range(W + 1)]    
    for i in range(1, n + 1):        
        for w in range(W, 0, -1):            
            if wt[i - 1] <= w:                
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])    
    return dp[W]

# Input weights and values
W = []
V = []
num = int(input("Enter the number of weights or values required: \n"))

for i in range(num):
    weight = int(input(f"Enter weight {i+1} : "))
    W.append(weight)

print("\n")

for i in range(num):
    value = int(input(f"Enter value {i+1} : "))
    V.append(value)

print("\n")

# Input the maximum weight capacity
M = int(input("Enter the maximum capacity of the knapsack: "))

# Number of items
n = len(V)

print("\nThe maximum value that can be obtained is:", knapSack(M, W, V, n))

#Brach and bound method
from collections import namedtuple
import os

# Assuming KnapSackBranchNBound is defined elsewhere or will be added
class KnapSackBranchNBound:
    def __init__(self, capacity, items, item_count):
        self.capacity = capacity
        self.items = items
        self.item_count = item_count
        self.maxProfit = 0
        self.taken = []

    def solve(self):
        # Placeholder for the actual branch and bound algorithm
        self.maxProfit = 0  # Example placeholder value
        self.taken = [0] * self.item_count  # Example placeholder array

    def __str__(self):
        self.solve()
        return get_solution(self.maxProfit, self.taken)

def get_solution(optimal_value, taken):
    output_data = str(optimal_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == "__main__":
    Item = namedtuple("Item", ['index', 'value', 'weight'])
    
    # Specify the path to your data file
    file_path = "test.data"  # or use the full path if necessary, e.g., "D:\\test.data"
    
    # Check if the file exists before trying to open it
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
    else:
        # Load data from file
        with open(file_path, 'r') as file:
            input_data = file.read()
        
        lines = input_data.split('\n')
        
        # Read item count and knapsack capacity
        firstLine = lines[0].split()
        item_count = int(firstLine[0])
        capacity = int(firstLine[1])
        
        # Read each item (value and weight)
        items = []
        for i in range(1, item_count + 1):
            line = lines[i]
            parts = line.split()
            items.append(Item(i - 1, int(parts[0]), float(parts[1])))

        # Create and solve the knapsack problem using Branch and Bound
        kbb = KnapSackBranchNBound(capacity, items, item_count)
        print(kbb)
