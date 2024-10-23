# Working with Visual Studio Code in ML Zoomcamp 2024

- [Working with Visual Studio Code in ML Zoomcamp 2024](#working-with-visual-studio-code-in-ml-zoomcamp-2024)
  - [What is Visual Studio Code?](#what-is-visual-studio-code)
  - [How do I install VS Code?](#how-do-i-install-vs-code)
  - [How do I configure VS Code?](#how-do-i-configure-vs-code)
  - [How do I install extensions for VS Code?](#how-do-i-install-extensions-for-vs-code)
  - [How do I open VS Code from the terminal?](#how-do-i-open-vs-code-from-the-terminal)
  - [How do I select a virtual environment in VS Code?](#how-do-i-select-a-virtual-environment-in-vs-code)
  - [How do I work with jupyter notebooks in VS Code?](#how-do-i-work-with-jupyter-notebooks-in-vs-code)
  - [Conclusion](#conclusion)
  - [Optional: Install additional extensions](#optional-install-additional-extensions)
  - [Snippets](#snippets)
  - [more to explore](#more-to-explore)
  - [useful links](#useful-links)

In this article, I will try to answer the above questions to enhance your experience with Visual Studio Code during the [ML Zoomcamp 2024](https://github.com/DataTalksClub/machine-learning-zoomcamp):

When working in Data Science and Machine Learning and throughout the ML Zoomcamp and also afterwards you will work a lot with jupyter notebooks. These are a fantastic tool to analyse and clean your data, visualise it and develop machine learning models. If you dont want to use your browser (with JupyterLab or Jupyter Notebook) to work with jupyter notebooks, you can also use an IDE, for example [Visual Studio Code (VSCode)](https://code.visualstudio.com/docs/python/python-quick-start "VSCode Python Quick Start").

## What is Visual Studio Code?

Visual Studio Code, commonly known as VS Code, is a versatile and free integrated development environment (IDE) that caters to developers across macOS, Linux, and Windows platforms. Think of an IDE as a specialized toolkit crafted specifically for software development, and VS Code stands out as one of the most popular choices in this category.

At its core, VS Code is a robust source code editor with support for a wide array of programming languages. However, it goes far beyond basic editing capabilities, offering a comprehensive suite of features that enhance the development process:

- Debugging tools
- Built-in compiler support
- Syntax highlighting for improved code readability
- Code spell checking to catch typos
- Linting for code quality assurance
- Automatic code formatting

One of VS Code's strengths lies in its extensibility. The platform boasts a rich marketplace teeming with extensions that can add new functionalities or improve existing ones, allowing developers to tailor their environment to their specific needs.

Notably, VS Code also supports Jupyter notebooks, making it an excellent choice for data scientists and machine learning practitioners. This feature enables seamless integration of data analysis and model development within the same environment used for writing deployment-ready Python scripts.

In essence, VS Code provides a unified workspace where developers can effortlessly transition between various aspects of their projects, from exploratory data analysis in Jupyter notebooks to crafting production-level code, all within a single, powerful application.

## How do I install VS Code?

Since I already have [🍺 Homebrew](https://brew.sh "🍺 Homebrew") installed on my MacBook, I can install VS Code by running the following command in the terminal:

```bash
brew install --cask visual-studio-code
```

## How do I configure VS Code?

To get the most out of VS Code, you can customize the editor to suit your preferences. Here I will only show some useful settings that I use, but you can explore more.

- disable telemetry, for keeping some privacy (consider using Codium, the open-source version of VSCode)

```json
{
  "telemetry.enableTelemetry": false
}
```

- colors and icons, make yourself comfy

```json
{
  "workbench.colorTheme": "SpaceCamp",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.productIconTheme": "macos-modern",
}
```

- sidebar on the right, so the code is not shifted if you open the sidebar, less intrusive

```json
{
  "workbench.sideBar.location": "right",
}
```

- terminal

```json
{
  "terminal.integrated.fontFamily": "'Hack Nerd Font'",
  "terminal.integrated.defaultProfile.osx": "zsh",
}
```

## How do I install extensions for VS Code?

To further enhance your VS Code experience, you can install extensions from the [marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace).
In the primary side bar you can find an icon for the extensions or you can open the extensions tab in the sidebar with `Cmd+Shift+X`.

For python development, I recommend the following extensions:

- [Python Extension Pack](https://github.com/DonJayamanne/python-extension-pack)
- [Code Spell Checker](https://github.com/streetsidesoftware/vscode-spell-checker)
- [autoDocstring](https://github.com/NilsJPWerner/autoDocstring) - Python Docstring Generator
- GitLense - Git supercharged
- Rainbow CSV
- [Docker](https://github.com/microsoft/vscode-docker)

I added an [extensions.json](./extensions.json) file, you can move it to the VS Code settings folder `.vscode` in your project folder to see all recommended extensions at once.

## How do I open VS Code from the terminal?

To easy navigate between different repositories in the terminal, you can open a specific folder in VS Code directly from the terminal. In order to install the terminal command we need to open the command palette with the keyboard combination `Shift+CMD+P`. Search for `shell command` and select `Shell command: Install code command in PATH`.

You can now open a VS Code window from the terminal with the command `code <path/to/folder>`. A quick shortcut to open the current directory in VS Code is `code .`.

## How do I select a virtual environment in VS Code?

Always remember to select the correct [virtual environments](https://code.visualstudio.com/docs/python/environments) in VS Code. You can easyly select the correct environment in your status bar at the bottom of the window.

If you click on `Select Interpreter` it will open a list of available environments. Make sure to select the one from your current project.

## How do I work with jupyter notebooks in VS Code?

You need to install the `Jupyter package` (e.g. by running `pip install jupyterlab` in your terminal) in your virtual environment to work with [juypter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). Once you've done this you can open an existing jupyter notebook or create a new one by creating a new file with the extension `.ipynb`.

Select the correct virtual environment for your project and you can start working with jupyter notebooks in VS Code.

## Conclusion

VS Code is a powerful and versatile IDE that can significantly enhance your development workflow. By customizing the editor to your liking and installing relevant extensions, you can create a tailored environment that boosts productivity and streamlines your coding experience.

How do you use VS Code in your workflow? Share your tips and tricks in the comments below!



Next to setup VSCode, I installed the following VSCode extensions:

- [Black Formatter](https://github.com/microsoft/vscode-black-formatter)
- [Github Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilotvs)
- [isort](https://github.com/microsoft/vscode-isort)
- [Python Extension Pack](https://github.com/DonJayamanne/python-extension-pack)
  - 
  - IntelliCode
  - Python
  - Python Indent
  - Python Environment Manager
- [Remote - SSH](https://github.com/Microsoft/vscode-remote-release)

color themes:

- [SpaceCamp](https://github.com/dinogomez/SpaceCamp)

## Optional: Install additional extensions

[The 30 Best VSCode Extensions You Need to Use in 2024](https://hackr.io/blog/best-vscode-extensions)

- Better Comments
- Code Runner
- colorize
- Data Wrangler
- Highlight Line
- indent-rainbow
- Material Icon Theme
- Markdown All in One
- Markdown PDF
- Markdown Preview Mermaid Support
- Path Intellisense
- Prettier - Code formatter
- Prettier SQL VSCode
- Rainbow CSV
- TODO Highlight
- Todo Tree
- Trailing Spaces
- vscode-pdf

[Support shell integration in oh-my-zsh and powerlevel10k](https://github.com/microsoft/vscode/issues/146587)

## Snippets

## more to explore

[Nasc VSCode Touchbar](https://marketplace.visualstudio.com/items?itemName=felipe.nasc-touchbar)

[How to customize the touch bar in visual studio code?](https://stackoverflow.com/questions/47060436/how-to-customize-the-touch-bar-in-visual-studio-code)

[How to Configure the Touch Bar in Visual Studio Code in Under 5 Minutes](https://dev.to/p42/how-to-configure-the-touch-bar-in-visual-studio-code-in-under-5-minutes-50lm)

## useful links

[Setup macOS for Development]

[Setup macOS for Development]: https://dev.to/equiman/setup-macos-for-development-3kc2

[The Pythonista’s Guide to Setting Up a Mac for 🐍 Python 🐍 Development](https://www.kristen-foster-marks.com/post/python-dev-setup)