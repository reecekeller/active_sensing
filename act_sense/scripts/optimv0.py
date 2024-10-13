start_x, start_y = 30, 0
end_x, end_y = 0, 49
max_steps = 100  # Example maximum number of steps

rows, cols = data.shape
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Initialize DP table and parent table
dp = np.full((rows, cols, max_steps + 1), -np.inf)
parent = np.full((rows, cols, max_steps + 1, 2), -1)

# Weights for information score, path length, and acceleration
weight_info = 1.0
weight_distance = 1.0
weight_acceleration = 1.0

# Starting point
dp[start_x, start_y, 0] = data[start_x, start_y]

# Fill DP table
for k in tqdm(range(1, max_steps + 1)):
    for x in range(rows):
        for y in range(cols):
            if dp[x, y, k - 1] != -np.inf:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        new_score = dp[x, y, k - 1] + data[nx, ny]
                        if new_score > dp[nx, ny, k]:
                            dp[nx, ny, k] = new_score
                            parent[nx, ny, k] = [x, y]


# Find the maximum score at the end position
max_score = -np.inf
best_k = -1
for k in range(max_steps + 1):
    if dp[end_x, end_y, k] > max_score:
        max_score = dp[end_x, end_y, k]
        best_k = k

# Reconstruct the path
if max_score == -np.inf:
    path = []

path = []
x, y, k = end_x, end_y, best_k
while k >= 0:
    path.append((x, y))
    x, y = parent[x, y, k]
    k -= 1
path.reverse()


# Example usage
print(path)


# Plot the data matrix
plt.imshow(data)

# Plot the path
path_x = [point[1] for point in path]
path_y = [point[0] for point in path]
plt.plot(path_x, path_y, 'r.')

# Set the axis labels
plt.xlabel('Column')
plt.ylabel('Row')

# Show the plot
plt.show()