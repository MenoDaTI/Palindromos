from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_palindromes(start, end):
    palindromes = [num for num in range(start, end + 1) if is_palindrome(num)]
    return palindromes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    start = int(request.form['start'])
    end = int(request.form['end'])
    palindromes = find_palindromes(start, end)
    return render_template('result.html', palindromes=palindromes, start=start, end=end)

if __name__ == '__main__':
    app.run(debug=True)

