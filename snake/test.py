def main() :
    numCases = int(input())
    for case in range(1, numCases + 1):
        padlock = input()
        favorites = input()

        for p in padlock:
            tries = []
            for f in favorites:
                tries.append(dist(p, f))
                
            minOperations = min(tries)
            
            print(f'Case #{case}: {minOperations}\n')
        
        
def dist(a, b) :
    distance = abs(ord(a) - ord(b))
    
    if distance <= 13:
        return distance
    else:
        return 26 - distance

main()