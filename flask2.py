from flask import Flask,request,jsonify

app=Flask(__name__)

book_list =[
    {
    "id":0,
   "author":"shyam",
   "language":"english",
   "title":"android robot",
},
 {
    "id":1,
   "author":"athul",
   "language":"english",
   "title":"gamer",
},
 {
    "id":2,
   "author":"vibin",
   "language":"tamil",
   "title":"916",
},
 {
    "id":3,
   "author":"souhrid",
   "language":"english",
   "title":"cyril boy",
},
 {
    "id":4,
   "author":"Adhish",
   "language":"malayalam",
   "title":"machine",
}]

@app.route('/books',methods =["GET","POST"])
def books():
    if request.method=="GET":
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            return "Nothing Found"
    if request.method=='POST':
        new_author = request.form['author']
        new_language=request.form['language']
        new_title=request.form['title']
        new_id=book_list[-1]['id']+1

        new={
            'id':new_id,
            'author':new_author,
            'language':new_language,
            'title':new_title
        }
        book_list.append(new)
        return jsonify(book_list),201

@app.route('/books/<int:id>',methods = ['GET','PUT','DELETE'])
def onebook(id):
    if request.method=='GET':
        for book in book_list:
            if book['id']==id:
                return jsonify(book)
            pass
    if request.method=='PUT':
        for book in book_list:
            if book['id']==id:
                book['author']=request.form['author']
                book['language']=request.form['language']
                book['title']=request.form['title']
                updated_book={
                    'id':id,
                    'author':book['author'],
                'language':book['language'],
                'title':book['title']
                }
                return jsonify(updated_book)

    if request.method == 'DELETE':
        for index,book in enumerate(book_list):
            if book['id']==id:
                book_list.pop(index)
                return jsonify(book_list)




@app.route('/bookstry',methods=['POST'])

def book():
    request_data = request.get_json()
    if request.method == 'POST':
        new_author = request_data['author']
        new_language = request_data['language']
        new_title = request_data['title']
        new_id = book_list[-1]['id'] + 1

        new = {
        'id': new_id,
        'author': new_author,
        'language': new_language,
        'title': new_title
            }
        book_list.append(new)
        return jsonify(book_list), 201



if __name__ == "__main__":
    app.run(debug=True)


