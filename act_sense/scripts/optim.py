import torch
import torch.optim as optim

# Initialize position trajectory (T steps of 2D positions)
T = 100  # number of steps
trajectory = torch.randn(T, 2, requires_grad=True)  # (T, 2) -> (x_t, y_t)

# Example values for target, information, and lambda weights
x_f = 0
y_f = 30
p_f = torch.tensor([x_f, y_f])  # final target
information_grid = torch.randn(T, 2)  # hypothetical information values
lambda_1 = 1.0
lambda_2 = 1.0
lambda_3 = 1.0

optimizer = optim.Adam([trajectory], lr=0.01)

for epoch in range(100000):
    # Compute the distance term
    distance = torch.norm(trajectory - p_f, dim=1).sum()

    # Compute the acceleration term
    acceleration = trajectory[2:] - 2 * trajectory[1:-1] + trajectory[:-2]
    energy = torch.norm(acceleration, dim=1).sum()

    # Compute the information term (negative to maximize)
    information = information_grid.sum()

    # Cost function
    cost = lambda_1 * distance + lambda_2 * energy - lambda_3 * information

    # Gradient descent
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    print(f'Epoch {epoch}, Cost: {cost.item()}')