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
    f=open('#direct path to the file contains the urls','r+')

    # Read the URL from the command line
    urls=get_url(f)

    # Specify extra command line options here
    options = {
        'format': 'best',
        'outtmpl':'',#output template ,check Readme.md from youtube-dl
        'proxy':'127.0.0.1:1081',
        'external_downloader': '',#direct path to external-downloader here
        #'external-downloader-args': '-x 16 -k 1M', #optional arguments
        'no-overwrites':'true',
        'retries':30
    }

    # GET THAT VIDEO!
    for url in urls:
        download_no_matter_what(url)

    clear_url(f)
