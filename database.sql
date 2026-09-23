-- Remove a tabela caso ela já exista
DROP TABLE IF EXISTS content;


-- Cria a tabela de conteúdos
CREATE TABLE content (
    c_id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_title TEXT NOT NULL,
    c_text TEXT NOT NULL,
    c_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    c_status TEXT DEFAULT 'on'
);


-- Insere alguns dados para teste
INSERT INTO content (c_title, c_text)
VALUES (
    'Primeiro conteúdo',
    'Este é o primeiro conteúdo cadastrado no banco de dados.'
);


INSERT INTO content (c_title, c_text)
VALUES (
    'Aprendendo Flask',
    'Estou aprendendo a integrar Python, Flask, HTML e SQLite.'
);


INSERT INTO content (c_title, c_text)
VALUES (
    'Banco de dados SQLite',
    'Agora o projeto também possui armazenamento de dados.'
);