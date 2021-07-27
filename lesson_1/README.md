# Lesson 1 

## Python's Place in the World

- Machine learning
- Data science/data analysis
- Rest, Api and Web development 
- Scripting/Meta-Programming
- Prototyping

### Companies that use Python 
- Google
- Netflix
- Stripe
- Dropbox
- Reddit 
- Instagram
- Spotify

## Install

- Running python in the terminal 
```
python --version 
python3 --version 
```

Homebrew: 
- This is a package Manager for MacOS
- Extremely useful for managing commandline tools, updating python and packages

### Step 1
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Step 2
```
brew update && brew upgrade
```

### Step 3
```
brew install python3
```


## Variables

Python is a dynamically typed language

The interpretor figures out the type of the variable for you 

```
var_1 = 10
print(var_1)
print("The type: ", type(var_1))
var_1 = 3.14
print(var_1)
print("The type: " type(var_1))

```

## Arithmetic 

```
x = 1 + 2
y = x * 2 
z = y ** x

a = 5
b = 5 / 2 
c = 5 // 2 
d = 5 % 2
```

## String Format 

```
var1 = <something>
var2 = <something>
format_ = f"{var1} Lorem ipsum dolor, sit amet consectetur adipisicing elit. Perferendis, nesciunt!  {var2}"
```