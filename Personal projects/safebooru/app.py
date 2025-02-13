from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Función para obtener imágenes de Safebooru (con enlaces a cada imagen)
def get_safebooru_images(tag):
    url = f"https://safebooru.org/index.php?page=post&s=list&tags={tag}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    images = []

    # Buscar todas las imágenes en la página de resultados y sus enlaces
    for img in soup.find_all("a", {"class": "thumb"}):
        image_url = "https:" + img.find("img")["src"]
        post_url = "https://safebooru.org" + img["href"]
        images.append({"image": image_url, "link": post_url})

    return images[:10]  # Limitar a 10 imágenes

# Función para obtener imágenes de Deepbooru (con enlaces a cada imagen)
def get_deepbooru_images(tag):
    url = f"https://danbooru.donmai.us/posts?tags={tag}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    images = []

    # Buscar todas las imágenes en la página de resultados y sus enlaces
    for img in soup.find_all("a", {"class": "thumb"}):
        image_url = "https:" + img.find("img")["src"]
        post_url = "https://danbooru.donmai.us" + img["href"]
        images.append({"image": image_url, "link": post_url})

    return images[:10]  # Limitar a 10 imágenes

@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    error_message = None

    if request.method == "POST":
        tag = request.form.get("tag", "").strip().replace(" ", "_")
        if not tag:
            error_message = "Por favor, introduce un tag para buscar."
        else:
            # Buscar en ambas páginas
            safebooru_images = get_safebooru_images(tag)
            deepbooru_images = get_deepbooru_images(tag)
            
            images = safebooru_images + deepbooru_images
            if not images:
                error_message = "No se encontraron imágenes con ese tag."

    return render_template("index.html", images=images, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
