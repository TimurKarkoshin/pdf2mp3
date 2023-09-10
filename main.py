from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path, language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Преобразуем файл: {Path(file_path).name}')
        print('[+] Выполняется...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 успешно сохранён!\n---Удачного дня!---'

    else:
        return "По данному пути нет искомого файла"


def main():
    tprint('PDF2MP3', font='block')
    file_path = input("\nВведите асболютный путь до файла(включая сам файл): ")
    language = input("Выберите язык введя 'en' или 'ru': ")
    while language not in ("en", "ru"):
        language = input("Выберите язык используемый в файле введя 'en' или 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
