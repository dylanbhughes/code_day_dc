# CodeDay DC - A Brief Introduction to Data Engineering

Hello! This repository was created as part of a presentation I made at CodeDay DC on 2022-11-19. [Here's a link to that presentation.](https://docs.google.com/presentation/d/1OFrxebSzCHCUyb6z2YzUIcurBLNgOFhF1imv02iJ6UE/edit?usp=sharing)

The other parts of this repository include the notebook that I used to demonstrate the different parts of a data pipeline (`get_data_and_plot.ipynb`), a version of the pipeline working just on my laptop (`fetch_parking_tickets.py`), and a version of the pipeline working with Prefect (`fetch_parking_tickets_with_prefect.py`).

If you have any questions or would just like to connect, feel free to reach me on [LinkedIn](https://www.linkedin.com/in/dylanbhughes).

## Environment Setup

### Conda

For OSX, use [Homebrew](https://brew.sh/)'s distribution of [Miniconda](https://docs.conda.io/en/latest/miniconda.html):

```bash
brew install miniconda
```

### Installing & Activating This Environment

```bash
conda env create -f environment.yml
conda activate code_day_dc
```
