import re
from sys import exit

def main():
    print(parse(input("HTML: ")))

def parse(s):
    s_list = s.split()
    for data in s_list:
        if data.startswith("src="):
            data.lstrip("src=")
            return shareable(re.search(r'"(?:http|https)://(?:www\.)?youtube\.com/embed/[\w-]+"', data))
    return None

def shareable(url):
    try:
        if url:
            query = url[0].split("/")
            query[-1] = query[-1].rstrip('"')
            return ("https://youtu.be/" + query[-1])
        else:
            return None
    except Exception:
        exit(None)


if __name__ == "__main__":
    main()