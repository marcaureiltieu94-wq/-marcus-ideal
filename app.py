import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WHATSAPP = "0758664771"
LINK = "https://wa.me/225758664771"

PRODUCTS = [
    ("【entity-Chelsea¦canonical_name=Chelsea】 Domicile Bleu", 15000, "Best-seller"),
    ("【entity-Barca¦canonical_name=Barca】 Domicile Blaugrana", 16000, "Populaire"),
    ("【entity-Atletico Madrid¦canonical_name=Atletico Madrid】 Exterieur Gris", 15000, ""),
    ("【entity-Atletico Madrid¦canonical_name=Atletico Madrid】 Exterieur Gris V2", 15000, ""),
    ("【entity-Athletic Bilbao¦canonical_name=Athletic Bilbao】 Exterieur Noir-Rouge", 15500, "Edition Limitee"),
    ("【entity-Athletic Bilbao¦canonical_name=Athletic Bilbao】 Domicile Rouge-Blanc", 15000, ""),
    ("【entity-Liverpool¦canonical_name=Liverpool】 Domicile Rouge", 16000, "Best-seller"),
    ("OM Marseille Domicile Blanc-Bleu", 15000, ""),
    ("Pack OM Marseille 2 maillots", 28000, "Pack -20%"),
]

def cards():
    h = ""
    for i, (name, price, badge) in enumerate(PRODUCTS):
        h += f"""
        <div class='card'>
          <div class='img'>⚽ {name[:1]}</div>
          <div style='padding:14px'>
            <span style='font-size:12px;color:#666'>En stock - ★★★★★</span>
            <h3>{name}</h3>
            <p style='font-size:20px;font-weight:900'>{price:,} FCFA</p>
            <label>Taille <select id='s{i}'><option>S</option><option selected>M</option><option>L</option><option>XL</option><option>XXL</option></select></label><br><br>
            <label>Flocage Nom + N° (+2500)<br><input id='f{i}' placeholder='Ex: MARCUS 10'></label><br><br>
            <button class='add' onclick="add({i})">Ajouter au panier</button>
            <button class='wa' onclick="one({i})">Commander sur WhatsApp</button>
          </div>
        </div>"""
    return h

def page():
    return f"""<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
    <title>MARCUS IDEAL - 100% Maillots de Foot</title>
    <style>
    body{{margin:0;font-family:Arial;background:#f6f7f5}} header{{background:#0b1f14;color:#fff;padding:14px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}}
    .hero{{background:#0b1f14;color:#fff;padding:36px 16px;text-align:center}} .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;padding:16px;max-width:1100px;margin:auto}}
    .card{{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,.1)}} .img{{height:180px;background:#0b1f14;color:#fff;display:flex;align-items:center;justify-content:center;font-size:60px}}
    .add{{width:100%;padding:11px;border:0;border-radius:10px;background:#0b1f14;color:#fff;font-weight:800}} .wa{{width:100%;padding:11px;border:0;border-radius:10px;background:#25D366;color:#fff;font-weight:800;margin-top:8px}}
    .btn{{padding:10px 16px;border-radius:999px;text-decoration:none;font-weight:800;background:#25D366;color:#fff}}
    input,select{{width:100%;padding:9px;border:1px solid #ddd;border-radius:8px}}
    #cart{{display:none;position:fixed;right:10px;bottom:80px;width:min(380px,92vw);background:#fff;padding:16px;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.3);max-height:80vh;overflow:auto}}
    </style></head><body>
    <div style='background:#25D366;color:#fff;text-align:center;padding:8px;font-weight:700'>Livraison Abidjan & partout en Cote d'Ivoire - Paiement securise via WhatsApp</div>
    <header><div><b style='font-size:22px'>MARCUS <span style='color:#25D366'>IDEAL</span></b><br><small>100% MAILLOTS DE FOOT</small></div>
    <div>WhatsApp : <b>{WHATSAPP}</b> <a class='btn' href='{LINK}'>WhatsApp</a> <button class='btn' style='background:#fff;color:#111' onclick='toggle()'>Panier (<span id='c'>0</span>)</button></div></header>
    <div class
