from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image, ImageOps
import io

app = Flask(__name__)

SIZE_MAP = {
    "3x4": (354, 472),
    "4x6": (472, 709)
}

BG_COLOR_MAP = {
    "merah": (255, 0, 0),
    "biru": (0, 0, 255)
}

@app.route("/", methods=["GET", "POST"])
def index():
    hasil_url = None
    if request.method == "POST":
        ukuran = request.form.get("ukuran")
        warna = request.form.get("warna")
        foto = request.files.get("foto")

        if not foto or ukuran not in SIZE_MAP or warna not in BG_COLOR_MAP:
            return render_template("index.html", error="Mohon isi semua form dengan benar.")

        # Remove background
        input_bytes = foto.read()
        output_bytes = remove(input_bytes)

        # Buka image hasil remove bg
        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        # Ganti background
        bg_color = BG_COLOR_MAP[warna]
        background = Image.new("RGBA", img.size, bg_color + (255,))
        combined = Image.alpha_composite(background, img)

        # Resize
        target_size = SIZE_MAP[ukuran]
        final_img = combined.resize(target_size, Image.LANCZOS)

        # Simpan ke buffer
        buf = io.BytesIO()
        final_img.save(buf, format="PNG")
        buf.seek(0)

        return send_file(buf, mimetype="image/png", download_name=f"pasfoto_{ukuran}_{warna}.png", as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
