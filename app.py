import sys


def is_ready_to_be_env(line):
    index = line.index(":")
    return len(line[index:len(line)]) > 1


def is_parent(line):
    index = line.index(":")
    return len(line[index:len(line)]) == 1


def is_root(line):
    return not line.startswith(" ") and line.endswith(":")


def count_deeper(line):
    return len(line) - len(line.lstrip())


def find_parents(line, other_line):
    reversed_lines = other_line[::-1]
    deeper = count_deeper(line)
    if len(reversed_lines) == 0:
        return []
    parents = []
    deep = 1
    for line_ in reversed_lines:
        if deeper == count_deeper(line_):
            continue
        if is_root(line_):
            parents.append(line_)
            return parents
        if is_parent(line_) and (count_deeper(line_) == deeper - (deep * 2)):
            deep = deep + 1
            parents.append(line_)

    return parents


def upper_case_key(key):
    returned_key = ''
    for element in key:
        if element.isupper():
            element = "_" + element
        if element.islower():
            element = element.upper()
        returned_key += element
    return returned_key


def create_env(index, lines):
    line = lines[index]
    parents = find_parents(line, lines[0:index])
    value = line.split(': ')[1]
    key = ''
    for parent in parents[::-1]:
        key += parent.strip().replace(":", "_")
    key += line.strip().split(': ')[0]
    return f"{upper_case_key(key)}: {value}"


def process(yaml_location):
    lines = list(filter(None, (line.rstrip() for line in open(yaml_location))))
    env_to_return = ''
    for idx, line in enumerate(lines):
        if is_ready_to_be_env(line):
            env = create_env(idx, lines)
            env_to_return += f"{env}\n"
    return env_to_return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception('illegal arguments')
    yaml_location = sys.argv[1]
    env_location = sys.argv[2]
    env = process(yaml_location)
    with open(env_location, "w") as text_file:
        text_file.write(env)
