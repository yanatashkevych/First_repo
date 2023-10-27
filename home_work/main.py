from pathlib import Path
import shutil
import sys
import file_parser
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    normalized_name = normalize(file_name.stem) + file_name.suffix
    file_name.replace(target_folder / normalized_name)

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    file_parser.scan(folder)
    for file in file_parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in file_parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in file_parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in file_parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in file_parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3_AUDIO')
    for file in file_parser.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV_AUDIO')
    for file in file_parser.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR_AUDIO')
    for file in file_parser.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG_AUDIO')
    for file in file_parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV_VIDEO')
    for file in file_parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV_VIDEO')
    for file in file_parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI_VIDEO')
    for file in file_parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4_VIDEO')
    for file in file_parser.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT_DOCUMENTS')
    for file in file_parser.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC_DOCUMENTS')
    for file in file_parser.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX_DOCUMENTS')
    for file in file_parser.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX_DOCUMENTS')
    for file in file_parser.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF_DOCUMENTS')
    for file in file_parser.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX_DOCUMENTS')

    for file in file_parser.MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')

    for file in file_parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives'/ 'ZIP_ARCHIVES')
    for file in file_parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives'/ 'GZ_ARCHIVES')
    for file in file_parser.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives'/ 'TAR_ARCHIVES')

    for folder in file_parser.FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')

            
if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process)