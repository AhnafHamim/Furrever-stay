import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('baseball.csv')

# Dropdown menu
selected_year = st.selectbox('Select Year', data['Year'].unique())

# Filter with year
filtered_data = data[data['Year'] == selected_year]

# Runs Scored
rs_chart_data = filtered_data[['Team', 'RS']]
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(rs_chart_data['Team'], rs_chart_data['RS'])
ax.set_title(f'Runs Scored by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Runs Scored')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
print_text_one = """
Offensive Indicator: RS is a direct measure of a team's offensive capability. A higher number of runs scored indicates a strong offensive team. By tracking and comparing RS across teams or over time, one can gauge the offensive strength and efficiency of different teams.

Winning Probability: Typically, teams that score more runs have a higher likelihood of winning games. Analyzing RS can provide insights into a team’s winning potential.
"""
st.markdown(print_text_one)

# Runs Allowed
ra_chart_data = filtered_data[['Team', 'RA']]
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(ra_chart_data['Team'], ra_chart_data['RA'], color='red')
ax.set_title(f'Runs Allowed by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Runs Allowed')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

print_text_two = """
Defensive Indicator: RA reflects the effectiveness of a team's defense and pitching staff. A lower number of runs allowed suggests a strong defensive team. Comparing RA across teams or over time can help evaluate the defensive prowess of teams.

Team Improvement: By analyzing the RA metric, teams can identify areas of improvement in their defense to decrease the number of runs allowed, which in turn could lead to more wins.
"""
st.markdown(print_text_two)

# Playoffs
playoff_chart_data = filtered_data[['Team', 'Playoffs']]
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(playoff_chart_data['Team'], playoff_chart_data['Playoffs'], color='green')
ax.set_title(f'Made It To The Playoffs by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Playoffs')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
print_text_three = """
Importance: Making it to the playoffs is a significant achievement, indicating that a team performed well during the regular season and is among the top contenders for the championship.
Use: The playoff indicator provides a binary outcome, allowing for a clear distinction between successful and non-successful seasons.
"""
st.markdown(print_text_three)