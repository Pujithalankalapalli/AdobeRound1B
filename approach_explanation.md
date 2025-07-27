# Approach Explanation for Round 1B

In this challenge, the goal is to build an intelligent document analysis system that extracts and prioritizes relevant sections from multiple PDFs based on a specific persona and their job-to-be-done.

Our solution follows these steps:

1. **Section Extraction:**  
   We use PyMuPDF to parse each PDF document page-wise and extract text blocks. To keep it generic and scalable, we consider all sizable text blocks as potential sections.

2. **Relevance Ranking:**  
   We combine the persona description and the job-to-be-done into a single query string. Using TF-IDF vectorization (from scikit-learn), we transform the query and document sections into vector space. Then, cosine similarity scores identify how closely each section matches the persona's needs.

3. **Ranking & Output:**  
   The top-ranking sections per document are selected and output in a JSON format with metadata including input docs, persona, job, and processing timestamp. Each section includes document name, page number, section title snippet, and importance rank. Additionally, a sub-section analysis includes the full text and page number.

4. **Constraints:**  
   The entire process runs on CPU with a lightweight model (TF-IDF), no internet access, and completes quickly for 3-5 PDFs. This avoids heavy NLP models while maintaining relevance accuracy.

This approach ensures a generic, extensible, and interpretable system suitable for diverse documents and personas without violating resource constraints.
