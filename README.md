# Console Application for Managing a Library of Books

This console application allows users to manage a library of books. Users can add, remove, search, and display books. Each book contains a unique identifier, title, author, publication year, and status.

## Application Functionality

### 1. Adding a Book
Users can add a new book to the library by entering the following details:
- **title**: The title of the book
- **author**: The author of the book
- **year**: The publication year of the book

When a book is added, a unique identifier is automatically generated, and the book's status is set to "available".

### 2. Removing a Book
Users can remove a book from the library by entering the unique identifier of the book. If a book with the specified identifier does not exist, the application will display an error message.

### 3. Searching for a Book
Users can search for books by criteria.

### 4. Changing the Status of a Book
Users can change the status of a book by entering the unique identifier of the book and the new status ("available" or "issued"). If a book with the specified identifier does not exist, the application will display an error message.

## Data Storage
Book data is stored in MongoDB. Each time the data is modified (added, removed, or status changed), the file is updated to maintain the current information about the books.

## Error Handling
The application ensures proper error handling for scenarios such as:
- Attempting to delete a non-existent book
- Attempting to change the status of a book with a non-existent identifier
- Invalid input when adding a book

