# Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a list (`list = []`). You can perform the following commands:   

1. `insert i e`: Insert integer $e$ at position $i$.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer $e$.
4. `append e`: Insert integer $e$ at the end of the list.  
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of the $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.  

**Example**  
$N = 4$  
$\text{append 1}$  
$\text{append 2}$  
$\text{insert 1 3}$  
$\text{print}$   
</br >
</br >
   
- $\text{append 1}$: Append $1$ to the list, $arr = [1]$.  
- $\text{append 2}$: Append $2$ to the list, $arr = [1, 2]$.  
- $\text{insert 1 3}$: Insert $3$ at index $1$, $arr = [1, 3, 2]$.  
- $\text{print}$: Print the array.  
</br >
Output:
<pre>
[1, 3, 2]
</pre>

**Input Format**

The first line contains an integer, $n$, denoting the number of commands.	
Each line $i$ of the $n$ subsequent lines contains one of the commands described above.


**Constraints**

- The elements added to the list must be *integers*.

**Output Format**

For each command of type `print`, print the list on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T17:12:16.379Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-lists/problem)