arr = []
with open('lc_links_unclean.txt', 'r') as file:
    for line in file:
        arr.append(line)

def remove_elements(array, pattern):
    clean_links = []
    for element in array:
        if pattern not in element:
            clean_links.append(element)
        else:
            print("Removed" + element)
    return clean_links

arr = remove_elements(arr, '/solution')
print(len(arr))
arr = list(set(arr))

with open('leetcode_links.txt', 'w') as file:
    for link in arr:
        file.write('https://www.leetcode.com' + link)