# n =[i[0].upper()+i[1:] for i in ["ramu","raju"]]
# print(n)

# friends = ['ashley', 'matt', 'michael']

# m = [friend[0].upper() for friend in friends] # ['Ashley', 'Matt', 'Michael']
# print(m)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = [len(i) for i in words if i!="the" ]
# print(word_lengths)

# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# newlist = [i for i in numbers if i>=0]
# print(newlist)

# n = list(set([char[0] for char in ("mathematics") if char in "aeiou"]))
# print(n)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = ''.join([[i for i in j] for j in words])
# print(word_lengths)

n = [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]
arr =[i+i if i%2==0 else i*-1 for i in n]
print(arr) #[144, 52, -79, 140, 40, 136, -43, 71, -71, -4]