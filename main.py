from compare import compare_docs
from summarizer import summarize_diff

if __name__ == "__main__":
    file1 = 'docs/doc1.txt'
    file2 = 'docs/doc2.txt'

    print("[+] Comparing documents...")
    diff_text = compare_docs(file1, file2)
    print(diff_text)

    print("\n[+] Summarizing differences with OpenAI...")
    summary = summarize_diff(diff_text)
    print("\nSummary:\n", summary)
