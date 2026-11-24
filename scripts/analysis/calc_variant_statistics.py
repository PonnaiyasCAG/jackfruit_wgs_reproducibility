#!/usr/bin/env python3
"""
Calculate Variant Statistics and Functional Impacts
Parses VCF files (or SnpEff-annotated VCF) to compute Transition/Transversion (Ti/Tv)
ratios, SNP vs. InDel proportions, and functional impact distributions.
"""
import os
import sys
import gzip
import argparse
from collections import defaultdict

def parse_vcf(vcf_path):
    is_gz = vcf_path.endswith('.gz')
    opener = gzip.open if is_gz else open
    mode = 'rt' if is_gz else 'r'
    
    total_vars = 0
    snps = 0
    indels = 0
    transitions = 0
    transversions = 0
    
    impacts = defaultdict(int)
    
    with opener(vcf_path, mode) as f:
        for line in f:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 5:
                continue
            total_vars += 1
            ref = fields[3].upper()
            alt_list = fields[4].upper().split(',')
            
            for alt in alt_list:
                if len(ref) == 1 and len(alt) == 1:
                    snps += 1
                    pair = f"{ref}>{alt}"
                    if pair in ['A>G', 'G>A', 'C>T', 'T>C']:
                        transitions += 1
                    else:
                        transversions += 1
                else:
                    indels += 1
                    
            # Parse SnpEff ANN field if present
            if len(fields) > 7 and 'ANN=' in fields[7]:
                info = fields[7]
                ann_part = [x for x in info.split(';') if x.startswith('ANN=')]
                if ann_part:
                    ann_str = ann_part[0][4:]
                    first_eff = ann_str.split(',')[0].split('|')
                    if len(first_eff) > 2:
                        impact = first_eff[2]
                        impacts[impact] += 1
                        
    titv = transitions / transversions if transversions > 0 else 0.0
    return {
        "total_variants": total_vars,
        "snps": snps,
        "indels": indels,
        "transitions": transitions,
        "transversions": transversions,
        "titv_ratio": titv,
        "impact_distribution": dict(impacts)
    }

def main():
    parser = argparse.ArgumentParser(description="Calculate Variant Statistics from VCF")
    parser.add_argument("vcf", help="Path to VCF file (plain or .gz)")
    args = parser.parse_args()
    
    if not os.path.exists(args.vcf):
        print(f"Error: File '{args.vcf}' not found.")
        sys.exit(1)
        
    print(f"Parsing VCF: {args.vcf}...")
    stats = parse_vcf(args.vcf)
    print("=" * 60)
    print("  Variant Summary Statistics")
    print("=" * 60)
    print(f"  Total Evaluated Variants : {stats['total_variants']:,}")
    print(f"  Single Nucleotide (SNPs) : {stats['snps']:,} ({(stats['snps']/max(1,stats['total_variants']))*100:.2f}%)")
    print(f"  Insertions/Deletions     : {stats['indels']:,} ({(stats['indels']/max(1,stats['total_variants']))*100:.2f}%)")
    print(f"  Transitions (Ti)         : {stats['transitions']:,}")
    print(f"  Transversions (Tv)       : {stats['transversions']:,}")
    print(f"  Ti/Tv Ratio              : {stats['titv_ratio']:.2f}")
    if stats['impact_distribution']:
        print("\n  SnpEff Impact Categories:")
        for imp, cnt in stats['impact_distribution'].items():
            print(f"    - {imp:<12}: {cnt:,} ({(cnt/stats['total_variants'])*100:.2f}%)")
    print("=" * 60)

if __name__ == "__main__":
    main()
