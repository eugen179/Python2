def is_anagram(str1, str2):

    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    return str1 == str2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")