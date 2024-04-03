# Quicktail Operators

Are you tired of wrapping everything in parentheses for quick and dirty prototyping? Annoyed by those pesky prefix prints that get in the way of your workflow? If you're still here, congratulations! You're in for a treat with **quicktail operators**.

### What is Quicktail Operators?

Quicktail operators are here to make your Python coding experience smoother and more efficient. They are designed for those times when printing is an afterthought and you just want to get things done without cluttering your code.

### Features

- **Tailprint Operator**: Easily print the result of an expression at the end of a line, without the need for parentheses.
  ```python
  2 + 2 | tailprint
  # printed: 4
  ```
  Useful when you want a quick result without the hassle of wrapping everything in print statements.
  

### Customize output:
```
from quicktail import tailprint

# Instead of:
# pprint(json.dumps(function(some_class.raw_data())),width=3)
json.dumps(function(some_class.raw_data())) | tailprint(width=3)
# Get immediate formatting without interrupting your code flow!

```
### Define Your Own End of Line Operator
With Quicktail Operators, you can define your custom end-of-line operator to fit your needs:

```
toFile = TailOp(file.write)
"username" | toFile
```

### Installation
```
pip install quicktail
```


### Contribution
Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to open an issue or submit a pull request on GitHub.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

