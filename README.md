## API Endpoints

### Books API
- **GET /books/** → List all books (Public).
- **GET /books/<int:pk>/** → Get a book by ID (Public).
- **POST /books/create/** → Create a book (Authenticated users only).
- **PUT /books/<int:pk>/update/** → Update a book (Authenticated users only).
- **DELETE /books/<int:pk>/delete/** → Delete a book (Authenticated users only).

### Permissions
- Read operations (List/Detail) are **open to all**.
- Write operations (Create/Update/Delete) **require authentication**.
