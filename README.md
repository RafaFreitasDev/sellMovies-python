# PARA RODAR O PROJETO 

## Requisitos ##
- Ter o Python instalado

- Ter o Django instalado

- Ter o pip instalado (gerenciador de pacotes)

## Fazer os seguintes comandos ##

pip install -r .\requirements.txt (para instalar dependencias)

python .\manage.py migrate (para rodar as migrations)

python  .\manage.py runserver (para iniciar o servidor)

## Endpoints:

| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
| POST   | /login                     | Gera o token de autenticação                      | Qualquer usuário, não necessita token  |
| POST   | /users                     | Criação de usuário                                | Qualquer usuário, não necessita token  |
| GET    | /users                     | Lista todos os usuários                           | Qualquer usuário, não necessita token  |
| GET    | /users/:id                 | Lista todos os usuários                           | Qualquer usuário, obrigatório token    |
| PATCH  | /users/:id                 | Atualiza um usuário                               | Obrigatório token e dono da conta      |
| POST   | /movies                    | Criação de filme                                  | Usuário employee, obrigatório token    |
| GET    | /movies                    | Lista todos os filmes                             | Qualquer usuário, não necessita token  |
| POST   | /movies/:id/order          | Criação de filme compra                           | Qualquer usuário, obrigatório token    |


### **POST - /users/login/**

Rota de login do usuário. 

**Url da requisição**: `http://127.0.0.1:8000/api/users/login/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "username": "silvia",
  "password": "2222"
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MDQ1NzUzMCwiaWF0IjoxNjkwMzcxMTMwLCJqdGkiOiJiNzc4ODQyY2U0YWY0M2Y4OWNkMDY4OGE2ODNhNjVjZSIsInVzZXJfaWQiOjJ9.ksLIjHNqviQn0WGVgo1gUbuy1hTuqyIEKmMHo2k824k",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwMzcxNDMwLCJpYXQiOjE2OTAzNzExMzAsImp0aSI6IjBlNDc1MjgzZDA2ZDQ3N2FiZDFkMGZiNmIwZmZlY2JkIiwidXNlcl9pZCI6Mn0.Fgw5Z_-46nYN7epU4sBcij0WSyaid4rHxAssT2WZK0Y"
}
```

### **POST - /users/**

Rota de criação de usuário. As chaves **_is_employee_** e **_is_superuser_** são **_opcionais_**

**Url da requisição**: `http://127.0.0.1:8000/api/users`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "username": "silvia",
  "email": "silvia@gmail.com",
  "birthdate": "2014-03-02",
  "first_name": "Silvia",
  "last_name": "Freitas",
  "password": "2222",
  "is_employee": true
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">201 CREATED</b> |

```json
{
	"id": 2,
	"username": "silvia",
	"email": "silvia@gmail.com",
	"first_name": "Silvia",
	"last_name": "Freitas",
	"birthdate": "2014-03-02",
	"is_employee": true,
	"is_superuser": true
}
```

### **GET - /users/**

Rota de listagem de todos usuários.

**Url da requisição**: `http://127.0.0.1:8000/api/users/`

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
[
	{
		"id": 1,
		"username": "pedro",
		"email": "pedro@gmail.com",
		"first_name": "Pedro",
		"last_name": "Freitas",
		"birthdate": "2014-03-02",
		"is_employee": true,
		"is_superuser": true
	},
	{
		"id": 2,
		"username": "silvia",
		"email": "silvia@gmail.com",
		"first_name": "Silvia Helena",
		"last_name": "Freitas",
		"birthdate": "2014-03-02",
		"is_employee": true,
		"is_superuser": true
	},
	{
		"id": 3,
		"username": "rafael",
		"email": "rafael@gmail.com",
		"first_name": "Rafael",
		"last_name": "Freitas",
		"birthdate": "2014-03-02",
		"is_employee": false,
		"is_superuser": false
	}
]
```

### **PATCH - /users/:id/**

Atualizar o úsuário dono da conta pelo id recebido nos parâmetros da rota.

**Url da requisição**: `http://127.0.0.1:8000/api/users/2/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "first_name": "Silvia Maria"
}
```

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"id": 2,
	"username": "silvia",
	"email": "silvia@gmail.com",
	"first_name": "Silvia Maria",
	"last_name": "Freitas",
	"birthdate": "2014-03-02",
	"is_employee": true,
	"is_superuser": true
}
```

### **POST - /movies/**

Rota de criação de filme.

**Url da requisição**: `http://127.0.0.1:8000/api/movies`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "title": "Revolver 4",
  "duration": "110min",
  "rating": "R",
  "synopsis": "Jake Green is a hotshot gambler, long on audacity and short on..."
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">201 CREATED</b> |

```json
{
	"id": 4,
	"title": "Revolver 4",
	"duration": "110min",
	"rating": "R",
	"synopsis": "Jake Green is a hotshot gambler, long on audacity and short on...",
	"added_by": "pedro@gmail.com"
}
```

### **GET - /movies/**

Rota de listagem de todos usuários.

**Url da requisição**: `http://127.0.0.1:8000/api/movies/`

| Resposta do servidor:                          |
| ---------------------------------------------- |
| Body: Formato Json                             |
| Status code: <b style="color:green">200 OK</b> |

```json
{
	"count": 4,
	"next": "http://127.0.0.1:8000/api/movies/?page=2",
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "Revolver 2",
			"duration": "110min",
			"rating": "R",
			"synopsis": "Jake Green is a hotshot gambler, long on audacity and short on...",
			"added_by": "silvia@gmail.com"
		},
		{
			"id": 2,
			"title": "Revolver 1",
			"duration": "110min",
			"rating": "R",
			"synopsis": "Jake Green is a hotshot gambler, long on audacity and short on...",
			"added_by": "silvia@gmail.com"
		}
	]
}
```

### **POST - /movies/:id/orders//**

Rota de criação de compra de filme.

**Url da requisição**: `http://127.0.0.1:8000/api/movies/1/order/`

| Dados de Envio:    |
| ------------------ |
| Body: Formato Json |

```json
{
  "price": 100.00
}
```

| Resposta do servidor:                               |
| --------------------------------------------------- |
| Body: Formato Json                                  |
| Status code: <b style="color:green">201 CREATED</b> |

```json
{
	"id": 3,
	"title": "Revolver 2",
	"price": "100.00",
	"buyed_by": "rafael@gmail.com",
	"buyed_at": "2023-07-26T12:01:22.803886Z"
}
```




