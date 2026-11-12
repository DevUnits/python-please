import tooly
import random
from datetime import datetime

lorem = tooly.Lorem()

profile = {
    "base": {
        "birth-day": lorem.date(past=29565)
    }
}

def gen_profile():
    return profile

def main():
    print("Python, please!\n")
    p = gen_profile()
    print(p["base"]["birth-day"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("Пока")
