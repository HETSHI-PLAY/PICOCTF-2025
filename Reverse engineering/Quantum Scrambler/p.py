import ast

def unscramble(L):
    result = []
    queue = [L]

    while queue:
        item = queue.pop(0)
        if isinstance(item, list):
            for sub_item in item:
                queue.append(sub_item)
        else:
            result.append(chr(int(item, 16)))
    return ''.join(result)

def read_scrambled_flag_from_file(filename):
    with open(filename, 'r') as file:
        scrambled_flag = file.read().strip()

    try:
        scrambled_flag_list = ast.literal_eval(scrambled_flag)
    except Exception as e:
        print(f"Error converting scrambled flag to list: {e}")
        scrambled_flag_list = []

    return scrambled_flag_list

filename = 'scrambled_flag.txt'

scrambled_flag_list = read_scrambled_flag_from_file(filename)

flag = unscramble(scrambled_flag_list)
print(f"Unscrambled Flag: {flag}")
