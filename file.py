from flask import Flask, request, jsonify, render_template
import models

app = Flask(__name__)

homeworks = []

homework1 = models.Homework(
'Homework 1',
'This is the first homework.',
'Group A',
'https://example.com/image.png'
)

homework2 = models.Homework(
'Homework 2',
'This is the second homework.',
'Group B',
'https://example.com/image.png'
)

homework3 = models.Homework(
'Homework 3',
'This is the third homework.',
'Group C',
'https://example.com/image.png'
)

homeworks.append(homework1)
homeworks.append(homework2)
homeworks.append(homework3)


@app.route('/homework', methods=['GET', 'POST'])
def Homework():
    if request.method == 'GET':
        homework = homeworks[0]
        return render_template(
        'homework.html',
        homework=homework
        )
    elif request.method == 'POST':
        text = request.form.get('homework_text')
        return jsonify({
        'message': 'Text received',
        'homework_text': text
    }   ), 200


@app.route('/api/get_homework', methods=['POST'])
def get_homework():
    data = request.get_json()
    group = data.get('group')
    result = []
    for homework in homeworks:
        if homework.pinned_group == group:
            homework_dict = {
            'title': homework.title,
            'body': homework.body,
            'pinned_group': homework.pinned_group,
            'header_url': homework.header_url
        }
        result.append(homework_dict)
    return jsonify(result), 200



@app.route('/get_group', methods=['GET', 'POST'])
def get_group():
    result = []

    if request.method == 'POST':
        group = request.form.get('group')
        for homework in homeworks:
            if homework.pinned_group == group:
                result.append(homework)

    print(result)
    return render_template(
    'apihomework.html',
    homeworks=result
    )

if __name__ == '__main__':
    app.run(debug=True)
