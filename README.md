# Atividade Jogos

Projeto Django da atividade prática: cadastro de jogos com listagem, busca, filtros e paginação.

## Modelos

- **Desenvolvedora**: nome, país
- **Plataforma**: nome, fabricante
- **Jogo**: nome, ano de lançamento, desenvolvedora (FK), plataforma (FK)

Todos os modelos estão registrados no Django Admin.

## Funcionalidades

- Listagem de jogos (`/`)
- Busca por nome do jogo (parâmetro `q`)
- Filtro por desenvolvedora e por plataforma (parâmetros `desenvolvedora` e `plataforma`)
- Paginação com 5 jogos por página, preservando os filtros ativos ao trocar de página

## Como rodar o projeto

```powershell
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Integrantes
- **Malu**
- **Emiily**
- **Yas**

## Funcionalidades e filtros implementados
- **Modelos e relacionamentos (`RF01` / `RF02`):** Modelos `Desenvolvedora` e `Plataforma` relacionados a `Jogo` via `ForeignKey`, gerenciados no Django Admin com mais de 20 jogos cadastrados e pelo menos 3 registros em cada modelo relacionado.
- **Listagem (`RF03`):** Exibe os jogos cadastrados com nome, desenvolvedora, plataforma e ano de lançamento.
- **Pesquisa textual (`RF04`):** Campo de busca por nome do jogo via `GET` (`?q=...`) utilizando `nome__icontains` no ORM do Django.
- **Filtros dinâmicos combinados (`RF05`):** Dois campos `<select>` enviados via `GET` (`desenvolvedora` e `plataforma`) que funcionam individualmente ou combinados entre si e com a pesquisa textual.
- **Paginação (`RF06`):** Divisão dos resultados filtrados em páginas de **5 registros por página** com `Paginator`, exibindo botões de anterior/próxima, página atual e total de páginas.
- **Preservação dos filtros (`RF07`):** Mantém `q`, `desenvolvedora` e `plataforma` na `querystring` ao navegar entre as páginas.


Acesse `http://127.0.0.1:8000/` para a listagem e `http://127.0.0.1:8000/admin/` para o painel de administração.

