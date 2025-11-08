# server.py
# Executar: pip install flask
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Credenciais "de exemplo"
VALID_USERNAME = "admin"
VALID_PASSWORD = "senha123"

LOGIN_HTML = """
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title>Login de Exemplo</title>
    <style>
      body { font-family: Arial, sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; background:#f2f2f2; }
      .card { background:white; padding:20px; border-radius:8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); width:320px; }
      input[type=text], input[type=password] { width:100%; padding:8px; margin:6px 0 12px; box-sizing:border-box; }
      button { width:100%; padding:8px; }
      .msg { margin-top:12px; color: #b00; }
      .success { color: green; }
    </style>
  </head>
  <body>
    <div class="card">
      <h2>Entrar</h2>
      <form method="post" action="{{ url_for('login') }}">
        <label>Usuário</label>
        <input type="text" name="username" placeholder="usuário" required autofocus>
        <label>Senha</label>
        <input type="password" name="password" placeholder="senha" required>
        <button type="submit">Login</button>
      </form>

      {% if message %}
        <div class="msg {{ 'success' if success else '' }}">{{ message }}</div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    # Mostra o formulário sem mensagem
    return render_template_string(LOGIN_HTML, message=None)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        msg = f"FLAG ENCONTRADA!!"
        return render_template_string(LOGIN_HTML, message=msg, success=True)
    else:
        msg = "Usuário ou senha incorretos. Tente novamente."
        return render_template_string(LOGIN_HTML, message=msg, success=False)

if __name__ == "__main__":
    # Rodar: python server.py
    # Acesse http://127.0.0.1:5000 no navegador
    app.run(host="0.0.0.0", port=5000, debug=True)
