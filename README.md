# Python Solutions for the Advent of Code Event (2022)

*!! Note: This repository is still a work in progress. - 01/15/24 !!*


This repository contains my Python 3 solutions for each of the 25 challenges for the [Advent of Code](https://adventofcode.com/2022/) event of 2022.

Each challenge has its own directory, which contains the challenge description, input data for solving that challenge, and a solution written in Python.
(See [Repository Layout](#repository-layout) for more information.)

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
    </li>
    <li>
      <a href="#roadmap">Roadmap</a>
      <ul>
        <li>
          <a href="#the-setup_tutorials-folder">The Setup Tutorials Folder</a>
        </li>
        <li>
          <a href="#the-solutions-folder">The Solutions Folder</a>
        </li>
        <li>
          <a href="#the-templates-folder">The Templates Folder</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#todo">TODO</a>
    </li>
  </ol>
</details>

---

## About the Project

This GitHub repository contains my Python code solutions for the Advent of Code 2022 event. Within each day's challenge solution folder, I have also included a Jupyter notebook that walks through my code solution, explaining my train of thought as I solved the challenge, as well as possible alternatives for solving the challenge, and why I ended up choosing one method over another. 

I make no claims to be an expert at Python or programming, but I created this GitHub repository anyway for 2 reasons:

1. I wanted to log my current knowledge of Python, and where I am currently in my self-taught coding journey. In several years, I can look back at my solutions, and see how far I have come.

2. I wanted to provide tutorials for anyone struggling with the challenges, and while my solutions may be unorthodx or may not always be the most algorithmically efficient, at least they might provide an alternative method of solving the solutions.

Again, I make no claims that these are the "best" solutions to these challenges, only that they are "my" solutions to these challenges - 100% original, unless otherwise stated. The only times I have used another's code solution was when I was well and truly stuck on a problem for more than a few days, and it is explcitly stated that the solution is not my own, as well as credited to the source.

---

## Roadmap

The CURRENT overall structure of the project is as follows (an explanation of each directory follows the tree layout):

```sh
├── README.md
├── TODO.md
├── setup
│   ├── setup_jupyter.md
│   └── setup_tutorials.md
├── solutions
│   ├── __init__.py
│   ├── day_1
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   ├── solution.ipynb
│   │   └── solution.py
│   ├── day_10
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_11
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_2
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   ├── solution.ipynb
│   │   └── solution.py
│   ├── day_3
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_4
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_5
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_6
│   │   ├── __init__.py
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   ├── solution.ipynb
│   │   └── solution.py
│   ├── day_7
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   ├── sample.txt
│   │   └── solution.ipynb
│   ├── day_8
│   │   ├── copied_solution.ipynb
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   └── tests
│       ├── __init__.py
│       ├── test_day_6.py
│       └── test_find_packet_marker.py
└── templates
    ├── generate_challenge_files.ipynb
    ├── template.ipynb
    ├── template_instructions.md
    └── template_solution.ipynb
```

---

### The `setup_tutorials/` Folder

The `setup_tutorials/` folder contains various Markdown files which contain instructions for setting up software to follow along with my solutions. 

In brief, this includes setting up (for Windows 10/11) the following software: 

- [WSL 2](/setup_tutorials/setup_wsl2.md)
- [VS Code](/setup_tutorials/setup_vscode.md)
- [Python 3](/setup_tutorials/setup_python3.md)
- [Jupyter](/setup_tutorials/setup_jupyter.md)
- [Git/GitHub](/setup_tutorials/setup_github.md)

For more information, see the [Setup Tutorials](/setup_tutorials/setup_tutorials.md) file.

---

### The `solutions/` Folder

The [solutions/](/solutions/) folder contains my Python solutions for the challenges. Each day has its own folder, and each solution has an interactive Jupyter notebook (`.ipynb` file) as well as a pure Python module (`.py` file).

The `solutions/` folder consists has the following contents:

- `day_{n}/` : A folder containing the files for that day's challenge. There are 25 `day_{n}/` folders, from `day_1/` through `day_25/`. Each of these folders contains the following files:

  - `instructions.md` : Instructions for that day's challenge from the Advent of Code page, edited with Markdown where appropriate.

  - `input.txt` : A text file containing the challenge's input data, copied directly from the Advent of Code website. ***!! Note that your own input data may be different. If you are solving the challenges to submit your own solutions, be sure to use your own challenge input. !!***

  - `solution.py` : My pure Python solution.

  - `solution.ipynb` : My solution in an interactive Jupyter notebook, with Python code cells and Markdown cells explaining the code. *(For more information on setting up your own Jupyter notebooks, see [this tutorial](/setup_tutorials/setup_jupyter.md)).* 


---

### The `templates/` Folder

The [templates/](/templates/) folder contains templates for generating challenge solution folders on the fly. Anyone may use them to generate their own challenge folders.

The template you will use is a of Jupyter notebook with custom variables. It does not pull input data from the Advent of Code page. (You must copy and paste the challenge input data and instructions for the challenge, if you so choose.)

- [generate_challenge_files.ipynb](/templates/generate_challenge_files.ipynb) : This is the only template file you need to interact with. It will create a `day_{n}/` folder based on the day you specify with a custom variable, and all of the files that go in each challenge day's folder (see [here](#the-solutions-folder) for a list of files contained in each day's solution folder).

Neither of the following files need to be interacted  with. They exist soley for reference.

- [template_instructions.md](/templates/template_instructions.md)
- [template_solution.ipynb](/templates/template_solution.ipynb)

---

## TODO

- [ ] Finish solutions for all 25 days of the event.
- [ ] Update `generate_challenge_files.ipynb` into a pure Python module.
- [ ] Discard/hide miscellaneous files such as the template files.
- [ ] Redo Day 7's solution with an original solution.
- [ ] Implement each day's solution as a pure Python module as well.
- [ ] Add more Markdown cells to each solution's `.ipynb` file to create a more "tutorial" style Jupyter notebook.