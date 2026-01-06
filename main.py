import hashlib

class URLShortener:
    def __init__(self):
        self.store = {}

    def shorten(self, url):
        code = hashlib.md5(url.encode()).hexdigest()[:6]
        self.store[code] = url
        return code

    def resolve(self, code):
        return self.store.get(code)


def run():
    shortener = URLShortener()
    code = shortener.shorten("https://example.com")
    shortener.resolve(code)


if __name__ == "__main__":
    run()
