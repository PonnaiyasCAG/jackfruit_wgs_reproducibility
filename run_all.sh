#!/usr/bin/env bash
# ==============================================================================
# Jackfruit WGS Publication Reproducibility Runner
# Reproduces all figures and analytical tables for journal submission.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "====================================================================="
echo "  Artocarpus heterophyllus (Jackfruit PLJS) Genomics Reproducibility"
echo "====================================================================="

# 1. Check Python dependencies
python3 -c "import pandas, numpy, matplotlib, scipy; print('✓ Scientific Python libraries detected.')"

# 2. Run All Visualizations (Figures 1 through 14)
echo ""
echo ">> Generating All Publication Figures (300 DPI)..."
python3 scripts/visualization/render_all_figures.py

# 3. Run Analysis Demonstrations
echo ""
echo ">> Running Analytical Script Checks..."
python3 scripts/analysis/calc_comparative_go_kegg_enrichment.py data/comparative_top_GO_BP.tsv
python3 scripts/analysis/parse_orthofinder_families.py data/Orthogroups.GeneCount.tsv

echo ""
echo "====================================================================="
echo "  All outputs successfully generated! Check the figures/ folder."
echo "====================================================================="
