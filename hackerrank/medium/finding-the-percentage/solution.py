if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    # Input read karke dictionary me store karna
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    # --- Yahan se aapka main logic shuru hota hai ---
    
    # 1. Target student ke marks dictionary se nikalein
    query_scores = student_marks[query_name]
    
    # 2. Average calculate karein (sum of scores / total number of subjects)
    avg = sum(query_scores) / len(query_scores)
    
    # 3. Exactly 2 decimal places tak print karein
    print(f"{avg:.2f}")
