def exists_word(word, instance):
    result = []

    for item in instance.items:
        file_name = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]

        for line_number, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrence = {"linha": line_number}
                found_word_info = {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": [occurrence],
                }
                existing_result = next(
                    (r for r in result if r["arquivo"] == file_name), None
                )
                if existing_result:
                    existing_result["ocorrencias"].append(occurrence)
                else:
                    result.append(found_word_info)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
