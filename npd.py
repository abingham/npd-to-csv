# Convert "npd format" data files to CSV for easy spreadsheet importing.
#
# Usage: python npd.py input.txt > output.csv
#
# NB! This requires Python 3.3 or higher


def header_fields(line):
    start = 0
    prev_space = False
    for idx in range(len(line)):
        if line[idx] != ' ':
            if prev_space:
                yield line[start:idx]
                start = idx
            prev_space = False
        else:
            prev_space = True


def parse_line(line, fields):
    start = 0
    for field in fields:
        end = start + len(field)
        yield line[start:end]
        start = end


def parse(filename):
    with open(filename, mode='rt') as f:
        lines = iter(f)
        fields = list(header_fields(next(lines)))
        yield fields
        yield from (list(parse_line(l, fields)) for l in lines)


if __name__ == '__main__':
    import sys
    for line in parse(sys.argv[1]):
        print(','.join(line))
