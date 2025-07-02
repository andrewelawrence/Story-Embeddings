# 0. Install requirements.txt
# ----
pip install -r requirements.txt

# 1. Dataset downloading and processing
# ----
# Download parquet files from HuggingFace
huggingface-cli download euclaise/writingprompts \
  --repo-type dataset \
  --local-dir . \
  --include data/*.parquet 

# Merge train/valid/test parquet files into single data.parquet 
python3 -c "
import polars as pl
import rootutils
from pathlib import Path

root = rootutils.setup_root('.', dotenv=True, pythonpath=True, cwd=True)

df = pl.read_parquet('data/*.parquet')
df.write_parquet(Path(root, 'data/data.parquet'))
"
# Clean up data/
find data/ -name "*.parquet" -not -name 'data.parquet' -delete


# 2. Inspect the dataset
# ----
# TODO
