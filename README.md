# Basic Authentication Project for class Bravo Members

## Getting Started

Follow these instructions to set up and contribute to the project.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <https://github.com/michaelovo/BravoAuth.git>
cd <BravoAuth>
```

### 2. Branch Structure
This repository has two main branches:
- `main` - Production branch
- `staging` - Development branch

### 3. Switch to Staging Branch
```bash
git checkout staging
```

### 4. Create Your Feature Branch
Create a new branch from `staging` for your task:
```bash
git checkout -b <your-branch-name>
```

## Project Structure

The project contains two core files:

- **`Authentication.py`** - Main program file
- **`AuthenticationValidators.py`** - Task functions and validators

## Development Workflow

### Working on Your Task
1. Implement your task functions in `AuthenticationValidators.py`
2. Use `Authentication.py` for your main program logic
3. Test your changes thoroughly

### Committing Changes
```bash
git add .
git commit -m "Your descriptive commit message"
```

### Pushing to GitHub
```bash
git push origin <your-branch-name>
```

### Creating a Pull Request
1. Navigate to the repository on GitHub
2. Click on "Pull Requests"
3. Click "New Pull Request"
4. Set base branch to `staging`
5. Set compare branch to your feature branch
6. Add a descriptive title and description
7. Submit the pull request

## Important Notes

⚠️ **DO NOT CREATE ANY ADDITIONAL FILES** - Work only with the two existing files:
- `Authentication.py`
- `AuthenticationValidators.py`

## Need Help?

If you encounter any issues, please reach out to the project maintainer.