'''
Given a text as input, find and output the lonest world
'''

sentence =list( input('put a sentence: ').split())

w_len = []
count = 0
for w in sentence :
    w_len.append(len(w))
    count += 1
print(w_len)


for x in range(len(sentence)):
    if w_len[x] == max(w_len):
        print('the longest world is "' ,sentence[x],'".')
        