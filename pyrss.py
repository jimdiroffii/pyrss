import feedparser


def add_feed(url):
    try:
        f = open("feeds.txt", "a")
        f.write(url + "\n")
    except:
        print("File IO Error: Could not add feed. Please try again.")
    finally:
        f.close()
        return


def read_all_feeds():
    try:
        f = open("feeds.txt", "r")
        for line in f:
            d = feedparser.parse(line)
            print(d["feed"]["title"])
            print(d["feed"]["description"])
            print(d["feed"]["link"])
    except:
        print("File IO Error: Could not read feeds. Please try again.")
    finally:
        f.close()
        return


def delete_feed(url):
    try:
        f = open("feeds.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("feeds.txt", "w")
        for line in lines:
            if line != url + "\n":
                f.write(line)
    except:
        print("File IO Error: Could not delete feed. Please try again.")
    finally:
        f.close()
        return


def list_all_feeds():
    try:
        f = open("feeds.txt", "r")
        for line in f:
            print(line)
    except:
        print("File IO Error: Could not list feeds. Please try again.")
    finally:
        f.close()
        return


def get_url():
    url = input("Enter a feed URL: ")
    return url


def menu():
    print("PyRSS")
    print("1. Add a feed")
    print("2. Delete a feed")
    print("3. List all feeds")
    print("4. Read all feeds")
    print("5. Exit")
    print()


def main():
    while True:
        menu()
        d = input("Enter a menu # (or q to exit): ")
        match d:
            case "q":
                break
            case "1":
                url = get_url()
                add_feed(url)
            case "2":
                url = get_url()
                delete_feed(url)
            case "3":
                list_all_feeds()
            case "4":
                read_all_feeds()


if __name__ == "__main__":
    main()
