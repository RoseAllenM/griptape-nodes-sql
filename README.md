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
