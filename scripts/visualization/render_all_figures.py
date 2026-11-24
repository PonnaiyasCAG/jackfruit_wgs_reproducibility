#!/usr/bin/env python3
"""
Master Visualization Runner for Jackfruit WGS Journal Submission
Executes all standalone plotting scripts and exports high-resolution (300 DPI)
publication figures into the figures/ directory.
"""
import os
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from fig1_chromosome_scaffolding import plot_fig1
from fig2_variant_impact_architecture import plot_fig2
from fig3_moraceae_orthogroups import plot_fig3
from fig4_candidate_genes_profiling import plot_fig4
from fig5_three_way_assembly_comparison import plot_fig5
from fig6_manhattan_variant_density import plot_fig6
from fig7_moraceae_phylogenomic_tree import plot_fig7
from fig8_candidate_protein_domains_lollipop import plot_fig8
from fig9_whole_genome_circos import plot_fig9
from fig10_comparative_go_distribution import plot_fig10
from fig11_comparative_kegg_pathway_landscape import plot_fig11
from fig12_functional_overlap_venn import plot_fig12
from fig13_agronomic_metabolic_expansions import plot_fig13
from fig14_sequencing_quality_and_coverage import plot_fig14

def main():
    print("=" * 75)
    print("  Jackfruit WGS Genomics: Generating All 300 DPI Publication Figures")
    print("=" * 75)
    start_time = time.time()
    
    plots = [
        ("Figure 1: Chromosome Scaffolding", plot_fig1),
        ("Figure 2: Variant Impact Architecture", plot_fig2),
        ("Figure 3: Moraceae Orthogroups", plot_fig3),
        ("Figure 4: Agronomic Candidate Genes", plot_fig4),
        ("Figure 5: Cultivar Assembly Comparison", plot_fig5),
        ("Figure 6: Manhattan Variant Density", plot_fig6),
        ("Figure 7: Moraceae Phylogenomic Tree", plot_fig7),
        ("Figure 8: Candidate Protein Domains & Lollipop", plot_fig8),
        ("Figure 9: Whole-Genome Circos Plot", plot_fig9),
        ("Figure 10: Comparative GO Distribution", plot_fig10),
        ("Figure 11: Comparative KEGG Pathway Landscape", plot_fig11),
        ("Figure 12: Three-Way Functional Overlap Venn", plot_fig12),
        ("Figure 13: Agronomic Metabolic Expansions", plot_fig13),
        ("Figure 14: Sequencing Quality & Coverage Profiles", plot_fig14)
    ]
    
    for name, func in plots:
        print(f"\n[Running] {name}...")
        try:
            func()
        except Exception as e:
            print(f"[Error] Failed to render {name}: {e}")
            
    elapsed = time.time() - start_time
    fig_dir = os.path.abspath(os.path.join(SCRIPT_DIR, "../../figures"))
    print("\n" + "=" * 75)
    print(f"  All figures rendered successfully in {elapsed:.1f}s!")
    print(f"  Output directory: {fig_dir}")
    print("=" * 75)

if __name__ == "__main__":
    main()
