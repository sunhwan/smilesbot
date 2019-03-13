from flask import Flask
from flask import send_file

import os
from io import BytesIO

# avoid unicode encoding error
os.environ['RDK_NOPANGO'] = "1"

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions 

DrawingOptions.atomLabelFontSize = 55
DrawingOptions.dotsPerAngstrom = 100
DrawingOptions.bondLineWidth = 3.0

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
