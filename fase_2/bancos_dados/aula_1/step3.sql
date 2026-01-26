-- 3. DCL - Data Control Language
-- Criar usuários e definir permissões de acesso aos dados

-- Criar usuário
CREATE USER analista WITH PASSWORD '102030';

---- Executar no terminal:
---- docker exec -it <3 primeiros dígitos do conteiner id> /bin/bash
---- Validar dentro do container: psql -U analista -d db_fiap
---- Só consegue fazer a query no terminal depois que der o GRANT

-- Concedendo permissões
GRANT SELECT ON investidores, acoes, transacoes TO analista;

-- Testando acesso
SELECT * FROM investidores;

-- Revogando permissões
REVOKE SELECT ON transacoes FROM analista;

-- Testando acesso
SELECT * FROM transacoes;