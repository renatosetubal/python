import connection as conn

client = conn.retorna_conexao()
db = client.dbposts
col = db.posts

post1 = {
    'title': 'PHP',
    'content': 'CodeIgniter',
    'Versao': '7.4',
    'author': {
        'name': 'Renato Setúbal',
        'email': 'remiset@gmail.com'
    }
}
post2 = {
    'title': 'Java',
    'content': 'Conteúdo referente a awt',
    'level': 'Intermediário',
    'author': {
        'name': 'Craudio',
        'email': 'craudio@gmail.com'
    }
}

result = col.insert_one(post1)
result = col.insert_one(post2)
