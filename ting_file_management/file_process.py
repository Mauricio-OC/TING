def process(path_file, instance):
    terms = txt_importer(path_file)
    for term in terms:
        instance.enqueue(term)

def remove(instance):
    instance.dequeue()

def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Índice Inválido ou Inexistente")

