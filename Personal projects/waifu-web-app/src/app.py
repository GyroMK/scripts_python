from flask import Flask, render_template, request
import asyncio
from waifuim import WaifuAioClient

app = Flask(__name__)

async def fetch_images(tags):
    async with WaifuAioClient() as wf:
        # Buscar imágenes con los tags dados (sin 'many=True')
        image = await wf.search(included_tags=[tags]) if tags else await wf.search()

        # Si no se encontró imagen, devolver None
        if not image:
            return None

        return image

@app.route("/", methods=["GET", "POST"])
def index():
    image, tags, error_message = None, [], ""

    if request.method == "POST":
        search_tag = request.form.get("tags", "").strip().lower()

        try:
            image = asyncio.run(fetch_images(search_tag))

            if image:
                tags = [tag.name for tag in image.tags]
            else:
                error_message = "No se encontraron imágenes con ese tag."

        except Exception as e:
            error_message = f"Error en la búsqueda: {e}"

    return render_template("index.html", image=image, tags=tags, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
