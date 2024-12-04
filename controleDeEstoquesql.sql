-- criando o banco de dados
-- CREATE DATABASE controle_de_estoque;

-- entrando no banco de dados criado 
-- USE controle_de_estoque;

-- CREATE TABLE categorias (
--     id_categoria INT AUTO_INCREMENT PRIMARY KEY,
--     nome_categoria VARCHAR(100) NOT NULL,
--     descricao TEXT
-- );

-- CREATE TABLE localizacoes (
--     id_localizacao INT AUTO_INCREMENT PRIMARY KEY,
--     descricao VARCHAR(100) NOT NULL,
--     deposito VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE produtos (
--     id_produto INT AUTO_INCREMENT PRIMARY KEY,
--     nome_produto VARCHAR(100) NOT NULL,
--     descricao TEXT,
--     preco DECIMAL(10, 2) NOT NULL,
--     quantidade INT NOT NULL,
--     categoria_id INT,
--     localizacao_id INT,
--     data_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria),
--     FOREIGN KEY (localizacao_id) REFERENCES localizacoes(id_localizacao)
-- );

-- INSERINDO DADOS	
--  INSERT INTO categorias (nome_categoria, descricao)
--  VALUES 
--  ('Frutas', 'Frutas diversas'),
--  ('Cosmeticos', 'Produtos de Cosmeticos diversos');


-- INSERT INTO localizacoes (descricao, deposito) 
-- VALUES
--  ('Prateleira A', 'Depósito 1'),
--  ('Prateleira A', 'Depósito 2'),
--  ('Prateleira A', 'Depósito 3');
--  



-- INSERT INTO produtos (nome_produto, descricao, preco, quantidade, categoria_id, localizacao_id) 
-- VALUES ('Celular', 'Smartphone de última geração', 1999.99, 20, 1, 1);


-- USE controle_de_estoque;
-- select * from produtos;
-- select * from categorias;
-- select * from localizacoes;
--  

 
-- CREATE TABLE movimentacoes (
--     id_movimentacao INT AUTO_INCREMENT PRIMARY KEY,
--     produto_id INT NOT NULL,
--     tipo_movimentacao ENUM('entrada', 'saida') NOT NULL,
--     quantidade INT NOT NULL,
--     data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (produto_id) REFERENCES produtos(id_produto)
-- );
use controle_de_estoque
select * FROM localizacao
 


