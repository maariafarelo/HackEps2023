import React, { useState, useEffect } from 'react';
import './Admin.css';
import {Link} from "react-router-dom";

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
        xhr.open('GET', 'http://127.0.0.1:5000/feedback');
        xhr.setRequestHeader('Content-Type', 'text/plain');
        xhr.send();
        xhr.onload = () => {
            const data = JSON.parse(xhr.response);
            console.log(data)
            setCards(data.feedback_not_posted);
        };
    }, []);


    const handleAddToAsana = (cardId) => {
        const xhr = new XMLHttpRequest();
        const path = 'http://127.0.0.1:5000/feedback/' + cardId;
        console.log(path);
        xhr.open('POST', path);
        xhr.setRequestHeader('Content-Type', 'text/plain');
        xhr.send();
        xhr.onload = ()=>{
            window.location.reload()
        };
        // window.location.reload();
    };

    return (
        <div className='adminPage'>
            <div className='asana-button'>
                <a href="https://app.asana.com/0/1206028568433081/1206028802878624" target={"_blank"}>Go to Asana</a>
            </div>
            <div className='manageFeedback'>
                <h1>Manage your feedback!</h1>
            </div>
            <div className='cards'>
                {cards ? cards.map((card) => (
                    <Card
                        key={card.id}
                        title={card.title}
                        description={card.description}
                        onAddToAsana={() => handleAddToAsana(card.id)}
                    />
                ))
                :
                    <div className='manageFeedback'>
                        <h3>You don't have any more feedback!</h3>
                    </div>
                }
            </div>
        </div>
    );
}

export default Admin;
