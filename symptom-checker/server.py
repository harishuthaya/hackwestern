# from flask import Flask, render_template
from flask import Flask, redirect, url_for, request, jsonify
from scraper import scrape_symptoms, scrape_factors, scrape_causes
app = Flask(__name__)

@app.route('/symptoms',methods = ['GET'])
def symptoms():
  data = scrape_symptoms()
  return jsonify(data)

#frontend needs to append '-adult' to end of symptom
@app.route('/relatedfactors',methods = ['GET'])
def relatedfactors():
  symptom = request.args.get('symptom')
  if not symptom:
    return jsonify({'error': 'symptom name not provided'})
  data = scrape_factors(symptom)
  return jsonify(data)
    
#frontend needs to append '-adult' to end of symptom
#factors should be strings separated by , (and no space after commas)
@app.route('/causes',methods = ['GET'])
def causes():
  symptom = request.args.get('symptom')
  factors = request.args.get('factors')
  if not symptom or not factors:
    return jsonify({'error': 'symptom name or factors not provided'})
  data = scrape_causes(symptom, factors)
  return jsonify(data)
    

if __name__ == '__main__':
  app.run(port=8000, debug = True)