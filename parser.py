import time
from pathlib import Path

import asyncio


# изображения
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
# видео файлы
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
# DOCUMENTS
DOC_DOCUM = []
DOCX_DOCUM = []
TXT_DOCUM = []
PDF_DOCUM = []
XLSX_DOCUM = []
PPTX_DOCUM = []
# MUSIC
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
# ARCHIVES
ARCHIVES = []

OTHER = []
FOLDERS = []

REGISTER_EXTENSIONS = {
    # изображения
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    # видео файлы
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    # DOCUMENTS
    'DOC': DOC_DOCUM,
    'DOCX': DOCX_DOCUM,
    'TXT': TXT_DOCUM,
    'PDF': PDF_DOCUM,
    'XLSX': XLSX_DOCUM,
    'PPTX': PPTX_DOCUM,
    # MUSIC
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    # ARCHIVES
    'ZIP': ARCHIVES,
    'TAR': ARCHIVES,
    'GZ': ARCHIVES

}

EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    file_list = sorted(folder.glob("**/*"))
    return file_list


async def sorter(folder: Path) -> None:
    file_list = scan(folder)
    for i in range(len(file_list)):
        item = file_list[i]
        if item.is_dir():
            if item.name not in ("archives", "video", "audio", "documents", "images", "OTHER"):
                FOLDERS.append(item)
            continue

        ext = get_extension(item.name)
        fullname = item
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    start = time.time()
    path = Path(input('input some directory: '))
    asyncio.run(sorter(path))
    #sorter(path)
    for direct_name, inside_files in REGISTER_EXTENSIONS.items():
        print('\n')
        print(direct_name, inside_files)
        print('\n')
    print(time.time() - start)