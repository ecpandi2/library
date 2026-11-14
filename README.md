# Campus Library Manager

A small object-oriented Python project for books, magazines and DVDs.
Requires Python 3.12 or later. No external packages or installation needed.

## Run

Extract the ZIP, open a terminal in `library_manager`, then run:

```bash
python3 main.py
```

On Windows:

```powershell
python main.py
```

`output.txt` contains the full console output captured from the final demo run.
To regenerate it, run `python3 main.py > output.txt` (Windows: `python main.py > output.txt`).

## Files and features

- `models.py`: abstract LibraryItem, three item subclasses and Member.
- `main.py`: two members, three items, descriptions, polymorphic fees, successful
  loans and returns, duplicate-loan errors, a custom borrow-limit error,
  invalid returns, private access and safe list copying.
- `output.txt`: actual demo output.
- `README.md`: run instructions and the three reflection answers below.

Book fees are Rs 2/day, magazine fees Rs 1/day and DVD fees Rs 5/day.
The mixed-item loop produces Rs 6, Rs 3 and Rs 15 for three days, without type checks.
Alice uses the default limit of three; Bob uses a custom limit of one so the
demo can trigger a limit error using only the required three items.
Negative or non-integer late days raise ValueError before a return changes state.

The starter's `init` methods have been corrected to `__init__`, Python's constructor name.

## Reflection

### 1. Why is LibraryItem abstract, and what happens if DVD forgets late_fee()?

LibraryItem is abstract because it defines common item behaviour while requiring
each concrete item type to provide its own late-fee calculation. If DVD does not
implement late_fee(), it remains abstract and constructing a DVD raises TypeError.

### 2. What happens when you read item.__available, and why use is_available()?

Reading item.__available directly from outside the class raises AttributeError
because Python name-mangles the double-underscore attribute. is_available()
provides a public way to read the state while methods control changes; name
mangling discourages accidental access rather than providing security.

### 3. How do LibraryItem.total_items and self.title differ?

LibraryItem.total_items is a class attribute shared across all item types and
counts the items constructed during the current process. self.title is an
instance attribute, so each individual item has its own title.
