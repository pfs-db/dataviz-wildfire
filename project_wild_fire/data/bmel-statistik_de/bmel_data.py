from pathlib import Path
import os


def get_pdf():
    """wget https://www.bmel-statistik.de/fileadmin/daten/0302250-2013.pdf"""
    for year in range(1992, 2023):
        file_name = f"0302250-{year}.pdf"
        if Path().joinpath(file_name).exists():
            os.remove(Path().joinpath(file_name))
        os.system(f"wget https://www.bmel-statistik.de/fileadmin/daten/{file_name}")


def main():
    get_pdf()


if __name__ == "__main__":
    main()
