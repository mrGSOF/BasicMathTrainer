# Basic Math Trainer

### A fun game to teach kids basic math.

**By:** Guy Soffer (GSOF), 2019

- - -

## Overview

This project is a **terminal-based math exercise program** designed to help children practice basic arithmetic operations (`+`, `-`, `*`, `/`) while learning the logic behind simple procedural programming.

Each question gives immediate feedback with audio, while mistakes trigger playful “try again” sounds. The goal is to make math both **educational and entertaining**.

- - -

## Features

*   Practice **addition, subtraction, multiplication, and division**
    
*   Adjustable difficulty levels:
    
    *   🟢 **Easy** – Numbers 0–10
        
    *   🟡 **Medium** – Numbers 0–20
        
    *   🔴 **Hard** – Numbers 0–100
        
*   Randomly generated exercises using dice-style logic
    
*   Sound effects for correct and incorrect answers
    
*   Compatible with both Windows (`winsound`) and cross-platform (`playsound`) audio playback
    
*   Optional improved visuals using the [`liveconsole`](https://github.com/TzurSoffer/Pysole) (`pysole`) library
    

- - -

## Installation

### 1. Clone or Download the Repository

```
git clone https://github.com/TzurSoffer/BasicMathTrainer.git
cd BasicMathTrainer
```

### 2. Install Dependencies

The script attempts to import `winsound` (Windows built-in) or fallback to `playsound`:

`pip install playsound`

(Optional, for enhanced visuals):

`pip install liveconsole`
- - -

## Running the Program

Simply run:

`python MathApp.py`

You’ll be prompted to:

1.  Choose difficulty level (`A`, `B`, or `C`)
    
2.  Select an operation (`+`, `-`, `*`, `/`)
    
3.  Set how many exercises you want to do
    

The program will then quiz you interactively!

- - -

## 💡 Example Interaction

pgsql

Copy code

`A - Easy (Numbers between 0 to 10) B - Medium (Numbers between 0 to 20) C - Hard (Numbers between 0 to 100) What level {A,B,C}? a Type of math operation {+,-,*,/}? + How many exercises? 3 2 + 5 = 7 VERY NICE!!! 6 + 1 = 8 VERY NICE!!! 10 + 0 = 10 VERY NICE!!!`

- - -

## Author

**Guy Soffer (GSOF)**  
2019 — Educational freeware project.
- - -
