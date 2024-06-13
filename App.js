import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/api/books')
      .then(response => {
        setBooks(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error);
      });
  }, []);

  const addBook = () => {
    const newBook = { title, author };
    axios.post('http://localhost:5000/api/books', newBook)
      .then(response => {
        setBooks([...books, response.data]);
        setTitle('');
        setAuthor('');
      })
      .catch(error => {
        console.error('There was an error adding the book!', error);
      });
  };

  return (
    <div>
      <h1>Library</h1>
      <ul>
        {books.map((book, index) => (
          <li key={index}>{book.title} by {book.author}</li>
        ))}
      </ul>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <input
        type="text"
        placeholder="Author"
        value={author}
        onChange={e => setAuthor(e.target.value)}
      />
      <button onClick={addBook}>Add Book</button>
    </div>
  );
}

export default App;
