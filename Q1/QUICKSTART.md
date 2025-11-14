# Quick Start Guide - Code Similarity Analysis

## 🚀 Fast Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd Q1
pip install -r requirements.txt
```

### Step 2: Run the Analysis
```bash
jupyter notebook similarity_analysis.ipynb
```

Then click: `Cell → Run All`

### Step 3: Check Results
Results will be saved in the `results/` folder:
- CSV files with similarity matrices
- PNG images with visualizations
- HTML interactive heatmap
- JSON summary statistics

---

## 📊 What Gets Generated

| File | What It Shows |
|------|---------------|
| `preprocessing_summary.csv` | Lines of code, file counts, component counts for each project |
| `textual_similarity_matrix.csv` | How similar is the actual code text (0-1 scale) |
| `structural_similarity_matrix.csv` | How similar is the folder/file organization (0-1 scale) |
| `semantic_similarity_matrix.csv` | How similar are function names, APIs, dependencies (0-1 scale) |
| `combined_similarity_matrix.csv` | Overall similarity combining all three metrics |
| `similarity_heatmaps.png` | Visual heatmaps of all similarity types |
| `similarity_network.png` | Network graph showing which projects cluster together |
| `comparative_charts.png` | Bar charts comparing project sizes and components |
| `interactive_heatmap.html` | Click and explore the similarity matrix |

---

## 🎯 Understanding the Results

### Similarity Scores Meaning:
- **0.0 - 0.3**: 🟢 Very different (unique implementation)
- **0.3 - 0.5**: 🟡 Somewhat similar (shared patterns)
- **0.5 - 0.7**: 🟠 Quite similar (many commonalities)
- **0.7 - 1.0**: 🔴 Very similar (potential code sharing)

### What to Look For:
1. **Most Similar Pairs** - Projects with highest scores (check for plagiarism?)
2. **Least Similar Pairs** - Most unique/creative implementations
3. **Project Clusters** - Groups of teams that used similar approaches
4. **Average Similarity** - Which projects are "typical" vs "outliers"

---

## 📝 Writing Your Report

Use the `report_template.md` file as a starting point:

1. Run the notebook to get all statistics
2. Open `report_template.md`
3. Fill in the [brackets] with your actual results
4. Add the visualization images
5. Write your analysis and interpretations
6. Convert to PDF:
   ```bash
   # Option 1: Using pandoc
   pandoc report_template.md -o report.pdf

   # Option 2: Copy to Google Docs and export as PDF
   # Option 3: Copy to Word and save as PDF
   ```

---

## ⚠️ Common Issues

**Problem**: `ModuleNotFoundError`
**Fix**: `pip install -r requirements.txt`

**Problem**: Notebook runs very slowly
**Fix**: Normal for many projects. Can take 10-20 minutes for 14+ projects.

**Problem**: "No projects found"
**Fix**: Make sure project folders are in the parent directory, not inside Q1/

**Problem**: Kernel keeps crashing
**Fix**: Try restarting Jupyter and running cell-by-cell instead of "Run All"

---

## 🎓 For Your Submission

Make sure you have:
- ✅ `similarity_analysis.ipynb` - with all cells executed
- ✅ `results/` folder - with all generated files
- ✅ `report.pdf` - analytical write-up (1+ pages)
- ✅ `README.md` - explaining how to run your code
- ✅ All files in a folder named `Q1`

---

## 💡 Tips for Good Grades

1. **Run the full analysis** - Don't skip any similarity metrics
2. **Interpret the results** - Don't just show numbers, explain what they mean
3. **Discuss interesting findings** - Which pairs are surprisingly similar/different? Why?
4. **Critique the methodology** - What are the limitations? How could it be improved?
5. **Nice visualizations** - Make sure all plots are clear and well-labeled
6. **Professional report** - Use the template, add your insights, format nicely

---

## 📚 Understanding the Code

### Three Similarity Levels Explained:

**1. Textual Similarity (TF-IDF)**
- Treats code as text documents
- Counts how often words/tokens appear
- Similar to plagiarism detection in essays
- Good for finding copy-paste

**2. Structural Similarity**
- Looks at folder names and file organization
- Compares project architecture
- Shows if teams followed similar design patterns
- Independent of actual code content

**3. Semantic Similarity**
- Extracts function names, API endpoints, dependencies
- Compares "what the code does" not "how it's written"
- Can find similar logic even with different code
- Most advanced level of analysis

---

Good luck with your assignment! 🎉
