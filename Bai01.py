def save_text(text, file):
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)


def main():
    text = str(input("Nhap mot chuoi ki tu: "))
    file = str(input("Nhap ten tap tin (../yourtextfile.txt): "))
    save_text(text, file)
    print("Chuoi da duoc luu")


if __name__ == "__main__":
    main()
