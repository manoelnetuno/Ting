from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            print(f"Arquivo '{path_file}' já foi processado. Ignorando.")
            return

    linhas = txt_importer(path_file)

    arquivo_processado = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas,
    }

    instance.enqueue(arquivo_processado)

    sys.stdout.write(f"{arquivo_processado}\n")


def remove(instance):
    if len(instance) == 0:
        return print('Não há elementos')
    else:
        removed_arq = instance.dequeue()
        return print(
            f"Arquivo {removed_arq['nome_do_arquivo']} removido com sucesso"
            )


def file_metadata(instance, position):
    if position >= 0 and position < len(instance):
        return print(instance.search(position))
    print('Posição inválida', file=sys.stderr)
