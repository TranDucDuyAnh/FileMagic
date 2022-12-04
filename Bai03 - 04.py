def update_file(text, file):
    with open(file, mode="a", encoding="utf-8") as f:
        f.write("\n")
        f.write(text)


def read_file(file):
    with open(file, mode="r", encoding="utf-8") as f:
        f.seek(0)
        print(f.read())


def main():
    text = str(input("Nhap mot chuoi ki tu: "))
    file = str(input("Nhap ten tap tin (../yourtextfile.txt): "))
    update_file(text, file)
    print("Tap tin da duoc cap nhat")
    read_file(file)


if __name__ == "__main__":
    main()
