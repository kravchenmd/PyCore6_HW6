import sys
from pathlib import Path

# containers for file names
IMAGES = []
DOCUMENTS = []
AUDIO = []
VIDEO = []
ARCHIVES = []
OTHER_TYPES = []

# dict to choose proper container based on the type of file
EXTENSIONS_CONT = {
    'IMAGES': IMAGES,
    'DOCUMENTS': DOCUMENTS,
    'AUDIO': AUDIO,
    'VIDEO': VIDEO,
    'ARCHIVES': ARCHIVES
}

# dict with types of files and known extensions
EXTENSIONS_DICT = {
    'IMAGES': ('jpg', 'jpeg', 'png', 'svg'),
    'DOCUMENTS': ('txt', 'doc', 'docx', 'pdf'),
    'AUDIO': ('mp3',),
    'VIDEO': (),
    'ARCHIVES': ('zip',)
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].lower()  # just changed to lower()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Если это папка то добавляем ее с список FOLDERS и преходим к следующему элементу папки
        if item.is_dir():
            # проверяем, чтобы папка не была той в которую мы складываем уже файлы
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER_TYPES'):
                FOLDERS.append(item)
                #  сканируем эту вложенную папку - рекурсия
                scan(item)
            #  перейти к следующему элементу в сканируемой папке
            continue

        #  Пошла работа с файлом
        ext = get_extension(item.name)  # взять расширение
        fullname = folder / item.name  # взять полный путь к файлу
        if not ext:  # если у файла нет расширения добавить к неизвестным
            OTHER_TYPES.append(fullname)
        else:
            try:
                for k, v in EXTENSIONS_DICT.items():
                    # at first choose type of extention
                    if ext in v:
                        # then choose proper contaner
                        container = EXTENSIONS_CONT[k]

                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Если мы не регистрировали расширение в REGISTER_EXTENSIONS, то добавить в другое
                UNKNOWN.add(ext)
                OTHER_TYPES.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images: {IMAGES}')
    print(f'Documents: {DOCUMENTS}')
    print(f'Audio: {AUDIO}')
    print(f'Archives: {ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')

    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
