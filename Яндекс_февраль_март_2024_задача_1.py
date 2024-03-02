import re
import textwrap

st = input()

st = re.sub(' +,', ',', st)
st = re.sub(r'(?<=[,])(?=[^\s])', r' ', st)

len_word = 0
a = st.replace(',','')
for i in a.split():
    if len(i) > len_word:
        len_word = len(i)
len_line = len_word * 3
print(textwrap.fill(st, len_line))
