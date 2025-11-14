# Q2: Image Blurring Implementation and Performance Analysis

## Overview
This project implements and analyzes two methods for applying a 3x3 mean blur filter to images: an iterative Python approach and a vectorized NumPy approach.

## Requirements

### Python Version
- Python 3.6 or higher

### Required Libraries
Install the required packages using pip:

```bash
pip install numpy pillow matplotlib jupyter
```

Or using conda:

```bash
conda install numpy pillow matplotlib jupyter
```

### Library Versions (Tested)
- numpy >= 1.19.0
- Pillow >= 8.0.0
- matplotlib >= 3.3.0
- jupyter >= 1.0.0

## Running the Notebook

1. Navigate to the Q2 directory:
   ```bash
   cd Q2
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook box_blur.ipynb
   ```

3. In the Jupyter interface, run all cells in sequence using "Cell > Run All" or run each cell individually using Shift+Enter.

## Assumptions

1. **Font Availability**: The notebook attempts to use system fonts (Helvetica on macOS, Arial on Windows). If these are not available, it falls back to the default PIL font.

2. **Image Size**: The implementation uses a 400x200 pixel image as specified in the requirements.

3. **Border Handling**: Both implementations exclude the outermost single-pixel boundary when applying the blur filter, as specified.

4. **Data Type**: The image is created as an 8-bit grayscale image (dtype uint8), with pixel values ranging from 0 to 255.

5. **Timing**: Benchmarking uses Python's `time.time()` function. For very fast operations, running the notebook multiple times may show slight variations in timing.

## Expected Output

When you run the notebook, you should see:

1. **Image generation confirmation** with shape and dtype information
2. **Execution times** for both implementations (blur_python and blur_numpy)
3. **Performance comparison** showing the speedup factor
4. **Three side-by-side images**: original, blurred (Python), and blurred (NumPy)
5. **Verification** confirming both implementations produce identical results

## Troubleshooting

### Font Issues
If you see a warning about fonts, the code will automatically fall back to the default font. The blur functionality will still work correctly.

### Import Errors
Ensure all required libraries are installed:
```bash
pip install --upgrade numpy pillow matplotlib jupyter
```

### Jupyter Not Found
Install Jupyter:
```bash
pip install jupyter
```

## File Structure

```
Q2/
├── box_blur.ipynb    # Main implementation notebook
└── README.md         # This file
```

## Notes

- The notebook is self-contained and generates all required data programmatically
- No external image files are needed
- All code follows the strict requirements specified in the assignment
- The analysis section is included as markdown cells in the notebook
