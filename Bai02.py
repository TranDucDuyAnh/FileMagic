def read_file(file):
    with open(file, mode="r", encoding="utf-8") as f:
        f.seek(0)
        print(f.read())


def main():
    file = str(input("Nhap ten tap tin (../yourtextfile.txt): "))
    read_file()


if __name__ == "__main__":
    main()
