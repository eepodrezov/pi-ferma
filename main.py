def check_fermat_theorem(n):
    for a in range(1, 51):
        for b in range(1, 51):
            for c in range(1, 51):
                if a**n + b**n == c**n:
                    return True
    return False

theorem_proven = check_fermat_theorem(2)
if theorem_proven:
    print("Великая теорема Ферма доказана для n=2")
else:
    print("Великая теорема Ферма не доказана для n=2")