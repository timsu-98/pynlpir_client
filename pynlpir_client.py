import os

import pynlpir

class PyNLPIRClient:
    def __init__(self, read_dirs: list, output_dir: str) -> None:
        pynlpir.open()
        self.read_dirs = read_dirs
        self.output_dir = output_dir
    
    def analyse_files(self, segment: bool=True, get_key_words: bool=False, weighted: bool=True, statistic: bool=True):
        for read_dir in self.read_dirs:
            read_files = os.listdir(read_dir)
            for read_file in read_files:
                path_to_read_file = read_dir + '/' + read_file
                path_to_write_file = self.output_dir + '/' + read_file
                with open(path_to_read_file, 'r') as rf, open(path_to_write_file, 'w') as wf:
                    lines = rf.read().split('\n')
                    if segment:
                        for line in lines:
                            segmented_line = pynlpir.segment(line)
                            wf.write(line + '\n')
                            wf.write(str(segmented_line) + '\n')
                    if get_key_words:
                        keywords = pynlpir.get_key_words(" ".join(lines), weighted=weighted)
                        wf.write('\n\n\n##################### Keyword Analysis #####################\n')
                        writable_keywords = ""
                        for keyword in keywords:
                            writable_keywords += str(keyword) + '\n'
                        wf.write(writable_keywords)
    
    def add_read_dir(self, dir: str):
        self.read_dirs.append(dir)
    
    def change_output_dir(self, dir: str):
        self.output_dir = dir

    def close_client(self):
        pynlpir.close()
    