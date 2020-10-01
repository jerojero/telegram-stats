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
    
for d in data:
    words_length = len(d['text'])
    datestamp = d['date'].split("T")[0]
    try:
        words_per_day[datestamp] += words_length
    except:
        words_per_day[datestamp] = words_length
    
    
avg_words_per_day=0
for day, word_length in words_per_day.items():
    avg_words_per_day += word_length
    
avg_words_per_day /= len(words_per_day)

print(f"Average words per day: {avg_words_per_day}")