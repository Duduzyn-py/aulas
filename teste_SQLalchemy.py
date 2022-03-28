
class Casa(db.model):
	id = db.Columm(db.integer, primary_key = True)
	formato = db.Columm(db.string(254))
  quartos = db.relationship("Quarto", backref = 'casa')
  # cria autoaticamente a 'casa' na classe referida

	def __str__(self):
		return f'{self.id}, {self.formato}'
  
class Quarto(db.model):
	id = db.Columm(db.integer, primary_key = True)
	nome = db.Columm(db.string(254))
	dimensoes = db.Columm(db.string(224))
	casa_id = db.Columm(db.integer, db.foreignKey(Casa.id), nullable = False)
  #casa = db.relationship("Casa")

c1 = Casa(formato = 'Romana')
db.session.add(c1)
db.session.commit()
print(c1)

q1 = Quarto(nome = 'sala', dimensoes = "ss", casa = c1)
db.session.add(q1)
db.session.commit()
print(q1)

for q in c1.quartos:

print(q)
