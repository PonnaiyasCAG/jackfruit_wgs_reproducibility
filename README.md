# Reproducibility Code Archive: Whole Genome Sequencing and Comparative Genomics of Jackfruit (*Artocarpus heterophyllus* Lam. Cultivar PLJS)

This repository contains the analysis scripts, curated summary datasets, and high-resolution visualization code to reproduce all computational findings, statistical metrics, and publication figures for the manuscript:

> **Whole Genome Sequencing, Chromosome-Level Assembly, Three-Way Cultivar Comparison, and Comparative Genomics of a Local Jackfruit (*Artocarpus heterophyllus* Lam.) Cultivar PLJS Reveal Candidate Genes for Agronomic Traits and Moraceae Phylogenomic Architecture**  
> *[Author List]*, and Prof. Manivannan*  
> \* *Corresponding Author: Prof. Manivannan*

---

## 1. Data Availability Statement

- **Raw Sequencing Reads**: The raw paired-end Illumina genomic reads (150 bp, ~55 Gb, ~60× physical coverage) generated in this study have been deposited in the NCBI Sequence Read Archive (SRA) under BioProject accession `PRJNAXXXXXX` (BioSample: `SAMNXXXXXX`, SRA Runs: `SRRXXXXXX`).
- **Genome Assembly**: The de novo assembled contigs and the 28 chromosome-scale pseudomolecules anchored via RagTag have been deposited in NCBI GenBank under accession `GCA_XXXXXX`.
- **Public Comparative References**:
  - *Artocarpus heterophyllus* Chinese cultivar S10 (chromosome-level reference): NCBI accession [`GCA_025403435.1`](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_025403435.1/)
  - *Artocarpus heterophyllus* Bangladesh cultivar BSMRAU-JF-1 (scaffold-level reference): NCBI accession [`GCA_020010975.1`](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_020010975.1/)
  - *Morus alba* (White Mulberry, Moraceae sister lineage): NCBI accession [`GCF_000414095.1`](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000414095.1/)
  - *Ficus carica* (Common Fig, Moraceae outgroup): NCBI accession [`GCA_001014895.1`](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_001014895.1/)

---

## 2. Repository Structure

```text
jackfruit_wgs_reproducibility/
├── README.md                          # Repository documentation and reproduction manual
├── requirements.txt                   # Standard Python dependencies
├── run_all.sh                         # Linux / macOS master execution script
├── run_all.bat                        # Windows master execution script
├── data/                              # Curated summary and comparative tables
│   ├── assembly_scaffolding_metrics.tsv
│   ├── candidate_genes_circos_data.json
│   ├── candidate_genes_summary.tsv
│   ├── comparative_agronomic_KEGG_pathways.tsv
│   ├── comparative_top_GO_BP.tsv
│   ├── comparative_top_GO_CC.tsv
│   ├── comparative_top_GO_MF.tsv
│   ├── comparative_top_KEGG_pathways.tsv
│   ├── moraceae_mapping_rates.tsv
│   ├── SpeciesTree_rooted.txt
│   ├── Statistics_PerSpecies.tsv
│   ├── three_jack_functional_overview.tsv
│   ├── three_jack_overlap_statistics.tsv
│   ├── three_way_standardized_cultivar_comparison.tsv
│   └── variant_impact_summary.tsv
├── figures/                           # Generated 300 DPI publication-ready figures
└── scripts/
    ├── visualization/                 # Standalone publication figure generators
    │   ├── fig1_chromosome_scaffolding.py
    │   ├── fig2_variant_impact_architecture.py
    │   ├── fig3_moraceae_orthogroups.py
    │   ├── fig4_candidate_genes_profiling.py
    │   ├── fig5_three_way_assembly_comparison.py
    │   ├── fig6_manhattan_variant_density.py
    │   ├── fig7_moraceae_phylogenomic_tree.py
    │   ├── fig8_candidate_protein_domains_lollipop.py
    │   ├── fig9_whole_genome_circos.py
    │   ├── fig10_comparative_go_distribution.py
    │   ├── fig11_comparative_kegg_pathway_landscape.py
    │   ├── fig12_functional_overlap_venn.py
    │   ├── fig13_agronomic_metabolic_expansions.py
    │   ├── fig14_sequencing_quality_and_coverage.py
    │   └── render_all_figures.py      # Master visualization runner
    └── analysis/                      # Data processing & statistical validation scripts
        ├── calc_assembly_scaffolding_stats.py
        ├── calc_variant_statistics.py
        ├── calc_comparative_go_kegg_enrichment.py
        └── parse_orthofinder_families.py
```

---

## 3. Quick Start & Environment Setup

This repository is designed to be completely standalone. All data needed to reproduce the manuscript's figures and comparative statistics are pre-packaged in the `data/` directory.

