# Find the highest/lowest frequency element

arr = list(map(int, input().split()))
visited = []
freq_dict = {}

for i in range(len(arr)):
    if arr[i] not in visited:
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        freq_dict[arr[i]] = count
        visited.append(arr[i])

max_freq = max(freq_dict.values())
min_freq = min(freq_dict.values())

print("Highest frequency element(s):")
for key, value in freq_dict.items():
    if value == max_freq:
        print(f"{key} : {value} times")

print("Lowest frequency element(s):")
for key, value in freq_dict.items():
    if value == min_freq:
        print(f"{key} : {value} times")
