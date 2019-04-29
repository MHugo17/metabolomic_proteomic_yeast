# metabolomic_proteomic_yeast
metabolism prediction - data form Zelezniak, A. et.al. Cell2018

MODEL TO PREDICT GLYCOLISIS AND PPP INTERMEDIATES USING QUANTITATIVE PROTEOMICS of yeast (Saccaromyces cerevisiae) strains

Proteomics data need to be quantified y processed accroding to the above cited paper and input data should have the structure as "example.csv"
in order to be runned through the notebook nr.3.

Output will be a new dataframe with predicted values of each metabolite (for each, specific features are selected and a specific model is applied)
and for each yeast strain. Martín Hugo, PhD
www.linkedin.com/in/martín-hugo-pereira

=======

## Setup

```sh
git clone https://github.com/MHugo17/metabolomic_proteomic_yeast.git
```

```sh
conda env create --file environment.yml
source activate prot-met
```

## Usage

```sh
conda env update --file environment.yml
source activate prot-met
jupyter notebook
>>>>>>> Stashed changes
