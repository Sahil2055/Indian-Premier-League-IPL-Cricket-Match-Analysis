# Indian Premier League (IPL) Cricket Match Analysis 🏏

### Project Description
This project conducts a comprehensive analysis of ball-by-ball IPL match data from 2008 to 2024. The primary goal is to uncover the statistical patterns, player impacts, and strategic decisions that are most influential in determining match outcomes. By leveraging data visualization and statistical analysis, we aim to derive actionable insights that could be valuable for team strategists and cricket enthusiasts.

---

### Problem Statement
What are the key statistical drivers of success in the Indian Premier League? This analysis seeks to move beyond surface-level statistics to identify which factors (like winning the toss, performance in key match phases, or specific player matchups) have the strongest correlation with winning matches.

### Objectives
1.  **Toss Analysis:** To determine the impact of winning the toss on match outcomes across different venues and seasons.
2.  **Performance in Phases:** To evaluate team and player performance during critical phases of the game, specifically the **Powerplay** (overs 1-6) and **Death Overs** (overs 16-20).
3.  **Player Profiling:** To identify the most valuable batsmen and bowlers based on their performance under various conditions (e.g., chasing a target, bowling in the death overs).
4.  **Venue Analysis:** To uncover how different stadiums influence match dynamics, such as scoring patterns and toss advantages.
5.  **Strategic Insights:** To synthesize the findings into data-driven recommendations that could inform team strategies, auction selections, and on-field tactics.

---

### Data Sources
The analysis is based on two primary datasets, which are publicly available and commonly used for IPL analysis. The data covers matches from the inaugural 2008 season up to the 2024 season.

1.  **`matches.csv`**: This file contains match-level information. Each row represents a single match and includes details such as:
    * Match ID, season, date, and venue.
    * The two competing teams.
    * Toss winner and their decision (to bat or field).
    * The winner of the match and the margin of victory.
    * Player of the match and the umpires.

2.  **`deliveries.csv`**: This file contains ball-by-ball data for every match. Each row represents one ball bowled and includes details like:
    * Match ID to link with the `matches.csv` file.
    * Inning, over, and ball number.
    * The batting and bowling teams.
    * The batsman on strike, the non-striker, and the bowler.
    * Runs scored, extras, and total runs on that delivery.
    * Details of any wicket that fell, including the player dismissed and the type of dismissal.