from itertools import combinations
N = int(input())
letters = input().split()
K = int(input())
all_combinations = list(combinations(letters, K))
count_a = sum(1 for combo in all_combinations if 'a' in combo)
probability = count_a / len(all_combinations)
print(f"{probability:.3f}")
