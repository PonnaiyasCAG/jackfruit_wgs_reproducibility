@echo off
REM ==============================================================================
REM Jackfruit WGS Publication Reproducibility Runner (Windows)
REM ==============================================================================

echo =====================================================================
echo   Artocarpus heterophyllus (Jackfruit PLJS) Genomics Reproducibility
echo =====================================================================

python -c "import pandas, numpy, matplotlib, scipy; print('✓ Scientific Python libraries detected.')"
if %ERRORLEVEL% NEQ 0 (
    echo Error: Required libraries missing. Please run: pip install -r requirements.txt
    exit /b 1
)

echo.
echo >> Generating All Publication Figures (300 DPI)...
python scripts\visualization\render_all_figures.py

echo.
echo >> Running Analytical Script Checks...
python scripts\analysis\calc_comparative_go_kegg_enrichment.py data\comparative_top_GO_BP.tsv

echo.
echo =====================================================================
echo   All outputs successfully generated! Check the figures\ folder.
echo =====================================================================
pause
