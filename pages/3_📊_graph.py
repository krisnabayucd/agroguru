import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set file path
file_path = os.path.join(os.getcwd(), 'data.csv')

# Read the data
data = pd.read_csv(file_path)

st.title("Explore Our Training Data")

# Add a sidebar
st.sidebar.title("Options")
show_all_data = st.sidebar.checkbox("Display Complete Dataset")

# Checkbox to show all data
if show_all_data:
    st.subheader("Complete Dataset")
    st.write(data)


# Text input for search
search_value = st.text_input("Search for a value", value="")

# Filtered data based on search value
filtered_data = data[data.astype(str).apply(lambda x: x.str.contains(search_value, case=False)).any(axis=1)]

# Display filtered data
if not filtered_data.empty:
    st.subheader("Filtered Data")
    st.write(filtered_data)
else:
    st.info("No matching data found.")

def plot_heatmap():
    # Exclude the 'label' column from the correlation matrix
    corr_matrix = data.drop('label', axis=1).corr()

    # Create a heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, ax=ax)

    # Set title
    ax.set_title('Correlation Heatmap (Excluding Label)', fontsize=14)

    # Display the plot using st.pyplot()
    st.pyplot(fig)

def plot_barplot(column):
    plt.figure(figsize=(19, 7))
    sns.barplot(x="label", y=column, data=data)
    plt.xticks(rotation=90)
    plt.title(f"{column} vs Crop Type")
    st.pyplot(plt.gcf())
    plt.close()

# Set a title for the app
st.subheader("Bar Plot")

# Select column for bar plot
selected_column = st.selectbox("Select a column for bar plot", data.columns[:-1])

# Display the selected bar plot
plot_barplot(selected_column)
    
# Set a title for the app
st.subheader("Correlation Heatmap")

# Display the heatmap
plot_heatmap()
