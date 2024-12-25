from flask import render_template

def render_data(data):
    """
    Render the fetched data using a template.
    """
    return render_template('index.html', data=data)
