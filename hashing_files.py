import hashlib
import os


def get_sha512(file_path):
    h = hashlib.sha3_512()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def get_sha(file_path):
    h = hashlib.sha1()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def get_files():
    return list(os.walk(r"."))[0][-1]


if __name__ == '__main__':
    ext_list = ['py', 'txt', 'md', 'sha', 'dat']
    base_name, _ = os.path.splitext(__file__)
    # print(os.path.basename(__file__))
    files = get_files()
    # print(files)
    with open(base_name + ".sha", "w") as fn:
        for f in files:
            _, ext = os.path.splitext(f)
            if ext in ext_list:
                fn.write(f"{get_sha(f)} *{f}\n")

    files = get_files()
    # print(files)
    with open(base_name + ".sha3", "w") as fn:
        for f in files:
            _, ext = os.path.splitext(f)
            if ext in ext_list:
                fn.write(f"{get_sha512(f)} *{f}\n")
