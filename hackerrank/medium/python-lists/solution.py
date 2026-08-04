if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Input ko split karke command name aur arguments me alag karein
        cmd = input().split()
        
        action = cmd[0]  # Command ka naam (e.g., 'insert', 'print', etc.)
        
        if action == 'insert':
            i = int(cmd[1])
            e = int(cmd[2])
            my_list.insert(i, e)
        elif action == 'print':
            print(my_list)
        elif action == 'remove':
            e = int(cmd[1])
            my_list.remove(e)
        elif action == 'append':
            e = int(cmd[1])
            my_list.append(e)
        elif action == 'sort':
            my_list.sort()
        elif action == 'pop':
            my_list.pop()
        elif action == 'reverse':
            my_list.reverse()
