FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir pymupdf scikit-learn

# Copy the extractor script
COPY extractor_1b.py .

# Create input and output directories
RUN mkdir input output

# Default command to run the script (override with args)
CMD ["python", "extractor_1b.py", "--input_dir", "input", "--output_dir", "output", "--persona", "Undergraduate Chemistry Student", "--job", "Identify key concepts and mechanisms for exam preparation on reaction kinetics"]
