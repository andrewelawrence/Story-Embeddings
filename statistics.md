# Dataset Statistics
This document outlines the statistical measures extracted from the WritingPrompts dataset to support the novelty analysis and embedding computation. Assume statistics computed against both original and generated stories.
#### Text Statistics
- *Word count & length (characters)* 
  - Raw/min/max/mean/median/std
- *Token count (prompts & stories)*
  - Raw/min/max/mean/median/std
  - Needed to set Qwen3-Embedding-0.6B processing limits & DeepSeek-R1-Distill-Llama-70B generation limits
- *Sentence count & length (words)*
  - Raw/min/max/mean/median
- *Line count & length (words)*
  - Raw/min/max/mean/median
- *Paragraph count & length (words, sentences)* 
  - Raw/min/max/mean/median
#### Vocabulary Diversity
- *Vocabulary size & richness*
  - Total unique words, Type-Token Ratio (TTR)
  - Lexical diversity baseline
- *N-gram diversity*
  - Unique bigrams, trigrams, 4-grams counts and ratios
  - Needed for Fang et al. n-gram presence novelty metric
- *Lexical diversity (MTLD)*
  - More robust diversity measure than TTR ([McCarthy et al.](https://link.springer.com/article/10.3758/BRM.42.2.381))
- *Rare word frequency*
  - Proportion of hapax legomena (words appearing once), dis legomena (twice)
  - Vocabulary uniqueness assessment
#### Content & Complexity Analysis
- *Readability*
  - Flesch-Kincaid Grade Level, SMOG Index, Flesch Reading Ease
  - To grasp content complexity baseline
- *Part-of-Speech distribution*
  - Noun/verb/adjective/adverb ratios
  - For syntactic pattern analysis
- *Named entity statistics*
  - Person/place/organization mention counts and diversity
  - Needed for Liu et al. Bio-Entity Pair Distance novelty metric
#### Dataset Quality & Preprocessing
- *Data quality*
  - Empty stories, extremely short (<10 words), extremely long (>10k words)
  - To ensure a clean dataset for embedding computation
- *Character encoding issues*
  - Non-ASCII character frequency, encoding error counts
  - For data preprocessing
- *Prompt-Story Correlation*
  - Correlation between prompt length and story length (words/tokens)
  - Embedding cosine similarity between prompts and stories
  - To understand generation patterns
#### Embedding Preparation
- *Outlier detection*
  - Stories beyond 1.5 IQR from median length
  - Identify *potential* preprocessing candidates (removing statistical outliers that might skew embedding analysis)
#### Output Formatting
Each statistic should be computed and stored as:
```python
{
    "metric_name": {
        "raw": list | None,
        "min": float | None,
        "max": float | None, 
        "mean": float | None,
        "median": float | None,
        "std": float | None,
        "count": int | None
    }
}
```