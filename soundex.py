from nlp_utilities import soundex

# Test the soundex function with different names
names = ['Jurafsky', 'Jarofsky', 'Jarovsky', 'Jarovski', 'Einstein', 'Alex']
for name in names:
    print(f"{name}: {soundex(name)}")

# Test the soundex function with special cases
    # 1: A word that has sequences of identical numbers.
    # 2: A word with more than 4 letters.
    # 3: A word with less than 4 letters.
names = ['Jurrafsky', 'Alexadrina', 'Lee']
for name in names:
    print(f"{name}: {soundex(name)}")

# Test the soundex function with my name
name = 'SALWA'
emoji = '\U0001F603'
print(f"{name}: {soundex(name)} {emoji}")
