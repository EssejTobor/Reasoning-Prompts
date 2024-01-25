import py7zr

# Path to your 7z file
file_path = 'data\Fiverr.7z'

# Directory where files will be extracted
extract_path = 'Fiverr'

# Extracting the 7z file
with py7zr.SevenZipFile(file_path, mode='r') as z:
    z.extractall(path=extract_path)