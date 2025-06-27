## Background
Many proponents of AGI argue that recursive self-improvement will drive the intelligence explosion toward superintelligence, making the capacity for genuine algorithmic novelty an important milestone for future AI progress. Thus, it is vital to see if any benchmarks of novelty hold. I begin this process with a simple (and poor) proxy assessment.

[A review on the novelty measurements of academic papers](https://link.springer.com/article/10.1007/s11192-025-05234-0) (Zhao & Zhang, 2025) introduces a method to quantify the novelty of academic papers. This forms the metric of analysis we will base story novelty off of.

[WritingBench: A Comprehensive Benchmark for Generative Writing](https://arxiv.org/pdf/2503.05244) (Wu et al., 2025) ([HuggingFace](https://huggingface.co/spaces/WritingBench/WritingBench)) ([GitHub](https://github.com/X-PLUG/WritingBench)) introduces the WritingBench evaluation from which we can select an open-source model that performs well on creative writing tasks. The model selected is DeepSeek R1.

## Methodology
The pipeline involves ingesting 300 K WritingPrompts prompts to generate matching AI stories with DeepSeek-R1-Distill-Llama-70B, computing span embeddings using a sentence transformer, and then assessing novelty via a suite of metrics and visualizations. 
- Model: [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)
- Dataset: [Writing Prompts](https://www.kaggle.com/datasets/ratthachat/writing-prompts)
- Embeddings: [Qwen3-Embedding-0.6B](http://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- Metrics: [A review on the novelty measurements of academic papers](https://link.springer.com/article/10.1007/s11192-025-05234-0)

## Goals and Expected Results
Visualization of the embeddings:
- Project embeddings via [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) for local cluster inspection.
- Use [UMAP](https://umap-learn.readthedocs.io/en/latest/) for global structure plots.

Novelty Benchmarking (textual-data based measures): Bio-Entity Pair Distance (Liu et al. 2022), Life-Index & Semantic Novelty (Luo et al. 2022), Multi-Entity Contributions (Chen et al. 2024), N-Gram Presence (Chen & Fang 2019), Contribution-Sentence Cloud Similarity (Wang et al. 2024)

## Limitations
Pre-training Overlap: The model may have seen WritingPrompts data in pre-training, potentially biasing similarity measures. However, considering we’re looking for novel content, this ingestion should be a non-issue.

Metric Sensitivity: the novelty metric is only a proxy to “true” creativity which is likely the underlying mechanism needed for RSI.

## Next Steps
Do this analysis on research publications co-authored by AI so the entire novelty assessment suite can be utilized and a better proxy for creativity can be assessed.