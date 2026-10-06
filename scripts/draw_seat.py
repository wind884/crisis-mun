"""Draw uniformly from a pre-agreed JSON list of eligible countries or seats."""

import json
import secrets
import sys


def draw(pool):
    if not isinstance(pool, list) or not pool:
        raise ValueError('Expected a non-empty JSON list of names.')
    if any(not isinstance(item, str) or not item.strip() for item in pool):
        raise ValueError('Every entry must be a non-empty name.')
    names = [item.strip() for item in pool]
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError('Duplicate names would bias the draw.')
    index = secrets.randbelow(len(names))
    return {
        'pool': names,
        'index': index + 1,
        'selected': names[index],
        'probability': f'1/{len(names)}',
        'method': 'secrets.randbelow',
    }


def main():
    try:
        result = draw(json.load(sys.stdin))
    except (ValueError, TypeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
