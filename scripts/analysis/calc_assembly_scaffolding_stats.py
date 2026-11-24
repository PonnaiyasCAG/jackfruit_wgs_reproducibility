#!/usr/bin/env python3
"""
Calculate Assembly and Scaffolding Metrics
Computes assembly statistics (Total Length, Contig/Scaffold Count, N50, L50, GC%)
from FASTA sequences.
"""
import os
import sys
import argparse

def compute_fasta_stats(fasta_path):
    lengths = []
    gc_count = 0
    total_bases = 0
    
    current_len = 0
    with open(fasta_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_len > 0:
                    lengths.append(current_len)
                    current_len = 0
            else:
                current_len += len(line)
                line_upper = line.upper()
                gc_count += line_upper.count('G') + line_upper.count('C')
                total_bases += len(line)
        if current_len > 0:
            lengths.append(current_len)
            
    if not lengths:
        return None
        
    lengths.sort(reverse=True)
    total_len = sum(lengths)
    n_seqs = len(lengths)
    gc_pct = (gc_count / total_bases) * 100 if total_bases > 0 else 0
    
    # N50 / L50
    half_len = total_len / 2.0
    cum_len = 0
    n50 = 0
    l50 = 0
    for idx, l in enumerate(lengths):
        cum_len += l
        if cum_len >= half_len:
            n50 = l
            l50 = idx + 1
            break
            
    return {
        "num_sequences": n_seqs,
        "total_length_bp": total_len,
        "total_length_mb": total_len / 1e6,
        "n50_bp": n50,
        "n50_kb": n50 / 1e3,
        "l50": l50,
        "gc_percent": gc_pct,
        "max_length_bp": lengths[0],
        "min_length_bp": lengths[-1]
    }

def main():
    parser = argparse.ArgumentParser(description="Calculate Assembly and Scaffolding Contiguity Metrics")
    parser.add_argument("fasta", help="Path to assembly FASTA file")
    args = parser.parse_args()
    
    if not os.path.exists(args.fasta):
        print(f"Error: File '{args.fasta}' not found.")
        sys.exit(1)
        
    stats = compute_fasta_stats(args.fasta)
    print("=" * 60)
    print(f"  Assembly Contiguity Metrics: {os.path.basename(args.fasta)}")
    print("=" * 60)
    for k, v in stats.items():
        if isinstance(v, float):
            print(f"  {k:<25}: {v:,.2f}")
        elif isinstance(v, int):
            print(f"  {k:<25}: {v:,}")
        else:
            print(f"  {k:<25}: {v}")
    print("=" * 60)

if __name__ == "__main__":
    main()
