if __name__ == '__main__':
    students = []
    
    # Input lene ke liye loop
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  # Nested List: [ [Name, Score], [Name, Score] ]

    # 1. Sabhi unique scores nikale aur unhe sort kiya
    scores = sorted(set([student[1] for student in students]))
    
    # 2. Second lowest score pakda (index 1)
    second_lowest_score = scores[1]
    
    # 3. Jin students ka score second_lowest_score ke barabar hai unka naam nikala
    names = [student[0] for student in students if student[1] == second_lowest_score]
    
    # 4. Naamo ko alphabetically sort kiya
    names.sort()
    
    # 5. Har naam ko naye line par print kiya
    for name in names:
        print(name)
