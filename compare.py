import difflib

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def compare_docs(file1, file2):
    doc1 = load_file(file1)
    doc2 = load_file(file2)

    differ = difflib.unified_diff(doc1, doc2, lineterm='', fromfile='doc1', tofile='doc2')
    diff_result = '\n'.join(list(differ))
    return diff_result
