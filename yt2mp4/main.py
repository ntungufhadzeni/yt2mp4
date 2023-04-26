from pytube import YouTube
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Convert Youtube video to mp4')
    parser.add_argument('-l', '--link', type=str, help='Youtube link', required=True)
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory to save video')

    args = parser.parse_args()
    link = args.link
    path = args.directory

    if os.path.isdir(path):
        os.chdir(path)
    else:
        raise NotADirectoryError(path)

    yt = YouTube(link)
    print('Download...')
    yt.streams.filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download()
