class KnapsackPackage(object):    
    def __init__(self, weight, value):        
        self.weight = weight        
        self.value = value        
        self.cost = value / weight    
    
    def __lt__(self, other):        
        return self.cost < other.cost

class FractionalKnapsack(object):    
    def knapsackGreProc(self, W, V, M, n):        
        packs = []        
        for i in range(n):            
            packs.append(KnapsackPackage(W[i], V[i]))        
        packs.sort(reverse=True)        
        remain = M        
        result = 0        
        i = 0        
        stopProc = False
        
        while not stopProc:            
            if i < n and packs[i].weight <= remain:                
                remain -= packs[i].weight                
                result += packs[i].value                
                print("Pack", i, "- Weight", packs[i].weight, "- Value", packs[i].value)            
            elif i < n:                
                i += 1            
            if i == n:                
                stopProc = True
        
        print("Max Value:", result)

if __name__ == "__main__":    
    W = []    
    V = []    
    num = int(input("Enter the number of weights or values required:\n"))    
    for i in range(num):        
        weight = float(input(f"Enter weight {i+1}: "))        
        value = float(input(f"Enter value {i+1}: "))        
        W.append(weight)        
        V.append(value)
    
    M = float(input("Enter the maximum capacity of the knapsack:\n"))
    knapsack = FractionalKnapsack()
    knapsack.knapsackGreProc(W, V, M, num)
