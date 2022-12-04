import numpy as np


def rng():
    np.random.seed(360)
    x = np.random.randint(low=-1000, high=1000, size=1000)
    return x


def save_text(x, file):
    with open(file, mode="w", encoding="utf-8") as f:
        for i in range(1, len(x) + 1):
            f.write(str(x[i-1]))
            if i % 10 == 0:
                f.write("\n")
            else:
                f.write(", ")


def read_text(file):
    with open(file, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            old_text = line.strip()
            new_text = old_text.replace(", ", "    ")
            print(new_text)


def main():
    file = str(input("Nhap ten tap tin (../yourtextfile.txt): "))

    x = rng()
    save_text(x, file)
    print("Mot danh sach so da duoc tao va luu")
    read_text(file)


if __name__ == "__main__":
    main()
