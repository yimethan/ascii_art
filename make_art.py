from PIL import Image
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


class MakeArt():
    def __init__(self, image_path='test.jpg'):
        self.chars = ['$','#' ,'%','@','0','i','U','|','*','_','-',',','.',' ']
        
        self.image_path = image_path
        self.image = Image.open(self.image_path).convert('L')
        self.w, self.h = self.image.size
        
        self.width = 200
        self.height = int(self.h * self.width / self.w)


    def make_art(self):
        image = self.image.resize((self.width, self.height))
        
        pixels = image.getdata()
        pixels = [self.chars[pixel//19] for pixel in pixels]
        pixels =''.join(pixels)
        ascii_art = [pixels[i:i+self.width] for i in range(0, len(pixels), self.width)]
        ascii_art ='\n'.join(ascii_art)
        
        return ascii_art


@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        image_path = os.path.join('media', file.filename)
        file.save(image_path)
        ascii_art = MakeArt(image_path).make_art()
        os.remove(image_path)

        return jsonify({'ascii_art': ascii_art})

app.run(debug=True)