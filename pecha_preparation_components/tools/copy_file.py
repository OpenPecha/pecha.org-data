from pathlib import Path
import shutil


def copy_file(orig_path, dest_path):
    shutil.copy(Path(orig_path), Path(dest_path))


def recursive_copy_metadata(template, folder, pattern='*.docx'):
    for f in Path(folder).rglob(pattern):
        metadata = f.parent / f'{f.stem}.xlsx'
        copy_file(template, metadata)
