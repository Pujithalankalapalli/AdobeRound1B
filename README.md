# GenAI Challenge - Round 1B

## 📌 Task
Extract and structure relevant sections and sub-sections from academic PDFs to help a persona prepare for a specific topic.

## 👤 Persona
Graduate Chemistry Student

## 🎯 Job
Identify key concepts and mechanisms for exam preparation on **Reaction Kinetics**.

## 📂 Files
- `extractor.py`: Main logic for parsing and extracting sections.
- `utils.py`: Contains PDF parsing and section relevance functions.
- `round1b_output.json`: Final output in JSON format.
- `approach_explanation.md`: Methodology used for extraction.
- `Dockerfile`: Docker container setup for CPU-only processing.
- `sample_inputs/`: Contains input PDF files.

## 🧾 Output Format
The output JSON includes:
- Metadata
- Extracted Sections (document name, page number, section title, rank)
- Sub-section Analysis (document, page number, refined text)

## ⚙️ Constraints
- CPU-only execution
- Model size ≤ 1GB
- Processing time ≤ 60 seconds
- No Internet access

## 🚀 How to Run
```bash
python extractor.py --persona "Graduate Chemistry Student" --job "Identify key concepts and mechanisms for exam preparation on reaction kinetics"
