import React, { useState } from 'react';
import axios from 'axios';

function AskQuestion() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching answer:', error);
      setAnswer('Sorry, there was an error processing your request.');
    }
  };

  return (
    <div>
      <h1>Ask a Question</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Type your question here"
        />
        <button type="submit">Submit</button>
      </form>
      {answer && <p>Answer: {answer}</p>}
    </div>
  );
}

export default AskQuestion;
