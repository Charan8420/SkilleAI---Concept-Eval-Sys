from flask import render_template, request, jsonify, Blueprint, flash
from .llm import question_extraction

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            text = file.read().decode('utf-8')
            questions = question_extraction(text)
            
            return render_template('index.html', questions = questions)
        
        else:
            flash('No file uploaded')
            return render_template('index.html')
    
    
    return render_template('index.html') # GET

