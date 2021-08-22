# Given a string, s, return the length of the longest substring that contains every vowel occurring an even number of times. 
# Note: You may assume s only contains lowercase alphabetical characters and the vowels you must account for are a, e, i, o, and u. 

# Ex: Given the following string s…

# s = "aeiouaeioua", return 10 (the last 'a' cannot count).
# Ex: Given the following string s…

# s = "bbb", return 3 (all vowels occur an even number of times, i.e. zero times each).

class solution(object) : 
    def vowel_max(self, s) : 
        vowels = 'aeiou'
        max_len = 0
        start_idx = 0
        for i in range(len(s)) : 
            if s[i] in vowels : 
                if s.count(s[i]) % 2 == 0 : 
                    max_len = max(max_len, i - start_idx + 1)
                else : 
                    start_idx = i + 1
        return max_len
    
count = solution()
print(count.vowel_max('aeiouaeioua'))

