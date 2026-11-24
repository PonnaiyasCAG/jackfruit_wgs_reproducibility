#!/usr/bin/env python3
"""
Parse OrthoFinder Orthogroups
Identifies universal core single-copy orthologues, shared clades,
and species-specific gene family expansions from Orthogroups.GeneCount.tsv or Statistics_PerSpecies.tsv.
"""
import os
import sys
import argparse
import pandas as pd

def parse_orthogroups(file_path):
    df = pd.read_csv(file_path, sep="\t")
    
    # If this is Statistics_PerSpecies.tsv
    if 'Statistics' in os.path.basename(file_path) or df.columns[0].lower() in ['unnamed: 0', '', 'statistic']:
        print(">> Reading OrthoFinder Per-Species Summary Statistics:")
        print(df.to_string(index=False))
        return None
        
    # Taxa columns (exclude Orthogroup and Total)
    taxa_cols = [c for c in df.columns if c not in ['Orthogroup', 'Total']]
    for c in taxa_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0).astype(int)
        
    total_ogs = len(df)
    core_ogs = df[(df[taxa_cols] > 0).all(axis=1)]
    single_copy_core = df[(df[taxa_cols] == 1).all(axis=1)]
    
    # Species-specific
    species_specific = {}
    for col in taxa_cols:
        other_cols = [c for c in taxa_cols if c != col]
        spec_df = df[(df[col] > 0) & (df[other_cols] == 0).all(axis=1)]
        species_specific[col] = len(spec_df)
        
    return {
        "taxa": taxa_cols,
        "total_orthogroups": total_ogs,
        "core_shared_orthogroups": len(core_ogs),
        "single_copy_core_orthogroups": len(single_copy_core),
        "species_specific_orthogroups": species_specific
    }

def main():
    parser = argparse.ArgumentParser(description="Parse OrthoFinder Gene Count Statistics")
    parser.add_argument("tsv_file", help="Path to Orthogroups.GeneCount.tsv or Statistics_PerSpecies.tsv")
    args = parser.parse_args()
    
    if not os.path.exists(args.tsv_file):
        print(f"Error: File '{args.tsv_file}' not found.")
        sys.exit(1)
        
    res = parse_orthogroups(args.tsv_file)
    if res is not None:
        print("=" * 65)
        print("  OrthoFinder Phylogenomics & Gene Family Summary")
        print("=" * 65)
        print(f"  Analyzed Taxa ({len(res['taxa'])}) : {', '.join(res['taxa'])}")
        print(f"  Total Inferred Orthogroups        : {res['total_orthogroups']:,}")
        print(f"  Universal Core Orthogroups        : {res['core_shared_orthogroups']:,} ({(res['core_shared_orthogroups']/res['total_orthogroups'])*100:.1f}%)")
        print(f"  Single-Copy Universal Orthologs   : {res['single_copy_core_orthogroups']:,}")
        print("\n  Lineage-Specific Gene Families:")
        for sp, cnt in res['species_specific_orthogroups'].items():
            print(f"    - {sp:<30}: {cnt:,} orthogroups")
        print("=" * 65)

if __name__ == "__main__":
    main()
