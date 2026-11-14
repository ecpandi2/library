"""Run with python3 main.py (Windows: python main.py)."""

from models import Book, DVD, LibraryItem, Magazine, Member


def main():
    print("CAMPUS LIBRARY MANAGER")
    print("\n1. Abstract parent")
    try:
        LibraryItem("x", 1)
    except TypeError:
        print("Cannot create LibraryItem directly: late_fee() is abstract (TypeError).")

    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Campus Science", 2, 12)
    dvd = DVD("Learning Python", 3, 90)
    items = [book, magazine, dvd]
    alice = Member("Alice", 101)
    bob = Member("Bob", 102, max_items=1)

    print("\n2. Item descriptions and polymorphic fees")
    for item in items:
        print(f"{item.describe()} -> late fee for 3 days: Rs {item.late_fee(3)}")
    print("Total items created:", LibraryItem.total_items)
    print("Alice's default limit:", alice.max_items)
    print("Bob's custom limit:", bob.max_items)

    print("\n3. Borrowing and invalid actions")
    for member, item in [(alice, book), (bob, book), (alice, book),
                         (bob, dvd), (bob, magazine), (alice, magazine)]:
        try:
            member.borrow(item)
            print(f"{member.name} borrowed: {item.title}")
        except ValueError as e:
            print("Could not borrow:", e)
    print("Alice's borrowed titles:", alice.borrowed_titles())
    print("Bob's borrowed titles:", bob.borrowed_titles())
    try:
        bob.return_item(book)
    except ValueError as e:
        print("Could not return:", e)

    print("\n4. Encapsulation")
    try:
        print(book.__available)
    except AttributeError:
        print("Direct book.__available access raises AttributeError.")
    print("Book available via is_available():", book.is_available())
    titles = alice.borrowed_titles()
    titles.clear()
    print("Clearing the returned title list leaves Alice's loans unchanged:",
          alice.borrowed_titles())

    print("\n5. Returns and input validation")
    try:
        alice.return_item(book, days_late=-1)
    except ValueError as e:
        print("Could not return:", e)
    print("Book still borrowed after invalid days:", not book.is_available())
    for member, item, days in [(alice, book, 3), (alice, magazine, 0), (bob, dvd, 3)]:
        try:
            fee = member.return_item(item, days_late=days)
            print(f"{member.name} returned {item.title} ({days} days late); fee: Rs {fee}")
        except ValueError as e:
            print("Could not return:", e)
    try:
        alice.return_item(book)
    except ValueError as e:
        print("Could not return again:", e)
    print("All items available:", all(item.is_available() for item in items))
    print("Alice's borrowed titles:", alice.borrowed_titles())
    print("Bob's borrowed titles:", bob.borrowed_titles())


if __name__ == "__main__":
    main()
