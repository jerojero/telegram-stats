#!/usr/bin/env python3
import json

try:
    with open('export.json') as f:
        data=json.load(f)
except:
    print("Default data export not found, please provide a file path:")
    with open(input("Telegram JSON export file: ")) as f:
        data=json.load(f)
        
words_per_day={}
word_counts={}
    
for d in data:
    words_length = len(d['text'])
    datestamp = d['date'].split("T")[0]
    words_per_day[datestamp] = words_per_day.get(datestamp, 0) + words_length
    
    try:
        for word in d['text'].split():
            word_counts[word] = word_counts.get(word, 0) + 1
    except:
        pass
    
    
avg_words_per_day=0
for day, word_length in words_per_day.items():
    avg_words_per_day += word_length
    
avg_words_per_day /= len(words_per_day)

print(f"Average words per day: {avg_words_per_day}")
print(f"Top 10 occurrences of words: { { w:word_counts[w] for w in list(reversed(sorted(word_counts, key=word_counts.__getitem__)))[:10] } }")