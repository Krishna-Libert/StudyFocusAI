from flask import Flask, render_template, request, make_response
from ai_engine import StudyAIEngine
import datetime

app = Flask(__name__)
ai = StudyAIEngine()

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    context = {
        "plan": None,
        "summary": None,
        "quiz": None,
        "keywords": None
    }
    
    if request.method == 'POST':
        # 1. Input Processing
        subject = request.form.get('subject')
        hours = request.form.get('hours')
        raw_notes = request.form.get('raw_notes')
        action = request.form.get('action')

        # 2. Logic Routing
        if action == "generate_plan" and subject and hours:
            context["plan"] = ai.generate_study_plan(subject, hours)
            context["subject"] = subject # Keep state
            
        elif action == "summarize" and raw_notes:
            context["summary"] = ai.summarize_text(raw_notes)
            context["keywords"] = ai.extract_keywords(raw_notes)
            
        elif action == "quiz" and subject:
            context["quiz"] = ai.get_quiz(subject)

    return render_template('dashboard.html', **context)

@app.route('/download/<type>')
def download_resource(type):
    # Generates a downloadable text file (Objectives requirement)
    output = f"StudentFocus AI Resource - {datetime.date.today()}\n"
    output += "------------------------------------------------\n\n"
    
    if type == "plan":
        output += "Your generated study plan is ready.\nFocus on deep work and take breaks."
    else:
        output += "Summary of your notes..."
        
    response = make_response(output)
    response.headers["Content-Disposition"] = f"attachment; filename=study_{type}.txt"
    return response

if __name__ == '__main__':
    app.run(debug=True)
