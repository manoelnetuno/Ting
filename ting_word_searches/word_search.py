
def exists_word(word, queue):
    results = []
    word_lower = word.lower()

    for index in range(len(queue)):
        file = queue.search(index)
        occurrences = []
    with open(file['nome_do_arquivo'], 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            if word_lower in line.lower():
                occurrences.append({'linha': line_number})

            if occurrences:
                results.append({
                    'palavra': word,
                    'arquivo': file['nome_do_arquivo'],
                    'ocorrencias': occurrences
                })

    return results


def search_by_word(word, queue):
    results = []
    word_lower = word.lower()

    for index in range(len(queue)):
        file = queue.search(index)
        occurrences = []
        with open(file['nome_do_arquivo'], 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if word_lower in line.lower():
                    occurrences.append({
                        'linha': line_number,
                        'conteudo': line.strip()})

        if occurrences:
            results.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
                })

    return results
