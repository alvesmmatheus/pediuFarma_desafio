# 🏥 PediuFarma JSON Generator

Este script em Python se conecta a um banco de dados MySQL, extrai dados de produtos (código de barras, preços, estoques e promoções), processa as promoções com base na data atual e gera um arquivo `.json` com os preços finais e estoque disponível para cada item.

## 📌 Funcionalidades
- Conexão com banco de dados MySQL (porta 3308)
- Verificação automática de promoções com base na data atual
- Geração de JSON formatado para integração com sistemas web/mobile
- Escrita em arquivo `pediuFarma.json`

## 🧠 Lógica de preço
- Se não houver promoção ativa, aplica o preço normal
- Se houver promoção ativa no dia atual, aplica o preço promocional

## 🔧 Exemplo de saída JSON
```json
[
  { "ean": 7890000000000, "preco": 1.99, "estoque": 38 },
  { "ean": 7890000000001, "preco": 3.99, "estoque": 18 }
]
```

## ▶️ Como rodar
1. Configure seu banco MySQL com os dados corretos
2. Instale o `mysql-connector-python`:
   ```bash
   pip install mysql-connector-python
   ```
3. Execute o script:
   ```bash
   python pediuFarma.py
   ```

---

## 👨‍💻 Autor
Matheus de Miranda – Engenheiro de Controle e Automação | ROV Analyst  
[LinkedIn](https://www.linkedin.com/in/matheus-de-miranda/)