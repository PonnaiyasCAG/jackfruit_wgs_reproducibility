#!/usr/bin/env python3
"""
Calculate Comparative Functional Enrichment (GO & KEGG)
Performs comparative statistical calculations, ratios, and Fisher exact tests
for Gene Ontology terms and KEGG biological pathways across cultivars.
"""
import os
import sys
import argparse
import pandas as pd
import numpy as np
from scipy.stats import fisher_exact

def analyze_go_enrichment(input_tsv):
    df = pd.read_csv(input_tsv, sep="\t")
    required = ['GO_ID', 'GO_Name', 'Indian_PLJS_Genes', 'Chinese_S10_Genes', 'BSMRAU_JF1_Genes']
    for r in required:
        if r not in df.columns:
            raise ValueError(f"Missing required column: {r}")
            
    df['Ratio_PLJS_to_S10'] = (df['Indian_PLJS_Genes'] + 1) / (df['Chinese_S10_Genes'] + 1)
    df['Ratio_PLJS_to_BSMRAU'] = (df['Indian_PLJS_Genes'] + 1) / (df['BSMRAU_JF1_Genes'] + 1)
    
    # Calculate Fisher p-values for PLJS expansion
    total_pljs = df['Indian_PLJS_Genes'].sum()
    total_s10 = df['Chinese_S10_Genes'].sum()
    
    p_vals = []
    for _, row in df.iterrows():
        a = row['Indian_PLJS_Genes']
        b = total_pljs - a
        c = row['Chinese_S10_Genes']
        d = total_s10 - c
        table = [[a, b], [c, d]]
        odds, p = fisher_exact(table, alternative='two-sided')
        p_vals.append(p)
        
    df['Fisher_P_Value'] = p_vals
    return df

def main():
    parser = argparse.ArgumentParser(description="Calculate Comparative Functional Enrichment")
    parser.add_argument("input_tsv", help="Path to comparative functional TSV file")
    parser.add_argument("--output_tsv", help="Path to save annotated results TSV", default=None)
    args = parser.parse_args()
    
    if not os.path.exists(args.input_tsv):
        print(f"Error: File '{args.input_tsv}' not found.")
        sys.exit(1)
        
    df_res = analyze_go_enrichment(args.input_tsv)
    print("=" * 70)
    print(f"  Comparative Functional Profiling: {os.path.basename(args.input_tsv)}")
    print("=" * 70)
    print(df_res[['GO_Name', 'Indian_PLJS_Genes', 'Chinese_S10_Genes', 'Ratio_PLJS_to_S10', 'Fisher_P_Value']].head(10).to_string(index=False))
    print("=" * 70)
    
    if args.output_tsv:
        df_res.to_csv(args.output_tsv, sep="\t", index=False)
        print(f"Annotated results saved to: {args.output_tsv}")

if __name__ == "__main__":
    main()