### Prerequisites
- Python 3.9+ with standard scientific libraries:
```bash
pip install -r requirements.txt
```

### Reproduce All 14 Figures in One Step
```bash
# Linux / macOS / WSL
bash run_all.sh

# Windows
run_all.bat
```
All figures are exported at **300 DPI** directly into the `figures/` directory.

---

## 4. Manuscript Figures Catalog

Each figure can be reproduced individually using its dedicated Python script:

| Figure | Script | Description |
| :--- | :--- | :--- |
| **Figure 1** | `scripts/visualization/fig1_chromosome_scaffolding.py` | Chromosome-scale scaffolding metrics of Indian PLJS anchored into 28 pseudochromosomes vs. Chinese S10 reference. |
| **Figure 2** | `scripts/visualization/fig2_variant_impact_architecture.py` | SnpEff functional impact tiers (High LoF, Moderate Missense, Low Synonymous, Modifier) across 17.77M variants. |
| **Figure 3** | `scripts/visualization/fig3_moraceae_orthogroups.py` | OrthoFinder gene family assignment and Moraceae core vs. species-specific orthogroup hierarchy. |
| **Figure 4** | `scripts/visualization/fig4_candidate_genes_profiling.py` | Agronomic candidate gene families (sweetness, aroma, softening, flavonoids) and coding polymorphism ratios. |
| **Figure 5** | `scripts/visualization/fig5_three_way_assembly_comparison.py` | Three-way assembly contiguity comparison (PLJS vs. S10 vs. BSMRAU-JF-1) and cross-species mapping decay. |
| **Figure 6** | `scripts/visualization/fig6_manhattan_variant_density.py` | Genome-wide Manhattan variant density landscape across 28 pseudochromosomes showing hyper-polymorphic hotspots. |
| **Figure 7** | `scripts/visualization/fig7_moraceae_phylogenomic_tree.py` | Inferred Moraceae phylogenomic species tree (5,590 single-copy orthologues) with divergence times and Asian jackfruit clade. |
| **Figure 8** | `scripts/visualization/fig8_candidate_protein_domains_lollipop.py` | Functional domain architectures and missense mutation lollipop maps for key agronomic genes (SPS, TPS, CHS2, FUS3). |
| **Figure 9** | `scripts/visualization/fig9_whole_genome_circos.py` | Circular whole-genome visualization displaying 28 chromosomes, variant density waves, and candidate gene physical loci. |
| **Figure 10** | `scripts/visualization/fig10_comparative_go_distribution.py` | Three-way comparative Gene Ontology distribution across Biological Process, Molecular Function, and Cellular Component. |
| **Figure 11** | `scripts/visualization/fig11_comparative_kegg_pathway_landscape.py` | Top conserved and differential KEGG biological pathways across Indian, Chinese, and Bangladesh cultivars. |
| **Figure 12** | `scripts/visualization/fig12_functional_overlap_venn.py` | Three-way Euler/Venn diagram of core conserved (85.9% GO, 98.0% KEGG) vs. cultivar-specific functional terms. |
| **Figure 13** | `scripts/visualization/fig13_agronomic_metabolic_expansions.py` | Significant gene copy number expansions in key agronomic pathways (Starch/Sucrose, Fructose/Mannose, Flavonoids). |
| **Figure 14** | `scripts/visualization/fig14_sequencing_quality_and_coverage.py` | Per-base Phred sequencing quality progression (Q30+) and physical depth of coverage distribution (31.2× mean). |

---

## 5. Analytical Scripts Usage

These scripts can be used by reviewers and researchers to compute metrics directly from raw FASTA, VCF, or tabular outputs:

### 1. Calculate Assembly Contiguity Metrics
```bash
python scripts/analysis/calc_assembly_scaffolding_stats.py <assembly.fasta>
```
Outputs total contig count, total length (Mb), N50, L50, GC content, and sequence size distribution.

### 2. Summarize Variant Impacts & Ti/Tv Ratio
```bash
python scripts/analysis/calc_variant_statistics.py <variants.vcf[.gz]>
```
Parses VCF headers and records to calculate transition/transversion (Ti/Tv) ratios, SNP/InDel counts, and SnpEff impact distributions.

### 3. Compute Comparative Functional Enrichment
```bash
python scripts/analysis/calc_comparative_go_kegg_enrichment.py data/comparative_top_GO_BP.tsv --output_tsv results_annotated.tsv
```
Calculates cultivar representation ratios and Fisher's exact tests for functional term expansions.

### 4. Parse OrthoFinder Gene Family Dynamics
```bash
python scripts/analysis/parse_orthofinder_families.py data/Statistics_PerSpecies.tsv
```
Summarizes universal core single-copy orthologues, shared clades, and lineage-specific orphan gene families.

---

## 6. Citation

If you use this code or data, please cite:

```bibtex
@article citation details
```
