import os
import fitz  
import json
import datetime
import argparse
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        text += span["text"] + " "
                text = text.strip()
                if len(text) > 20:  
                    sections.append({
                        "text": text,
                        "page": page_num + 1,
                    })
    return sections

def rank_sections(sections, persona, job):
    query = (persona + " " + job).lower()
    corpus = [sec["text"].lower() for sec in sections]

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    corpus_vectors = vectorizer.fit_transform(corpus)
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(query_vector, corpus_vectors).flatten()

    for i, score in enumerate(scores):
        sections[i]["score"] = float(score)
    sections_sorted = sorted(sections, key=lambda x: x["score"], reverse=True)
    return sections_sorted

def main():
    parser = argparse.ArgumentParser(description="Round 1B Document Intelligence Extractor")
    parser.add_argument("--input_dir", type=str, default="input", help="Folder containing PDF files")
    parser.add_argument("--output_dir", type=str, default="output", help="Folder to save output JSON")
    parser.add_argument("--persona", type=str, required=True, help="Persona role description")
    parser.add_argument("--job", type=str, required=True, help="Job to be done description")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    all_docs = []
    output_data = {
        "metadata": {
            "input_documents": [],
            "persona": args.persona,
            "job_to_be_done": args.job,
            "processing_timestamp": datetime.datetime.now().isoformat(),
        },
        "extracted_sections": [],
        "sub_section_analysis": []
    }

    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(args.input_dir, filename)
            all_docs.append(filename)

            sections = extract_sections(pdf_path)

            ranked_sections = rank_sections(sections, args.persona, args.job)

            top_sections = ranked_sections[:5]

            for rank, sec in enumerate(top_sections, start=1):
                output_data["extracted_sections"].append({
                    "document": filename,
                    "page_number": sec["page"],
                    "section_title": sec["text"][:100],  # truncate to 100 chars
                    "importance_rank": rank
                })
                output_data["sub_section_analysis"].append({
                    "document": filename,
                    "refined_text": sec["text"],
                    "page_number": sec["page"]
                })

    output_data["metadata"]["input_documents"] = all_docs

    output_file = os.path.join(args.output_dir, "result_1b.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    main()
