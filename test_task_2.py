import os
from glob import glob

LABELS_DIR = '/tmp/labels'
IMAGE_PATTERNS = ('*.[pP][nN][gG]', '*.[jJ][pP][gG]', '*.[jJ][pP][eE][gG]')
META_EXT = '.[jJ][sS][oO][nN]'


def create_files(labels_dir):
    """Создаёт набор файлов, как указано в задании."""
    os.makedirs(labels_dir, exist_ok=True)
    labels = {
        "label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
        "label2": ["1.jpg", "1.json", "2.json", "3.json"],
        "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
        "label4": ["1.png", "1.txt", "2.txt", ],
    }
    for label in labels:
        label_path = os.path.join(labels_dir, label)
        os.makedirs(label_path, exist_ok=True)
        for item in labels[label]:
            open(os.path.join(label_path, item), 'a').close()
    open(os.path.join(labels_dir, "test.txt"), 'a').close()


def find_pattern(labels_dir, folder, pattern):
    """Ищет файл по паттерну в указанной папке и директории."""
    result = glob(os.path.join(labels_dir, folder, pattern))
    return result


def pair_files(labels_dir, image_patterns, meta_ext):
    """В директориях внутри указанной директории находит все
    пары файлов с одинаковыми названиями и расширениями image_patterns
    и meta_ext соответственно, помещает их в словарь где названию папки
    соответсвтуют все пары файлов, которые в ней находятся."""
    result = {}
    for folder in os.listdir(labels_dir):
        file_list = []
        for pattern in image_patterns:
            images = find_pattern(labels_dir, folder, pattern)
            for image in images:
                meta_list = find_pattern(
                    labels_dir,
                    folder,
                    f'{image.split(".")[0]}{meta_ext}'
                    )
                if len(meta_list) >= 1:
                    file_list.append([image, meta_list[0]])
        if len(file_list) >= 1:
            result[folder] = sorted(file_list, reverse=True)
    return result


def main():
    create_files(LABELS_DIR)
    result = pair_files(LABELS_DIR, IMAGE_PATTERNS, META_EXT)
    print(result)


if __name__ == '__main__':
    main()
