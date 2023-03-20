"""
Write a function that takes a list of strings and returns the longest common prefix of the strings.
Hello, Help -> Hel
“flower", "flow", "flight -> fl
"apple", "application", "appliance" -> appl
"""


def longest_prefix(array):
    max = -1
    longest_string = ""
    for string in array:
        if len(string) > max:
            longest_string = string
    array.remove(longest_string)
    temp = ""
    for index in range(0, len(longest_string)):
        temp += longest_string[index]
        for ele in array:
            if not ele.startswith(temp):
                temp = list(temp)
                temp.pop(-1)
                print("".join(temp))
                exit(0)
    if not temp:
        print("No valid prefix")


# longest_prefix(["flower", "flow", "flight"])
longest_prefix(["", "application", "appliance"])
