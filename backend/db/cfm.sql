CREATE USER docker;
CREATE DATABASE capibara;
GRANT ALL PRIVILEGES ON DATABASE capibara TO docker;
CREATE TABLE feedback (
    id serial PRIMARY KEY,
    client VARCHAR(200),
    product VARCHAR(200) NOT NULL,
    title VARCHAR(100) NOT NULL,
    priority VARCHAR(50) NOT NULL,
    description VARCHAR(300) NOT NULL,
    user_story VARCHAR(500) NOT NULL,
    feedback_type VARCHAR(50) NOT NULL,
    posted boolean DEFAULT FALSE
);