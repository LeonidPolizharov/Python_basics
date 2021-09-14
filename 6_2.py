from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    logs = []
    for i in f:
        content = f.readline()
        parsed_line = [content.split()[0]]
        parsed_line.extend(content[content.index('"') + 1:].split()[0:2])
        logs.append(tuple(parsed_line))

spam = Counter(logs).most_common(1)[0]

print(f"Спамер: {spam[0][0]}\nКол-во запросов: {spam[1]}")
