import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance.items:
        if item["nome_do_arquivo"] == path_file:
            print(f"Arquivo {path_file} já processado, ignorando...")
            return

    lines = txt_importer(path_file)

    metadata = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(metadata)

    print(metadata)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    fileName = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {fileName} removido com sucesso")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata)
    except IndexError:
        sys.stderr.write("Posição inválida")
