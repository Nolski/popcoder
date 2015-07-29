import json
import sys

from popcoder import Popcoder


def main():
    popcoder = Popcoder()

    data = None
    with open('popcorn.json', 'r') as f:
        data = json.loads(f.read())

    popcoder.process_json(data['data'], data['background'])

if __name__ == '__main__':
    sys.exit(main() or 0)
