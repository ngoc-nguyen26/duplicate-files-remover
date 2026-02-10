import hashlib
import os

# Returns the hash string of the given file name


def hashFile(filename, BLOCKSIZE=65536):
    # Reading large files at once can cause memory issues, so we take a blocksize to read at a time
    hasher = hashlib.md5()  # (64 KB)
    with open(filename, 'rb') as f:
        # Reads the particular blocksize from file
        while block := f.read(BLOCKSIZE):
            hasher.update(block)
    return hasher.hexdigest()


if __name__ == "__main__":
    # Dictionary to store the hash and filename
    hashMap = {}

    # List to store deleted files
    deletedFiles = []
    filelist = [f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key = hashFile(f)
        # If key already exists, it deletes the file
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')