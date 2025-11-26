def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for i in range(0, len(text)):
        ch = text[i].lower()
        if not ch in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1

    return counts

def get_sorted_counts(counts):
    sorted_counts = []
    for ch in counts:
        num = counts[ch]
        sorted_counts.append({ "char": ch, "num": num })

    def sort_func(chCount):
        return chCount["num"]
    
    sorted_counts.sort(reverse=True, key=sort_func)
    return sorted_counts
