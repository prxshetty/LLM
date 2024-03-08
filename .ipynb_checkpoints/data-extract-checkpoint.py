import os
from tqdm import tqdm #progress bar
import lzma

def xz_files_in_dir(directory):
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

folder_path = "C:/Users/prxsh/Downloads/openwebtext (1)/openwebtext"
output_file = "output{}.txt"
vocab_file = "vocab.txt"
split_files = int( input( "How many files do you want to split this into ?  "))