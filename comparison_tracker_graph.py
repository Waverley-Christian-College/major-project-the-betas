# Sample data
x = [1, 2, 3, 4, 5]
y = [5, 3, 7, 4, 8]

# Set Seaborn style
plt.figure(figsize=(8, 6))

# Solid line with circle markers
sns.lineplot(x=x, y=y, linestyle='-', marker='o', markersize=8, label='Solid Line', color='blue') 

# Dashed line with square markers
sns.lineplot(x=x, y=[i + 1 for i in y], linestyle='--', marker='s', markersize=8, label='Dashed Line', color='green') 

# Dash-dot line with triangle up markers
sns.lineplot(x=x, y=[i + 2 for i in y], linestyle='-.', marker='^', markersize=20, label='Dash-dot Line', color='purple') 

# Dotted line with asterisk markers
sns.lineplot(x=x, y=[i + 3 for i in y], linestyle=':', marker='*', markersize=15, label='Dotted Line', color='orange') 

plt.title('Customized Line and Scatter Plot with Seaborn') # Add a title
plt.xlabel('X-axis') # x-axis name
plt.ylabel('Y-axis') # x-axis name
plt.legend(loc='upper left') # Add a legend
plt.show() # Display the graph