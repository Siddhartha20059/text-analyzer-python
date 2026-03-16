text = "AI will change the world and AI will create new opportunities"
stopwords = ["the","and","is","a"]
words=text.lower().split()
clean_words=[]
for w in words:
    if w not in stopwords:
        clean_words.append(w)
freq={}
for n in words:
    if n in freq:
        freq[n]+=1
    else:
        freq[n]=1
print("word frequency:",freq)
sorted_words = sorted(freq, key=freq.get, reverse=True)

print("Top 3 words:",sorted_words[:3])