# Counting frequencies of array elements

arr = list(map(int,input().split()))
visited = []

for i in range(len(arr)):
    if arr[i] not in visited:
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        print(f"{arr[i]}:{count} times")
        visited.append(arr[i])
