from flask import Flask
import os
app = Flask(__name__)
PRODS = [
 ("【entity-Chelsea¦canonical_name=Chelsea】 Domicile Bleu", "15000"),
 ("【entity-Barca¦canonical_name=Barca】 Domicile Blaugrana", "16000"),
 ("【entity-Atletico Madrid¦canonical_name=Atletico Madrid】 Exterieur Gris", "15000"),
 ("【entity-Atletico Madrid¦canonical_name=Atletico Madrid】 Exterieur Gris V2", "15000"),
 ("Athletic Bilbao Exterieur Noir-Rouge", "15500"),
 ("Athletic Bilbao Domicile Rouge-Blanc", "15000"),
 ("Liverpool Domicile Rouge", "16000"),
 ("OM Marseille Domicile Blanc-Bleu", "15000"),
 ("Pack OM 2 maillots", "28000"),
]
@app.route("/")
def home():
    cards = ""
    for name, price in PRODS:
        msg = "Bonjour MARCUS IDEAL, je veux " + name + " - " + price + " FCFA"
        link = "https://wa.me/2250758664771?text=" + msg.replace(" ", "%20")
        cards += "<div style='border:1px solid #ddd;border-radius:12px;padding:12px;margin:10px;background:#fff'><h3>" + name + "</h3><p><b>" + price + " FCFA</b> - Tailles S M L XL XXL - Flocage +2500 FCFA</p><a href='" + link + "' style='display:block;background:#25D366;color:#fff;text-align:center;padding:10px;border-radius:8px;text-decoration:none;font-weight:bold'>Commander sur WhatsApp</a></div>"
    html = "<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>MARCUS IDEAL - 100% Maillots de Foot</title></head><body style='font-family:Arial;background:#f4f4f4;margin:0;padding:10px'><div style='background:#0b3d91;color:#fff;padding:20px;text-align:center;border-radius:12px'><h1>MARCUS IDEAL</h1><p>100% MAILLOTS DE FOOT - Abidjan</p><p>WhatsApp: 0758664771 - Orange Money / MTN MoMo / Wave / Espece</p></div><h2 style='text-align:center'>Nos 9 Maillots</h2>" + cards + "<p style='text-align:center'>Paiement Mobile Money au 0758664771 - MARCUS IDEAL, preuve sur WhatsApp. Pas de carte bancaire sur le site.</p></body></html>"
    return html
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
