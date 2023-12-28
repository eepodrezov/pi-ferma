def check_fermat_theorem(n,m):
    for a in range(1, 51):
        for b in range(1, 51):
            for c in range(1, 51):
                if a**n + b**n + m == c**n:
                    return True
    return False

theorem_proven = check_fermat_theorem(2)
print("Тут я проверял тригерр на питон файлы и сломал скрипт")
print("А тут перезаливал, потому что первая версия тригера не стработала")
print("Попытка4")
print("Создал новый тригер")
print("Изменил доккер файл, чтобы упал билд")
if theorem_proven:
    print("Великая теорема Ферма доказана для n=2")
else:
    print("Великая теорема Ферма не доказана для n=2")