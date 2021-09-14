with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    logs = []
    for i in f:
        content = f.readline()
        parsed_line = [content.split()[0]]
        parsed_line.extend(content[content.index('"') + 1:].split()[0:2])
        logs.append(tuple(parsed_line))

print(logs)
