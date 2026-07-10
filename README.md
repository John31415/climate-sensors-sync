# Urban Air Quality and Climate Pattern Analysis

A hands-on capstone project that consolidates core pandas skills by ingesting messy, real-world-like urban air quality and climate data from two mismatched sensor networks, handling missing values, aligning misaligned indices, and producing a composite risk index to identify the city with the most extreme environmental conditions.

---

## ⚠️ Critical Requirement

This project was developed using **`uv`** (Astral's fast Python package and environment manager). **It is strictly mandatory to have `uv` installed** to manage dependencies and execute the virtual environment correctly. 

If you do not have it installed yet, you can do so by running:

```bash
# On macOS/Linux:
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

# On Windows (PowerShell):
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

---

## 🚀 Getting Started

Follow these steps after cloning the repository to get the project up and running in seconds:

### 1. Sync and install dependencies

You do not need to create a virtual environment manually. The following command will create the `.venv` environment and install all required dependencies ultra-fast:

```bash
uv sync
```

### 2. Run the project

To execute the main script:

```bash
uv run main.py
```

---

## 📌 Problem Definition

This project is a hands-on capstone exercise designed to consolidate the core concepts taught in Chapter 5 of *Python for Data Analysis*: pandas' fundamental data structures (`Series` and `DataFrame`), intrinsic data alignment through Index objects, missing-data handling, label- and position-based indexing (`loc` / `iloc`), and descriptive statistics.

👉 **[Read the full problem definition and mathematical requirements here](./PROBLEM.md)**
