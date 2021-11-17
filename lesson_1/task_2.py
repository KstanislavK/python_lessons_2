import os


def print_directory_contents(directory):
    print("Все папки и файлы:", os.listdir())
    for item in os.listdir():
        print(os.path.join(directory, item))


def main():
    print_directory_contents(os.getcwd())


if __name__ == '__main__':
    main()
