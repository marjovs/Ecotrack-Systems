# 🌱 EcoTrack Systems API

Sistema desenvolvido em Python com Flask para monitoramento, 
análise e otimização do consumo de energia em setores de uma 
empresa.

---

## 📖 Sobre o projeto

Com o aumento do consumo de energia e a necessidade de práticas 
sustentáveis, esta API foi criada para auxiliar empresas a:

- Monitorar o consumo energético por setor
- Comparar consumo com metas sustentáveis
- Identificar desperdícios
- Gerar relatórios e estatísticas

---

## 🚀 Tecnologias utilizadas
- Python 
- Flask 
- SQLAlchemy 
- SQLite 

---

## ⚙️ Como executar

```bash
git clone https://github.com/SEU-USUARIO/api-ecotrack-systems.git
cd api-ecotrack-systems
python -m venv venv
venv\Scripts\activate
pip install flask sqlalchemy
python run.py
```

---

## 🌐 URL

```
http://127.0.0.1:5000
```

---

## 🔗 Endpoints

### Setores

* POST `/setores/`
* GET `/setores/`

### Consumos

* POST `/consumos/`
* GET `/consumos/`
* GET `/consumos/relatorio`
* GET `/consumos/acima-meta`
* GET `/consumos/estatisticas`

### Usuários

* POST `/usuarios/`
* GET `/usuarios/`
* GET `/usuarios/{id}`
* DELETE `/usuarios/{id}`
* POST `/usuarios/login`

---

## 📥 Exemplo

### Criar setor

```json
{
  "nome": "Administração",
  "meta_sustentavel": 500
}
```

---

## 🧠 Conceitos aplicados
- API REST
- Arquitetura em camadas (Controller, Service, Model)
- ORM com SQLAlchemy
- Validação de dados
- Boas práticas com Flask

---

## 👩‍💻 Autora

Projeto desenvolvido para fins acadêmicos.
