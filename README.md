# Exercício Ubiwhere

> ***Abstract*:** Pretende-se uma API REST que permita a gestão de ocorrências em ambiente urbano. As ocorrências devem ter **descrição**, uma **localização geográfica**, **autor**, **data de criação**, **data de actualização**, **estado** (por validar, validado, resolvido) e pertencer a uma das seguintes categorias:
> - CONSTRUCTION: Eventos planeados de obras nas estradas;
> - SPECIAL_EVENT: eventos especiais (concertos, feiras, etc);
> - INCIDENT: acidentes ou outros eventos inesperados;
> - WEATHER_CONDITION: eventos meteorológicos que afetam as estradas;
> - ROAD_CONDITION: estados das estradas que afetem quem circula nestas (piso degradado, buracos, etc).
>
>1) API REST
>1.1) Tem de permitir a adição de ocorrências (com a localização geográfica, e autor associados). Nota: O estado default será sempre por validar quando estas são criadas e o autor deve ser um utilizador registado;
>1.2) Tem de permitir a actualização de ocorrências (para mudar o estado das mesmas para "validadas" por um administrador do sistema);
>1.3) Tem de permitir a filtragem de ocorrências por autor, por categoria e por localização (raio de alcance).

## Instalação:
 1. `docker-compose up -d --build`
 2. `docker-compose down`	(**Ver:** Limitações encontradas)
 3. `docker-compose up -d` (**Ver:** Limitações encontradas)
 4. `docker-compose exec web python manage.py migrate`
 5. `python manage.py createsuperuser`
 
## Postman Collection:
O *Postman Collection* pode ser obtido em:
- [*Published Postman Collection*](https://documenter.getpostman.com/view/12976501/TVRhdAHs)
- [*RAW Postman Collection*](https://www.getpostman.com/collections/2b167bf525867bb0b5df)


## Endpoints:
 - `{HOST}/API/` [Método: GET]:
	 - **Descrição:** Listagem de todas as ocorrências
 - `{HOST}/API/` [Método: POST]:
	 - **Descrição:** Criação de uma nova ocorrência
	 - ***Request body*:** Objeto *JSON* com representação do modelo `API.models.Ocorrencia`
 - `{HOST}/API/autor/<int:autor>/`:
	 - **Descrição:** Pesquisa por autor
 - `{HOST}/API/categoria/<int:categoria>/`:
	 - **Descrição:** Pesquisa por categoria
 - `{HOST}/API/autor/<int:autor>/categoria/<int:categoria>/`:
	 - **Descrição:** Pesquisa por autor e categoria
 - `{HOST}/API/validate-ocorrencia/`:
	 - **Descrição:** Validação de uma ocorrência
	 - ***Request header*:** `Authorization: Token <token_de_autenticação>`
	 - ***Request body*:** Objeto *JSON* com `id` da ocorrência a validar
 - `{HOST}/API/api-token-auth/`:
	 - **Descrição:** Obtém *token* de autenticação
	 - ***Request header*:** `Content-Type: application/json`
	 - ***Request body*:** Objeto *JSON* com `username` e `password` do administrador

**Nota:** Para executar o *endpoint* `{HOST}/API/validate-ocorrencia/`, é necessário antes obter um *token* de autenticação fazendo uma chamada ao *endpoint* `{HOST}/API/api-token-auth/` e fornecendo um `username` e `password`. Após obtido o *token*, este deve ser colocado no *Header* `Authorization` do *endpoint* `{HOST}/API/validate-ocorrencia/` (**Importante:** o conteúdo do *Header* `Authorization` deve manter o formato: `Token <token_de_autenticação>`)

## Utilização:

 1. Iniciar servidor
 2. Consultar [*Published Postman Collection*](https://documenter.getpostman.com/view/12976501/TVRhdAHs), ou importar [*RAW postman collection*](https://www.getpostman.com/collections/2b167bf525867bb0b5df)
 4. Fazer chamadas aos *endpoints* da API

---
**Limitações encontradas:**
Quando se corre o comando `docker-compose up -d --build` pela primeira vez, pode acontecer que o *container* do serviço `web` seja executado antes do *container* do serviço `db`, causando problemas.
Por isso é recomendado, **apenas na primeira vez**, que o comando `docker-compose up -d --build` seja executado até ao fim, de seguida terminar a execução de todos os *containers* com `docker-compose down`, e por fim (e nas futuras execuções) voltar a iniciá-los com `docker-compose up -d`.

**Nota:** Mesmo usando a definição `depends: db` no serviço `web`, o problema parece persistir. É também comum a utilização de um *script* `wait-for-it.sh`, mas não foi possível testar no tempo previsto (**Ver:** Referências).


---
 **Referências docker:**
 - [Documentação Django](https://docs.djangoproject.com/en/3.1/)
 - [Documentação Django Rest Framework](https://www.django-rest-framework.org/) 
 - [Documentação Docker](https://docs.docker.com/) 
 - [TestDriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx)
 - [Docker - wait-for-it.sh](https://docs.docker.com/compose/startup-order/)
 - [Vishnubob - wait-for-it.sh](https://github.com/vishnubob/wait-for-it)
 - [Data migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/#data-migrations)

**Agradecimentos:**

 - [Nuno Rocha](https://github.com/nunobifes)