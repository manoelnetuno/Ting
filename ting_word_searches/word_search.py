def find_occurrences_in_file(word, file):
    occurrences = []
    word_lower = word.lower()

    with open(file['nome_do_arquivo'], 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            if word_lower in line.lower():
                occurrences.append({'linha': line_number})

    return occurrences


def find_occurrences_with_content_in_file(word, file):
    occurrences = []
    word_lower = word.lower()

    with open(file['nome_do_arquivo'], 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            if word_lower in line.lower():
                occurrences.append({
                    'linha': line_number,
                    'conteudo': line.strip()
                })

    return occurrences


def exists_word(word, queue):
    results = []
    processed_files = set()  #

    for index in range(len(queue)):
        file = queue.search(index)

        if file['nome_do_arquivo'] in processed_files:
            continue

        occurrences = find_occurrences_in_file(word, file)

        if occurrences:
            results.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
            processed_files.add(file['nome_do_arquivo'])

    return results


def search_by_word(word, queue):
    results = []
    processed_files = set()

    for index in range(len(queue)):
        file = queue.search(index)

        if file['nome_do_arquivo'] in processed_files:
            continue

        occurrences = find_occurrences_with_content_in_file(word, file)

        if occurrences:
            results.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
            processed_files.add(file['nome_do_arquivo'])

    return results
