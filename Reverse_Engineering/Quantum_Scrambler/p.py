import ast

def unscramble(data):
    queue, result = [data], []
    
    while queue:
        item = queue.pop(0)
        if isinstance(item, list):
            queue.extend(item)
        else:
            result.append(chr(int(item, 16)))
    
    return ''.join(result)

def read_scrambled_flag(filename):
    try:
        with open(filename, 'r') as file:
            return ast.literal_eval(file.read().strip())
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

flag = unscramble(read_scrambled_flag('scrambled_flag.txt'))
print(f"Unscrambled Flag: {flag}")
