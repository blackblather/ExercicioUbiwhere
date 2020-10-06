# Exercício Ubiwhere

> ***Abstract*:** Pretende-se uma API REST que permita a gestão de ocorrências em ambiente urbano. As ocorrências devem ter **descrição**, uma **localização geográfica**, **autor**, **data de criação**, **data de actualização**, **estado** (por validar, validado, resolvido) e pertencer a uma das seguintes categorias:
> - CONSTRUCTION: Eventos planeados de obras nas estradas;
> - SPECIAL_EVENT: eventos especiais (concertos, feiras, etc);
> - INCIDENT: acidentes ou outros eventos inesperados;
> - WEATHER_CONDITION: eventos meteorológicos que afetam as estradas;
> - ROAD_CONDITION: estados das estradas que afetem quem circula nestas (piso degradado, buracos, etc).

## Instalação:
**Método #1: Docker:**
 1. `docker-compose up -d --build`
 2. `docker-compose down`	(**Ver:** Limitações encontradas)
 3. `docker-compose up -d` (**Ver:** Limitações encontradas)
 4. `docker-compose exec web python manage.py migrate`

**Método #2: Manualmente:**
 1. Instalar PostgreSQL 13.0
 2. Instalar Python 3.8.5
 3. `pip install -Iv Django==3.1.2`
 4. `pip install -Iv djangorestframework==3.12.1`
 5. `pip install -Iv psycopg2==2.8.6`
 6. `python manage.py migrate`
 7. `python manage.py runserver`

## Base de Dados:
Para popular a base de dados com os valores iniciais, deve-se abrir a plataforma pgAdmin 4 e seleccionar a base de dados `DBExercicioUbiwhere`. De seguida deve-se abrir o menu de contexto das tabelas `API_estados` e `API_categorias` e selecionar a opção `Import/Export...` e selecionar os ficheiros `estados_dump_file.txt` e `categorias_dump_file.txt` para cada uma das tabelas respetivamente. (**Ver:** Limitações encontradas)

Para criar uma conta de administrador do Django, deve ser usado o seguinte comando:

    python manage.py createsuperuser
 
## Postman Collection:
O *Postman Collection* pode ser obtido em: [*Postman Collection*](https://www.getpostman.com/collections/43751fceec1448c44dfd)

Para executar o *endpoint* `Validate ocorrencia`, é necessário antes obter um *token* de autenticação fazendo uma chamada ao *endpoint* `Get admin authentication token`. Após obtido o *token*, este deve ser colocado no *Header* `Authorization` do *endpoint* `Validate ocorrencia` (**Importante:** o conteúdo do *Header* `Authorization` deve manter o seguinte formato: `Token <token_obtido_previamente>`)
## Utilização:

 1. Iniciar servidor (**Ver** Instalação)
 2. Importar [*postman collection*](https://www.getpostman.com/collections/43751fceec1448c44dfd)
 3. Popular base de dados (**Ver:** Base de dados)
 4. Criar conta de administrador (**Ver:** Base de dados)
 5. Fazer chamadas aos *endpoints* da API

---
**Limitações encontradas:**
Quando se corre o comando `docker-compose up -d --build` pela primeira vez, pode acontecer que o *container* do serviço `db` seja executado antes do *container* do serviço `web`, causando problemas.
Por isso é recomendado, **apenas na primeira vez**, que o comando `docker-compose up -d --build` seja executado até ao fim, de seguida terminar a execução de todos os *containers* com `docker-compose down`, e por fim (e nas futuras execuções) voltar a iniciá-los com `docker-compose up -d`.

**Nota:** Mesmo usando a definição `depends: db` no serviço `web`, o problema parece persistir. É também comum a utilização de um *script* `wait-for-it.sh`, mas não foi possível testar no tempo previsto.

Para popular a base de dados foi tentado utilizar a funcionalidade de *fixtures* do Django, mas sem sucesso.
Foi também tido em consideração a possibilidade de criar *endpoints* na API dedicados a esse fim, mas iria poluir o código desnecessariamente.
Não tendo mais tempo para explorar outras possíveis soluções, foi escolhida a opção de exportar o conteúdo das tabelas `API_estados` e `API_categorias` a partir do pgAdmin 4.


---
 **Referências docker:**
 - [Documentação Django](https://docs.djangoproject.com/en/3.1/)
 - [Documentação Django Rest Framework](https://www.django-rest-framework.org/) 
 - [Documentação Docker](https://docs.docker.com/) 
 - [TestDriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx)
 - [Docker - wait-for-it.sh](https://docs.docker.com/compose/startup-order/)
 - [Vishnubob - wait-for-it.sh](https://github.com/vishnubob/wait-for-it)