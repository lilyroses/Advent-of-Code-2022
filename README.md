# Python Solutions for the Advent of Code Event (2022)

*!! Note: This repository is still a work in progress. - 10/01/23 !!*

This repository will contain my Python (3) solutions for each of the 25 challenges for the Advent of Code event of 2022.

Each challenge has its own directory, which contains the challenge description, input data for solving that challenge, and a solution written in Python.
(See [Project Structure][#project-structure] for more information.)

---

## Project Description 

(From the [Advent of Code website](https://adventofcode.com/day/1/) for the 2022 event):

*Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas.*

*For that, their favorite snack is a special type of star fruit that only grows deep in the jungle.*

*The Elves have brought you on their annual expedition to the grove where the fruit grows.*

*To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th.*

*Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.*

**Collect stars by solving puzzles.**

*Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.*

*Each puzzle grants one star. Good luck!*

---

## Repository Purpose

I created this repository for several reasons.

First, I wanted a way to showcase my growing knowledge of Python. 

I also wished to provide solutions publicly that anyone struggling with the event may find helpful. 

Finally, throughout the course of building this repository, I have decided to make writing these solutions an exercise in good programming practices, honing skills such as proper code documentation and robust unit testing.

---

## Project Structure

*!! Note: The project structure is subject to change as this repository is currently a work in progress. See [TODO][#todo] section for more information on pending updates. !!*

Below is an outline of the project tree (created with the bash `tree` command - very useful!). Following that is a brief description of each.

---

### Project Tree

The overall structure of the project is currently as follows:

```sh
.
├── README.md
├── TODO.md
├── solutions
│   ├── day_1
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
│   ├── day_2
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.ipynb
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
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.py
│   ├── day_7
│   │   ├── input.txt
│   │   ├── instructions.md
│   │   └── solution.py
│   └── tests
│       ├── test_day_6.py
│       └── test_find_packet_marker.py
└── templates
    ├── generate_challenge_files.ipynb
    ├── template_instructions.md
    └── template_solution.ipynb
```

---

### Descriptions of Files and Directories

- `solutions/` : The solutions file contains all of the solutions for the event. Each solution is contained within its own folder, named for the day the challenge corresponds to (e.g., `day_1`...`day_25`.)

- `day_{n}/` : Each of these directories contains:

  - `instructions.md` : Instructions for the challenge, copied and pasted directly from the Advent of Code webpage for that challenge.

  - `input.txt` : The input data for that challenge, again copied directly from the Advent of Code website.

  - `solution.ipynb` : An interactive Jupyter notebook containing code solutions in an interactive. Ideally, so that anyone struggling with the challenge can use an interactive Jupyter notebook to walk through the steps themselves, with extra explanation added in Markdown cells.

---

## TODO

- [ ] Update `generate_challenge_files.ipynb` into a pure Python module.
- [ ] Discard/hide miscellaneous files such as the template files.
- [ ] Redo Day 7 with original solution
- [ ] Implement each day's solution as a pure Python module
- [ ] Add more Markdown cells to each solution's `.ipynb` file to create a more "tutorial" style Jupyter notebook 