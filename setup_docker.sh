#!/bin/bash

# Update the system
echo "Updating system packages..."
sudo dnf update -y

# Install Docker dependencies
echo "Installing Docker dependencies..."
sudo dnf install -y docker

# Start Docker service
echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker

# Add current user to docker group to run docker without sudo
echo "Adding current user to docker group..."
sudo usermod -aG docker $USER

# Install Docker Compose
echo "Installing Docker Compose..."
sudo dnf install -y docker-compose-plugin

# Verify installations
echo "Verifying installations..."
docker --version
docker compose version

echo "Installation completed!"
echo "Please log out and log back in for group changes to take effect."
echo "You can then run your Docker containers without sudo."

# Build and run the Docker container
echo "To build and run the container, use these commands after logging back in:"
echo "docker build -t web-travel-embedding -f Dockerfile.prod ."
echo "docker run -d -p 80:8000 web-travel-embedding"