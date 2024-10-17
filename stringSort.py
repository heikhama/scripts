newstrings = ["great", "simple", "great", "this", "useful", "investing", "compounding", "investing"]
for word in newstrings:
  print(word)
word_frequency = {}
for word in newstrings:
  if word.isalnum():
     word = word.lower()
     if word in word_frequency:
      word_frequency[word] += 1
     else:
      word_frequency[word] = 1
for word, frequency in word_frequency.items():
    print(f"'{word}': {frequency}")
sorted_dict = dict(sorted(word_frequency.items(), key=lambda item: item[1]))
print(sorted_dict)