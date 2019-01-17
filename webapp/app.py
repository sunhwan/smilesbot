import os
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO

from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/smiles/<smiles>')
def smiles(smiles):
    try:
        m = Chem.MolFromSmiles(smiles)
        img = BytesIO()
        Draw.MolToImage(m).save(img, 'png')
        img.seek(0)
        return send_file(img, mimetype='image/png')
    except:
        return 'error'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
