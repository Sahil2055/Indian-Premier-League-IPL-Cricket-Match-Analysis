# Indian Premier League (IPL) Cricket Match Analysis 🏏

### Project Description
This project analyzes ball-by-ball IPL match data to uncover patterns, strategies, and key performance indicators that lead to victory. The goal is to evaluate player and team impact, identify the statistical drivers of success, and build a foundation for predictive modeling of match outcomes based on the state of the game.

### Project By: **Sahil Kesharwani**

---

## 1. Problem Definition & Objectives

### Problem Statement
The Indian Premier League (IPL) is a professional Twenty20 cricket league in India, known for its explosive batting, strategic bowling, and thrilling finishes. While team composition and player form are crucial, several strategic factors and in-game events significantly influence the outcome of a match. This project aims to perform an in-depth analysis of ball-by-ball IPL match data to uncover the statistical drivers of success and identify key patterns that lead to victory.

The central question we seek to answer is: **"What are the most significant factors and strategies that contribute to winning an IPL match?"**

### Project Objectives
To address the problem statement, this analysis will focus on the following key objectives:

1.  **Impact of the Toss:** Determine if winning the toss and the subsequent decision (batting or fielding) provides a statistically significant advantage, considering different venues and seasons.
2.  **Powerplay Analysis:** Analyze team performance during the crucial first six "powerplay" overs. Identify teams that are most effective at scoring runs and minimizing wicket loss (batting), and teams that are best at taking wickets and restricting runs (bowling).
3.  **"Death Over" Specialist Bowlers:** Identify the most effective bowlers during the final "death overs" (overs 16-20) based on metrics like economy rate, wickets taken, and dot balls bowled.
4.  **Key Performance Indicators (KPIs) for Victory:** Investigate which match statistics (e.g., total score, wickets lost, run rate) are most strongly correlated with winning.
5.  **Player Impact Analysis:** Evaluate the performance of key batsmen and bowlers across different seasons to identify consistently high-impact players.
6.  **Predictive Modeling (Optional Extension):** Develop a simple predictive model to estimate the probability of a team winning based on the live state of the game (e.g., current score, wickets in hand, overs remaining).

---

## 2. Data Collection & Sources

The analysis is based on two comprehensive datasets obtained from a reliable public source (such as Kaggle or Cricsheet). These datasets provide detailed ball-by-ball information for every IPL match from the inaugural 2008 season to the most recent one.

### Datasets Used:
1.  **`matches.csv`**: This file contains match-level information. Each row corresponds to a single IPL match and includes details such as:
    * Season, date, and venue of the match.
    * Teams involved.
    * Toss winner and their decision.
    * Match winner and margin of victory.
    * Umpires and Player of the Match.

2.  **`deliveries.csv`**: This file contains ball-by-ball data for every match. Each row represents one ball bowled and includes details like:
    * The batting and bowling team.
    * The batsman, non-striker, and bowler.
    * Runs scored on that ball (batsman runs, extras).
    * Details of any wicket that fell, including the type of dismissal.

The granularity of the ball-by-ball data is the foundation of this project, allowing for deep and specific feature engineering and analysis that would not be possible with simple match summaries.

---

## 3. Insights & Interpretation

Based on the exploratory analysis and visualizations, we can draw several key strategic insights into the dynamics of the Indian Premier League.

### Insight 1: The Toss Decision is More Critical Than the Toss Itself
While the overall win percentage for the team that wins the toss is only slightly above 50%, a significant trend emerges in the *decision* made. Our analysis shows a strong preference (over 60%) for **electing to field first**. This strategic choice suggests that captains and team management believe chasing a target offers a distinct advantage. Potential reasons for this include:
* **Dew Factor:** In evening matches, dew can make the ball wet and difficult for bowlers to grip in the second innings.
* **Known Target:** The batting side knows the exact run rate required and can pace their innings accordingly.
* **Pressure on the Defending Team:** The pressure of setting a "good" score can lead to mistakes, while the chasing team has a clear, defined objective.
**Conclusion:** The real advantage isn't winning the coin flip, but in making the data-informed decision to chase, which has become the dominant strategy in the league.

### Insight 2: Sustained Dominance is Built on a Core of Key Players
The visualization of total team wins clearly identifies **Mumbai Indians** and **Chennai Super Kings** as the most successful franchises in IPL history. This is not accidental. A deeper look at the player-level data reveals that these teams have consistently featured players who top the charts for "Player of the Match" awards, runs scored, and wickets taken.
* **Impact Players:** The presence of consistent match-winners (like those in our Top 5 POTM chart) is a strong correlate of team success.
**Conclusion:** Long-term IPL success is not about having one good season. It is the result of building a team around a consistent core of high-impact, reliable performers. The data strongly supports a franchise strategy focused on retaining and acquiring these marquee players.

### Insight 3: The Currency of IPL is Specialization
Our analysis of the top run-scorers and wicket-takers highlights the immense value of specialist players.
* **Top Batsmen:** The leading run-scorers are predominantly top-order batsmen who have the skill to both build an innings and accelerate when needed.
* **Top Bowlers:** The most successful bowlers are specialists in their craft, whether it's powerplay swing bowling or "death over" yorkers.
**Conclusion:** While all-rounders are a valuable asset, the data shows that the most impactful roles in a T20 match are filled by specialists. For team auctions and strategy, identifying and securing the best specialist opener, finisher, and death bowler is a data-driven path to building a competitive advantage.

---

### Key Visualizations & Findings

**1. A Steady Rise in League Competition**
The number of matches per season has remained high, indicating the league's sustained popularity.

![Matches Per Season](../visualizations/1_matches_per_season.png)

**2. Mumbai Indians and Chennai Super Kings: The IPL Powerhouses**
These two teams have consistently dominated the league, as shown by their total number of wins.

![Total Wins by Team](../visualizations/2_total_wins_by_team.png)