# Django Async Views 🚀

Este projeto demonstra o uso de **views assíncronas** com Django e ASGI, utilizando `async def`, `asyncio`, e `httpx`. A aplicação responde imediatamente enquanto executa tarefas em segundo plano, simulando chamadas não bloqueantes.

---

## 🛠 Tecnologias

- Python 3.11+
- Django 4+
- Uvicorn (ASGI server)
- httpx (HTTP assíncrono)
- asyncio (execução paralela)

---

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/jrjunior72/async_views.git
   cd asyncviews
    ```

2. Crie e ative o ambiente virtual:

    bash
    ```
    python -m venv env
    source env/bin/activate  # ou .\env\Scripts\activate no Windows
    ```

3. Instale as dependências:

    bash
    ```
    pip install -r requirements.txt
    ```

4. Execute o servidor com Uvicorn:

    bash
    ```
    uvicorn asyncviews.asgi:application --reload
    ```

## 🧪 Testando a view assíncrona
Acesse no navegador:

http://127.0.0.1:8000/async_count/

### ➡️ Você verá a resposta imediata:

    json
    {
    "mensagem": "Contador finalizado",
    "valores": [1, 2, 3, 4, 5]
    }

Enquanto isso, o terminal exibirá a contagem em tempo real.

## 🤝 Contribuindo
Fork o projeto

Crie uma branch: git checkout -b minha-feature

Commit suas alterações: git commit -m "Adiciona nova feature"

Push para o repositório: git push origin minha-feature

Crie um Pull Request