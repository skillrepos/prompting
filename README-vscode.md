# Prompt Engineering Accelerator for AI

## Mastering the Techniques, Patterns, and Strategies Behind High-Performance AI Prompting ##

These instructions will guide you through setting up the lab environment locally using Visual Studio Code and Dev Containers.

## Prerequisites

Before getting started, make sure you have the following installed on your machine:

**1. Docker Desktop** - The Dev Container runs inside a Docker container, so you need Docker installed and running.
   - Download from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   - After installation, make sure Docker Desktop is **running** before proceeding.
   - Allocate at least **4 CPUs**, **16 GB of memory**, and **32 GB of storage** in Docker Desktop's resource settings (Settings > Resources).

**2. Visual Studio Code** - Download and install from [https://code.visualstudio.com](https://code.visualstudio.com).

**3. Dev Containers Extension** - Install the **Dev Containers** extension in VS Code.
   - Open VS Code, go to the Extensions view (Ctrl+Shift+X / Cmd+Shift+X), search for **Dev Containers** (by Microsoft), and install it.
   - Alternatively, install it from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

**4. Git** - Ensure Git is installed on your system so you can clone the repository.
   - Download from [https://git-scm.com/downloads](https://git-scm.com/downloads) if needed.

## Setup Instructions

**1. Clone the repository.**

Open a terminal and run:

```
git clone https://github.com/skillrepos/prompt-accel.git
cd prompt-accel
```

**2. Open the repository in a Dev Container.**

You can do this in one of two ways:

*Option A: Use the button below to open directly in VS Code:*

Click here ➡️  [![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/skillrepos/prompt-accel)

*Option B: Open manually:*
   - Open VS Code.
   - Open the cloned `prompt-accel` folder (File > Open Folder).
   - When prompted with a notification that says *"Folder contains a Dev Container configuration file. Reopen folder to develop in a container?"*, click **Reopen in Container**.
   - If you don't see the prompt, open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P), type **Dev Containers: Reopen in Container**, and select it.

**3. Wait for the container to build and initialize.**

This will take several minutes the first time as it pulls the base image, installs features (Docker, GitHub CLI, Python, Node.js), and runs the post-creation setup scripts to configure the Python environment and install dependencies.

It will look similar to a log output in the terminal while the container is being built and configured.

The environment is ready to use when you see a terminal prompt inside VS Code.

**4. Open up the *labs.md* file so you can follow along with the labs.**

You can either open it in a separate browser window or open it directly in VS Code. The Dev Container is configured to open Markdown files in preview mode by default.

**Now, you are ready for the labs!**

## Troubleshooting

- **Docker not running**: If you see an error about Docker, make sure Docker Desktop is started and running before opening the Dev Container.
- **Insufficient resources**: The Dev Container requires at least 4 CPUs, 16 GB memory, and 32 GB storage. Check your Docker Desktop resource allocation under Settings > Resources.
- **Container build fails**: Try rebuilding with no cache by running **Dev Containers: Rebuild Container Without Cache** from the Command Palette.
- **Extensions not loading**: After the container starts, VS Code may take a moment to install the required extensions. If they don't appear, try reloading the window (Ctrl+Shift+P / Cmd+Shift+P > **Developer: Reload Window**).
