import sys
import youtube_dl
from urllib.error import URLError
from urllib.error import HTTPError
from youtube_dl.utils import DownloadError

def get_url(f):
    result=list()
    for line in f.readlines():
        line=line.strip()
        if not len(line):
            continue
        result.append(line)
    return result

def clear_url(f):
    f.seek(0)
    f.truncate()
    f.close()

def download_no_matter_what(url):
    try:
        youtube_dl.YoutubeDL(options).download([url])
    except OSError:
        print('Error, Try later')
        urls.append(url)
    except TypeError:
        print('Error, Try later')
        urls.append(url)
    except URLError:
        print('Error, Try later')
        urls.append(url)
    except Warning:
        print('Error, Try later')
        urls.append(url)
    except HTTPError:
        print('Error, Try later')
        urls.append(url)
    except DownloadError:
        print('Error, Try later')
        urls.append(url)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Open the file that contains the URL
    f=open('C:\\Programs\\aria2\\download.txt','r+')

    # Read the URL from the command line
    urls=get_url(f)

    # Specify extra command line options here
    options = {
        'format': '720p',
        'outtmpl':'G:/CloudMusic/NewFolder/PH/%(title)s-%(uploader)s.%(ext)s',
        'proxy':'127.0.0.1:1081',
        'external_downloader': 'C:\\Programs\\aria2\\aria2c.exe',
        'external_downloader_args': ['-x','16','-k','1M'],
        'nooverwrites':'True',
        'hls_prefer_native':False,
        'prefer_ffmpeg':'True',
        'ffmpeg_location':'C:\\Programs\\aria2\\ffmpeg.exe',
        'continuedl':'True',
        'retries':30
    }

    # GET THAT VIDEO!
    for url in urls:
        download_no_matter_what(url)

    clear_url(f)
