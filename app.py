import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('baseball.csv')

# Select necessary columns and set the 'Team' column as the index
plot_data = data.set_index('Team')[['RS', 'RA']]

# Create a dropdown menu for year selection
selected_year = st.selectbox('Select Year', data['Year'].unique())

# Filter data based on selected year
filtered_data = data[data['Year'] == selected_year]

# Create a bar chart for Runs Scored
rs_chart_data = filtered_data.sort_values('RS', ascending=False)
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(rs_chart_data['Team'], rs_chart_data['RS'])
ax.set_title(f'Runs Scored by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Runs Scored')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)  # Pass the figure object directly


# Create a bar chart for Runs Allowed
ra_chart_data = filtered_data.sort_values('RA', ascending=False)
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(ra_chart_data['Team'], ra_chart_data['RA'], color='red')
ax.set_title(f'Runs Allowed by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Runs Allowed')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)  # Pass the figure object directly

# Create a bar chart for Runs Allowed
playoff_chart_data = filtered_data.sort_values('Playoffs')
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(ra_chart_data['Team'], ra_chart_data['RA'], color='red')
ax.set_title(f'Runs Allowed by Teams in {selected_year}')
ax.set_xlabel('Teams')
ax.set_ylabel('Runs Allowed')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)  # Pass the figure object directly










# # Create the stacked bar chart
# ax = plot_data.plot(kind='bar', stacked=True, figsize=(10, 7))

# # Labeling
# ax.set_ylabel('Runs')
# ax.set_title('Runs Scored and Runs Allowed per Team')

# plt.xticks(rotation=45)  # Rotates X-axis labels for better readability

# st.write(ax.figure)