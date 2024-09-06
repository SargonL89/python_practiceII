import re

hours_am = {
    "12": "00",
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11",
    }
hours_pm = {
    "12": "12",
    "1": "13",
    "2": "14",
    "3": "15",
    "4": "16",
    "5": "17",
    "6": "18",
    "7": "19",
    "8": "20",
    "9": "21",
    "10": "22",
    "11": "23"
    }

def main():
        print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", s):

        start_hour, start_minute, start_period = match.group(1), match.group(2) or ":00", match.group(3)
        end_hour, end_minute, end_period = match.group(4), match.group(5) or ":00", match.group(6)

        if start_period == "AM":
            inicio = hours_am[start_hour] + start_minute
        else:
            inicio = hours_pm[start_hour] + start_minute
        if end_period == "AM":
            fin = hours_am[end_hour] + end_minute
        else:
            fin = hours_pm[end_hour] + end_minute

        return (f"{inicio} to {fin}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()