from src.analyser import analyse_soundfile
from src.helpers.file_helper import get_files


def main() -> None:
    files = get_files()
    for file in files:
        analyse_soundfile(path_to_file=file)


if __name__ == "__main__":
    main()
