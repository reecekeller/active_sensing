import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
def find_path(data, start_x, start_y, end_x, end_y, max_steps, max_jump, weight_info, weight_acceleration, weight_steps):
    # Initialize DP table and parent table
    rows, cols = data.shape
    dp = np.full((rows, cols, max_steps + 1), -np.inf)
    parent = np.full((rows, cols, max_steps + 1, 2), -1)

    # Starting point
    dp[start_x, start_y, 0] = data[start_x, start_y]

    # Fill DP table
    for k in tqdm(range(1, max_steps + 1)):
        for x in range(rows):
            for y in range(cols):
                if dp[x, y, k - 1] != -np.inf:  # Only process reachable points
                    for jump in range(1, max_jump + 1):  # Allow jumps from 1 to max_jump
                        for dx in range(-jump, jump + 1):
                            dy = jump - abs(dx)  # Remaining distance to cover
                            # Create a list of possible movements
                            possible_moves = [(dx, dy), (dx, -dy), (-dx, dy), (-dx, -dy)]

                            for dx, dy in possible_moves:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < rows and 0 <= ny < cols:
                                    # Calculate new score
                                    information_gain = weight_info * data[nx, ny]

                                    # Calculate distance moved and velocity
                                    distance_moved = np.sqrt(dx**2 + dy**2)
                                    acceleration_penalty = weight_acceleration * (distance_moved - 1) ** 2  # Penalizing acceleration

                                    # Penalize for taking steps
                                    step_penalty = weight_steps * k

                                    # Combine scores
                                    new_score = dp[x, y, k - 1] + information_gain - acceleration_penalty - step_penalty

                                    # Update DP table if the new score is better
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
    path = []
    if max_score != -np.inf:  # Only reconstruct if a valid path was found
        x, y, k = end_x, end_y, best_k
        while k >= 0:
            path.append((x, y))
            x, y = parent[x, y, k]
            k -= 1
        path.reverse()

    return path


def plot_path(data, path):
    # Plot the path if it exists
    if path:
        path_x = [point[1] for point in path]
        path_y = [point[0] for point in path]
        # Calculate speed at every point
        speeds = []
        total_distance = len(path) - 1
        for i in range(len(path)):
            if i == 0:
                speed = 0
            else:
                distance = np.sqrt((path[i][0] - path[i-1][0])**2 + (path[i][1] - path[i-1][1])**2)
                speed = distance / total_distance
            speeds.append(speed)

    # Create a subplot with 1 row and 2 columns
    fig, axs = plt.subplots(1, 2)

    # Plot the data matrix with path overlay
    axs[0].imshow(data)
    if path:
        path_x = [point[1] for point in path]
        path_y = [point[0] for point in path]
        axs[0].plot(path_x, path_y, 'r.')

    # Set the size of the subplots
    fig.set_size_inches(12, 6)

    # Set the axis labels for the first plot
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')

    # Plot speed as a function of progress
    progress = np.linspace(0, 1, len(speeds))
    axs[1].plot(progress, speeds, 'b--')
    smoothed_speeds = np.convolve(speeds, np.ones(10)/10, mode='valid')
    smoothed_progress = np.linspace(0, 1, len(smoothed_speeds))
    axs[1].plot(smoothed_progress, smoothed_speeds, 'r-')
    # Set the axis labels for the second plot
    axs[1].set_xlabel('Trial Progress')
    axs[1].set_ylabel('Speed')

