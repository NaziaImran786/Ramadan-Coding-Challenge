import streamlit as st
import json

# File to store books
data_file = "books_data.json"

# Load existing books
try:
    with open(data_file, "r") as file:
        books = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    books = []

def save_books():
    """Save the books list to the JSON file."""
    with open(data_file, "w") as file:
        json.dump(books, file, indent=4)

st.title("📚 Personal Library Manager")

# Sidebar navigation
menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search Books", "Update Book", "Delete Book", "Reading Progress"])

if menu == "Add Book":
    st.header("📖 Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        if title and author and year and genre:
            books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
            save_books()
            st.success(f"Book '{title}' added successfully!")
        else:
            st.warning("Please fill in all fields.")

elif menu == "View Books":
    st.header("📚 Your Book Collection")
    if books:
        for index, book in enumerate(books, 1):
            st.write(f"{index}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✔ Read' if book['read'] else '❌ Unread'}")
    else:
        st.info("No books in your collection yet.")

elif menu == "Search Books":
    st.header("🔎 Search for a Book")
    search_text = st.text_input("Enter title or author")
    if st.button("Search"):
        results = [book for book in books if search_text.lower() in book['title'].lower() or search_text.lower() in book['author'].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("No matching books found.")

elif menu == "Update Book":
    st.header("✏ Update a Book")
    book_titles = [book['title'] for book in books]
    selected_book = st.selectbox("Select a book to update", book_titles)
    
    if selected_book:
        book = next((b for b in books if b['title'] == selected_book), None)
        if book:
            new_title = st.text_input("New Title", book["title"])
            new_author = st.text_input("New Author", book["author"])
            new_year = st.text_input("New Year", book["year"])
            new_genre = st.text_input("New Genre", book["genre"])
            new_read = st.checkbox("Have you read this book?", book["read"])
            
            if st.button("Update Book"):
                book.update({"title": new_title, "author": new_author, "year": new_year, "genre": new_genre, "read": new_read})
                save_books()
                st.success("Book updated successfully!")

elif menu == "Delete Book":
    st.header("🗑 Delete a Book")
    book_titles = [book['title'] for book in books]
    selected_book = st.selectbox("Select a book to delete", book_titles)
    
    if st.button("Delete Book"):
        books[:] = [book for book in books if book["title"] != selected_book]
        save_books()
        st.success("Book deleted successfully!")

elif menu == "Reading Progress":
    st.header("📊 Reading Progress")
    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])
    progress = (read_books / total_books * 100) if total_books > 0 else 0
    st.write(f"Total books: {total_books}")
    st.write(f"Read books: {read_books}")
    st.progress(progress / 100)
