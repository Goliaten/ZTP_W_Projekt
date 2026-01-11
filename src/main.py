import os
from src import config
from src.analyser import analyse_soundfile
from src.classifiers import train_and_evaluate_knn
from src.helpers.file_helper import get_files
from src.helpers.output_saver import save_dict_to_csv


def main() -> None:
    results = {}
    files = get_files()
    print(f"Detected {len(files)} sound files.")
    for file in files:
        path, filename = os.path.split(file)
        file_class = os.path.split(path)[1]
        analyse_result = analyse_soundfile(path_to_file=file)

        analyse_result |= {"class": file_class, "filename": filename}
        results[file] = analyse_result

    save_dict_to_csv(results, config.RESULT_CSV_FILENAME)
    knn_result = train_and_evaluate_knn()
    from pprint import pprint

    pprint(knn_result)


if __name__ == "__main__":
    main()
