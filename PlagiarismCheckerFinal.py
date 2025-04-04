import time
import re
from collections import deque
import os
import tracemalloc

def read_file(filename):
    """Lexon skedarin dhe heq karakteret speciale."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = re.sub(r'\W+', ' ', text)  # Heqja e shenjave të pikesimit dhe karaktereve speciale
            return text
    except FileNotFoundError:
        print(f"Gabim: Skedari '{filename}' nuk u gjet. Sigurohuni që ekziston dhe rruga eshte e sakte.")
        return None
    except Exception as e:
        print(f"Gabim gjate leximit te skedarit '{filename}': {e}")
        return None

def generate_patterns(text, pattern_length):
    """Gjeneron nje gjenerator me nenvargje te gjate sa pattern_length."""
    if text is None:
        return []
    words = text.split()
    queue = deque(maxlen=pattern_length)
    
    for word in words:
        queue.append(word)
        if len(queue) == pattern_length:
            yield ' '.join(queue)

def compute_lps(pattern):
    """KMP - llogarit tabelen LPS (Longest Prefix Suffix)"""
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(text, pattern):
    """KMP -kerkim i nenvargjeve ne tekst"""
    if not text or not pattern:
        return 0 
    lps = compute_lps(pattern)
    i = j = 0
    occurrences = 0
    
    while i < len(text):
        if j < len(pattern) and text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            occurrences += 1
            j = lps[j - 1] if j > 0 else 0
        elif i < len(text) and j < len(pattern) and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
        if j >= len(pattern): 
            j = lps[j - 1] if j > 0 else 0
    
    return occurrences

def rabin_karp_search(text, pattern, prime=101):
    """Rabin-Karp  Kerkimi i nenvargjeve me hash rolling"""

    if not text or not pattern:
        return 0
    d, m, n = 256, len(pattern), len(text)
    h = pow(d, m-1, prime)
    p_hash = t_hash = 0
    occurrences = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            occurrences += 1
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            t_hash = (t_hash + prime) if t_hash < 0 else t_hash
    
    return occurrences

def search_patterns(text, patterns, algorithm):
    """Ekzekuton algoritmin mbi te gjitha nenvargjet"""
    return sum(algorithm(text, pattern) for pattern in patterns)

def compare_files(file1, file2, pattern_length=3):
    text1, text2 = read_file(file1), read_file(file2)
    if text1 is None or text2 is None:
        return None

    # Gjenero modele unike (per te shmangur numerimin e dyfishte)
    patterns = list(set(generate_patterns(text1, pattern_length)))  #
    
    if not patterns:
        print("Gabim: Nuk u gjenden modele per krahasim.")
        return None

    results = {}
    
    for algo_name, algo_func in [("KMP", kmp_search), ("Rabin-Karp", rabin_karp_search)]:
        start_time = time.time()
        
        # Nese pattern_length=1, numero çdo fjale vetem 1 here
        if pattern_length == 1:
            words_in_text2 = set(text2.split())  # Perdor set per fjale unike
            total_matches = sum(1 for pattern in patterns if pattern in words_in_text2)
        else:
            total_matches = sum(algo_func(text2, pattern) for pattern in patterns)
        
        elapsed_time = time.time() - start_time
        
        #  nese total_matches > len(patterns)
        similarity = min((total_matches / len(patterns)) * 100, 100)  # Mu siguru qe se kalon 100%
        
        results[algo_name] = {
            "similarity": similarity,
            "time": elapsed_time
        }

    return results

file1 = 'document1.txt'
file2 = 'document2.txt'

# Kontrollo nese skedaret ekzistojn
if not os.path.exists(file1):
    print(f"Gabim: Skedari '{file1}' nuk ekziston.")
elif not os.path.exists(file2):
    print(f"Gabim: Skedari '{file2}' nuk ekziston.")
else:
    results = compare_files(file1, file2)
    if results:
        for algo, data in results.items():
            print(f"{algo} Similarity: {data['similarity']:.2f}% (Time: {data['time']:.4f} sec)")