import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(r'"(?:http|https)://(?:www\.)?youtube\.com/embed/([\w-]+)"', s):
        return shareable(match.group(1))
    return None

def shareable(video_id):
    if video_id:
        return (f"https://youtu.be/{video_id}")
    else:
        return None


if __name__ == "__main__":
    main()