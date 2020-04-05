import feedparser
import json


def parse(url):
    return feedparser.parse(url)


def get_books(parsed):
    books = []
    entries = parsed['entries']
    for entry in entries:
        parsed_date = entry['published'].split()[:4]
        books.append({
            'book_name': parsed.feed['title'],
            'id': entry['id'],
            'audio_file': entry['id'],
            'duration': entry['itunes_duration'],
            'chapter_name': entry['title'],
            'taught_by': entry['summary'],
            'subtitle': entry['subtitle'],
            'published': entry['published'],
            'parsed_date': ' '.join(entry['published'].split()[:4]),
            'tags': entry['tags']
        })

    result = {'title': parsed.feed['title'], 'books': books}
    print('check below')
    final_data = json.dumps(result)
    print(type(final_data))
    return result

# data = parse(URL)
# test = get_books(data)
# json_data = json.dumps(test)
# print(json_data)
