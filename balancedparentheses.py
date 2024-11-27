def generate_parentheses(n):
    def backtrack(open_count, close_count, current, result):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '{', result)
        
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + '}', result)
    
    result = []
    backtrack(0, 0, '', result)
    return result

def main():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        combinations = generate_parentheses(n)
        print(f"Test Case #{case}:")
        for combination in combinations:
            print(combination)

if __name__ == "__main__":
    main() 