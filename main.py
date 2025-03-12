from flask import Flask, Response, send_from_directory, request

app = Flask('app', static_url_path='')

@app.route('/style.css')
def stylecss():
    return send_from_directory('.', path='style.css')

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Check if browser is Firefox-based or Chrome/Chromium-based
    is_firefox_based = 'firefox' in user_agent
    response = Response()
    formatted_html = ""
    if is_firefox_based:
        # Firefox: Use Link header
        response.headers['link'] = '<style.css>; rel=stylesheet;'
    else:
        # Chrome/Others: Use HTML link element
        formatted_html = "<html><head><link rel=\"stylesheet\" href=\"style.css\"></head></html>"
    
    response.data = formatted_html
    response.headers['Refresh'] = '5; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    return response

if __name__ == "__main__":
    print(0.1+0.2)  # This will output 0.30000000000000004
    app.run(host='0.0.0.0', port=80, debug=True)
