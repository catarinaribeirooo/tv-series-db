# Base de Dados: Tv Series

Unidade Curricular: Base de Dados, 2º ano/1º semestre da Licenciatura IACD
Este projeto consiste na conceção e implementação de uma base de dados relacional normalizada para a gestão de conteúdos audiovisuais (séries de TV). 
O sistema foi desenhado para garantir a integridade referencial de dados complexos, como relações entre múltiplas temporadas, elencos vastos e categorização por géneros.

Linguagem Usada: SQL

##   Arquitetura dos Dados

O modelo está organizado à volta de 4 entidades principais e 3 tabelas de junção para gerir relações M:N:

* Entidades: Series, Season, Actor e Genre
* Relações Implementadas: Cast (Atores em Series), Series_Genre (Vários Géneros por Serie), Participantes (Registo de atores por temporada)

## Dados 

Os dados foram extraídos de fontes reais (IMDB e Kaggle) e processamento para garantir consistência antes do carregamento.

* Volume de Dados: Povoamento de aproximadamente 2.000 séries e 5.600 atores.
* Método: utilização de scripts de LOAD DATA INFILE para otimização do processo.

## Para Executar

Executar tabelas.sql para criar o esquema e as restrições de integridade
Executar dados.sql para o povoamento das tabelas.

<img width="1046" height="563" alt="image" src="https://github.com/user-attachments/assets/0893619e-f476-47d3-9b39-287eb0a57ec7" />

<img width="608" height="658" alt="image" src="https://github.com/user-attachments/assets/a982f2f1-f000-4159-8328-a5ecc8c04cb3" />

