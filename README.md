# Griptape Nodes: SQL

This repository contains a Library of custom [Griptape Nodes](https://www.griptapenodes.com/) 
for interacting with a [SQL](https://en.wikipedia.org/wiki/SQL) database. 

## 📦 Installation

### Prerequisites

- [Griptape Nodes](https://github.com/griptape-ai/griptape-nodes) installed and running

### Install the Library

1. **Download the library files** to your Griptape Nodes libraries directory:
   ```bash
   # Navigate to your Griptape Nodes libraries directory
   cd `gtn config show workspace_directory`
   
   # Clone or download your library
   git clone https://github.com/RoseAllenM/griptape-nodes-sql.git
   ```

2. **Add the library** in the Griptape Nodes Editor:
   * Open the Settings menu and navigate to the *Libraries* settings
   * Click on *+ Add Library* at the bottom of the settings panel
   * Enter the path to the library JSON file: **your Griptape Nodes Workspace directory**`/griptape-nodes-sql/library.json`
   * Close the Settings Panel
   * Click on *Refresh Libraries*

3. **Verify installation** by checking that your custom nodes appear in the Griptape Nodes interface in the **SQL** category.

## 📄 License

These Nodes are provided under the Apache License 2.0.

## Development

1. Clone this repo and `cd` into it.
2. Create a virtual environment.
   ```shell
   python -m venv venv --upgrade-deps
   ```
3. Activate the virtual environment. 
   ```shell
   # Windows
   venv\Scripts\Activate.ps1

   # Linux
   source venv/bin/activate
   ```
4. Install the dev dependencies.
   ```shell
   pip install -r requirements.txt
   ```
5. Install [pre-commit](https://pre-commit.com/) hooks.
   ```shell
   pre-commit install
   ```

### Code Style

This package uses [Ruff](https://docs.astral.sh/ruff/) to lint and format code.

Run `ruff check --fix ; ruff format` prior to every commit.
Once installed, the pre-commit hooks do this automatically.

### Versions

This package follows [Semantic Versioning](https://semver.org/).

`Major.Minor.Patch`

To bump the version, edit [`pyproject.toml`](pyproject.toml#L3)
