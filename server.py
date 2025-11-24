from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Credenciais 
VALID_USERNAME = "admin"
VALID_PASSWORD = "vespascon{L1ttl3_fUn_0s1nT}"

LOGIN_HTML = """
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <style>
      body { 
        font-family: Arial, sans-serif; 
        display:flex; 
        align-items:center; 
        justify-content:center; 
        height:100vh; 
        background:#f2f2f2;
        margin: 0;
        padding: 0;
      }

      header {
        position: fixed;
        top: 0;
        width: 100%;
        background: #ffffff;
        padding: 10px 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        justify-content: center;
        gap: 25px;
        z-index: 10;
      }

      header img {
        height: 32px;
        width: 32px;
        transition: transform 0.2s ease;
      }

      header img:hover {
        transform: scale(1.15);
        cursor: pointer;
      }

      .card { 
        background:white;
        padding:20px;
        border-radius:8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 400px; 
        margin-top: 90px; /* evita sobreposição com o header */
      }

      h2 { 
        margin-top: 0; 
        text-align: center;
      }

      input[type=text],
      input[type=password] { 
        width:100%; 
        padding:12px; 
        margin:6px 0 12px; 
        box-sizing:border-box;
        font-size: 1rem;
      }

      button { 
        width:100%;
        padding:12px; 
        font-size:1rem;
        margin-top: 5px;
      }

      button:hover{
        cursor: pointer;
      }

      .msg { 
        margin-top:12px; 
        color: #b00; 
        text-align: center;
      }

      .success { 
        color:green; 
      }
    </style>

  </head>

  <body>

    <header>
      <a href="https://instagram.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png">
      </a>

      <a href="https://twitter.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png">
      </a>

      <a href="https://linkedin.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
      </a>
    </header>

    <div class="card">
      <h2>Entrar</h2>

      <form method="post" action="{{ url_for('login') }}">
        <label>Usuário</label>
        <input type="text" name="username" placeholder="usuário" required autofocus value="admin" autocomplete="off">
        <!--Não esquecer do usuário "admin"!! -->
        <label>Senha</label>
        <input type="text" name="password" placeholder="senha" required>

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
    return render_template_string(LOGIN_HTML, message=None)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        msg = f"FLAG ENCONTRADA!!"
        return render_template_string(LOGIN_HTML, message=msg, success=True)
    else:
        msg = "Senha incorreta. Tente novamente."
        return render_template_string(LOGIN_HTML, message=msg, success=False)
