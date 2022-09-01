import logging
import time

from parser import *
from normalize import normalize

from pathlib import Path
import shutil

import asyncio


def handle_media(filename: Path, target_folder: Path):
    filename = Path(filename)
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


def handle_other(filename: Path, target_folder: Path):
    filename = Path(filename)
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


def handle_archives(filename: Path, target_folder: Path):
    filename = Path(filename)
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Folder {folder} hasn`t deleted")


def is_folder(path: str):
    path = Path(path.replace('\\', '/'))
    if path.is_dir():
        return path
    else:
        return False


async def sort(folder: Path):
    if not is_folder(str(folder)):
        return 'Path not correct'

    await sorter(folder)

    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in DOC_DOCUM:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in DOCX_DOCUM:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in TXT_DOCUM:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in PDF_DOCUM:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in XLSX_DOCUM:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in PPTX_DOCUM:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
        # other
    for file in OTHER:
        handle_other(file, folder / 'OTHERS')
        # archives
    for file in ARCHIVES:
        handle_archives(file, folder / 'archives')
        # folder
    for folder in FOLDERS[::-1]:
        handle_folder(folder)
    return 'Your folder is sorted'


async def main(path):
    await asyncio.gather(sort(path), return_exceptions=False)


if __name__ == "__main__":
    start = time.time()
    path_directory = input('input some directory: ')
    if path_directory:
        folder_for_scan = Path(path_directory)
        print(f'start in folder {folder_for_scan.resolve()}')
        asyncio.run(main(folder_for_scan.resolve()))
        #sort(folder_for_scan.resolve())
        print(time.time()-start)