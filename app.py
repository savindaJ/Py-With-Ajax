from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

con = pymysql.connect(host='localhost', user='root', password='80221474', charset='utf8', db='thogakade')
cur = con.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def test_post():
    if request.method == 'POST':
        id = request.form['cusId']
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']
        print(id, name, address, salary)
        cur.execute("INSERT INTO customer (customerID, Name, address, salary) VALUES (%s, %s, "
                    "%s, %s)", (id, name, address, salary))
        con.commit()
        return jsonify({'state': "200"})
    else:
        return jsonify({'state': '404'})


@app.route('/delete', methods=['DELETE'])
def delete():
    print("delete")
    cur.execute("DELETE FROM customer WHERE customerID=%s", request.form['cusId'])
    con.commit()
    return jsonify({'state': "200"})


@app.route('/update', methods=['PUT'])
def update():
    print("update")
    id_data = request.form['cusId']
    name = request.form['name']
    address = request.form['address']
    salary = request.form['salary']
    cur.execute("""
                  UPDATE customer
                  SET Name=%s, address=%s,  salary=%s
                  WHERE customerID=%s
               """, (name, address, salary, id_data))
    con.commit()
    return jsonify({'state': "200"})


if __name__ == '__main__':
    app.run(
        host='127.0.0.1', port=5000, debug=True
    )
