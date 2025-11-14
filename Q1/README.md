# Q1: Code Similarity Analysis - VidyaVichar MERN Implementations

## Overview
This project analyzes code similarity across multiple implementations of the VidyaVichar MERN stack project. It uses three levels of similarity analysis: **Textual**, **Structural**, and **Semantic**.

## Project Structure
```
Q1/
├── similarity_analysis.ipynb    # Main Jupyter notebook with all analysis
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── results/                     # Generated outputs
    ├── preprocessing_summary.csv
    ├── textual_similarity_matrix.csv
    ├── structural_similarity_matrix.csv
    ├── semantic_similarity_matrix.csv
    ├── combined_similarity_matrix.csv
    ├── analysis_summary.json
    ├── similarity_heatmaps.png
    ├── similarity_network.png
    ├── comparative_charts.png
    └── interactive_heatmap.html
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- All project repositories cloned in the parent directory

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Alternative: Using Conda
```bash
conda create -n similarity-analysis python=3.9
conda activate similarity-analysis
pip install -r requirements.txt
```

## Usage

### Running the Analysis
1. Ensure all project repositories are cloned in the parent directory (same level as Q1/)
2. Open the Jupyter notebook:
```bash
jupyter notebook similarity_analysis.ipynb
```
3. Run all cells sequentially (Cell → Run All)

### Expected Runtime
- Small projects (< 5): ~2-5 minutes
- Medium projects (5-15): ~5-10 minutes
- Large projects (15+): ~10-20 minutes

## Methodology

### Part A: Preprocessing
- **File Discovery**: Automatically discovers all project directories
- **Code Cleaning**: Removes comments, normalizes whitespace, skips minified files
- **Statistics Collection**: Counts LOC, React components, Express routes, Mongoose models
- **Output**: `preprocessing_summary.csv`

### Part B: Similarity Computation

#### 1. Textual Similarity (40% weight)
- **Method**: TF-IDF vectorization + Cosine similarity
- **Features**: Token-level and n-gram patterns (1-3 grams)
- **Purpose**: Detects copy-paste and similar coding patterns
- **Output**: `textual_similarity_matrix.csv`

#### 2. Structural Similarity (30% weight)
- **Method**: File structure analysis + Folder naming patterns
- **Features**: Directory depth, folder names, file type distributions
- **Purpose**: Identifies similar architectural patterns
- **Output**: `structural_similarity_matrix.csv`

#### 3. Semantic Similarity (30% weight)
- **Method**: Function/component name analysis + API endpoint matching
- **Features**: Function names, component names, API routes, dependencies
- **Purpose**: Captures functional and conceptual similarity
- **Output**: `semantic_similarity_matrix.csv`

#### Combined Score
Weighted average: `0.4×Textual + 0.3×Structural + 0.3×Semantic`

### Part C: Visualization
1. **Heatmaps**: 4-panel comparison of all similarity metrics
2. **Network Graph**: Cluster visualization with similarity threshold
3. **Bar Charts**: LOC, component counts, average similarities
4. **Interactive Heatmap**: Plotly-based explorable visualization

## Key Assumptions

1. **Project Location**: All team repositories are in the parent directory of Q1/
2. **Excluded Directories**: `node_modules`, `.git`, `dist`, `build`, `.next` are automatically skipped
3. **File Types**: Analysis focuses on `.js`, `.jsx`, `.ts`, `.tsx`, `.json`, `.css` files
4. **Minified Files**: Files with lines > 500 characters are considered minified and excluded
5. **Similarity Threshold**: Network graph uses 0.3 as the default threshold for displaying edges
6. **Encoding**: All files are read with UTF-8 encoding, errors are ignored
7. **Team Identification**: Team IDs are extracted from folder names using regex patterns

## Interpreting Results

### Similarity Scores
- **0.0 - 0.3**: Low similarity (very different implementations)
- **0.3 - 0.5**: Moderate similarity (some shared patterns)
- **0.5 - 0.7**: High similarity (many common elements)
- **0.7 - 1.0**: Very high similarity (potential code sharing)

### Key Metrics
- **Most Similar Pairs**: Projects with highest combined similarity scores
- **Least Similar Pairs**: Projects with lowest similarity (most unique)
- **Average Similarity**: Overall similarity of each project to all others
- **Network Clusters**: Groups of projects with similar implementations

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'X'`
**Solution**: Run `pip install -r requirements.txt`

**Issue**: Kernel crashes during execution
**Solution**: Reduce number of projects or increase memory allocation

**Issue**: "No projects found"
**Solution**: Ensure repositories are in parent directory, not inside Q1/

**Issue**: Slow execution
**Solution**: Check for very large projects, consider excluding them temporarily

**Issue**: Empty statistics for some projects
**Solution**: Check if project has unusual structure or is actually empty

## Output Files Description

| File | Description |
|------|-------------|
| `preprocessing_summary.csv` | Project statistics (LOC, files, components) |
| `textual_similarity_matrix.csv` | TF-IDF based similarity scores (NxN) |
| `structural_similarity_matrix.csv` | File structure similarity scores (NxN) |
| `semantic_similarity_matrix.csv` | Function/API similarity scores (NxN) |
| `combined_similarity_matrix.csv` | Weighted average similarity (NxN) |
| `analysis_summary.json` | Key statistics and findings |
| `similarity_heatmaps.png` | 4-panel heatmap visualization |
| `similarity_network.png` | Network graph of project clusters |
| `comparative_charts.png` | Bar charts comparing projects |
| `interactive_heatmap.html` | Interactive explorable heatmap |

## Extensions & Customization

### Adjusting Weights
Modify the weights in the "Combined Similarity Score" cell:
```python
weights = {'textual': 0.4, 'structural': 0.3, 'semantic': 0.3}
```

### Changing Network Threshold
Adjust the threshold for network visualization:
```python
threshold = 0.3  # Show only edges with similarity > 0.3
```

### Adding More Features
Extend the `extract_semantic_features()` function to include:
- CSS class names
- Database schema patterns
- Environment variable usage
- Error handling patterns

## Contact & Support
For questions or issues, please contact the course instructor or TA.

## License
This code is submitted as part of an academic assignment and is for educational purposes only.

---

**Author**: Student Submission
**Date**: November 2025
**Course**: Software Systems Development
**Assignment**: Q1 - Code Similarity Analysis
