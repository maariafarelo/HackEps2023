import React, { useState, useEffect } from 'react';
import './Admin.css';

// Card component
const Card = ({ title, description, onAddToAsana }) => {
    return (
        <div className='card'>
            <h3>{title}</h3>
            <p>{description}</p>
            <button onClick={onAddToAsana}>Add to Asana</button>
        </div>
    );
};

// Admin component
function Admin() {

    const [cards, setCards] = useState([]);
    useEffect(() => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://127.0.0.1:5000/feedback/');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send();
        xhr.onload = () => {
            const data = JSON.parse(xhr.response);
            setCards(data);
        };
    }, []);


    const handleAddToAsana = (cardId) => {
        const xhr = new XMLHttpRequest();
        const path = 'http://127.0.0.1:5000/feedback/' + cardId;
        console.log(path);
        xhr.open('POST', path);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send();
        window.location.reload();
    };

    return (
        <div className='adminPage'>
            <div className='manageFeedback'>
                <h1>Manage your feedback!</h1>
            </div>
            <div className='cards'>
                {cards.map((card) => (
                    <Card
                        key={card.id}
                        title={card.title}
                        description={card.description}
                        onAddToAsana={() => handleAddToAsana(card.id)}
                    />
                ))}
            </div>
        </div>
    );
}

export default Admin;
