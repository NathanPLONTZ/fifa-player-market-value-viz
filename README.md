# Football Player Market Value: Data Visualisation

A static data visualisation study of the market value of professional football players, based on the FIFA player dataset (SoFIFA, 2018). The project looks at four possible drivers of market value: the birth month, the playing position, the nationality and the overall rating.

The work was done as a group project for a data visualisation course (TELECOM Nancy, Université de Lorraine, 2024/2025).

## Context and questions

Football players are valued on a transfer market, and it is not obvious which characteristics drive that value. This project explores the following questions:

1. **Birth month.** Do players born early in the year, who benefit from the *relative age effect* (RAE) during their training, have a higher market value once they are professionals?
2. **Position.** How does market value vary between goalkeepers, defenders, midfielders and attackers?
3. **Nationality.** How do the average market value and the number of players vary by country and by region?
4. **Overall rating.** How strongly is the in-game overall rating related to market value, and which attributes characterise the best-valued players of each position?

## Data

The dataset is `data/fifa_players.csv`.

- **Source:** player data extracted from [SoFIFA.com](https://sofifa.com) (2018).
- **Size:** 17,954 players, 51 variables.
- **Variables:** general information (name, birth date, age, nationality, positions), financial information (`value_euro`, `wage_euro`, `release_clause_euro`), physical and technical attributes (`acceleration`, `sprint_speed`, `dribbling`, `finishing`, `standing_tackle`, ...), and the overall rating and potential.

Columns that describe the national team (`national_team`, `national_rating`, `national_team_position`, `national_jersey_number`) are not used by the analysis.

## Repository structure

```
.
├── data/
│   └── fifa_players.csv            # Raw dataset
├── notebooks/
│   └── Notebook_Projet_VDD.ipynb   # Full analysis: preprocessing and visualisations
├── src/
│   └── plotting.py                 # Shared plotting helpers and colour palette
├── requirements.txt                # Python dependencies
├── .gitignore
└── README.md
```

The notebook writes its interactive Plotly outputs (`*.html`) next to itself when it runs. These files are generated, so they are not versioned.

## Getting started

Requirements: Python 3.9 or newer.

```bash
# 1. Clone the repository
git clone https://github.com/NathanPLONTZ/fifa-player-market-value-viz.git
cd fifa-player-market-value-viz

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Launch Jupyter from the notebooks/ folder, so that the relative paths resolve
cd notebooks
jupyter notebook Notebook_Projet_VDD.ipynb
```

The notebook loads the data with `../data/fifa_players.csv` and imports the helpers from `src/` with `sys.path.append("..")`, so it must be run with `notebooks/` as the working directory (the default when Jupyter is launched from that folder).

Interactive charts are saved as HTML files and opened in your default browser.

## Method

1. **Preprocessing.** Rows with missing `value_euro` or `wage_euro` are removed. Missing `release_clause_euro` values are filled with the median. The national-team columns and `height_cm` are dropped.
2. **Exploration.** Missing-value heatmap, correlation of every numeric variable with market value, and summary statistics.
3. **Nationality.** Choropleth maps of player counts and average market value per country, and a bubble chart of player count against average value per region.
4. **Position.** The first listed position of each player is mapped to one of four categories: defender (CB, RB, LB, RWB, LWB), midfielder (CM, CDM, CAM), attacker (ST, LW, RW, CF, RM, LM) and goalkeeper (GK). Wingers (LM, RM) are counted as attackers. Market values are compared with medians.
5. **Overall rating.** Scatter plot of overall rating against market value, with a Pearson correlation, and radar charts comparing the profiles of three well-known players.
6. **Birth month.** Player counts per month and per quarter, and market value distribution per birth month on a log scale.

## Results

The findings below come from the project report.

### Birth month and the relative age effect

- Players are unevenly distributed across the year. The number of professionals is highest in January and February and decreases towards December.
- By quarter, about **32.9 %** of players were born in January–March, against **19.3 %** in October–December.
- Market value distributions are very similar from one birth month to the next (median values in the same range, large overlap of the boxes). The relative age effect therefore seems to act mainly as a filter for entering professional football, rather than as a driver of market value once a player is professional.

### Position

| Category   | Number of players | Median market value |
|------------|------------------:|--------------------:|
| Attacker   | 5,358             | ≈ 880,000 €         |
| Midfielder | 4,516             | ≈ 800,000 €         |
| Defender   | 5,801             | ≈ 630,000 €         |
| Goalkeeper | 2,024             | ≈ 380,000 €         |

Attackers have the highest median value and goalkeepers the lowest. Using the median limits the influence of a few very expensive players.

### Nationality

- Countries with a long football tradition (France, United Kingdom, Germany, Brazil, Spain) stand out for both the number of players and their average value.
- Some countries with few players have high average values, which shows the influence of a small number of very valuable players.
- The total market value of a region depends both on how many players it has and on how many stars it has. Western Europe and Latin America have the largest totals, while some regions with fewer players still reach high totals.

### Overall rating

- Overall rating and market value are positively correlated, with a **Pearson coefficient of 0.63**.
- Among the numeric variables, `release_clause_euro` is the most correlated with market value, as expected since it is a contractual estimate of value. The project keeps the overall rating as the main indicator because it summarises sporting performance.
- The radar charts show the strengths behind the value of three of the best-valued players: finishing, dribbling and pace for Lionel Messi (attacker); vision, passing and stamina for Kevin De Bruyne (midfielder); defending, power and interceptions for Sergio Ramos (defender).

### Conclusion

Market value depends on several factors at once. Position and overall rating have a clear influence, nationality reflects the environment in which players are trained and visible, and the birth month matters for access to professional football but not for value once a player is professional.

## Source

Player data: [SoFIFA.com](https://sofifa.com) (2018).
