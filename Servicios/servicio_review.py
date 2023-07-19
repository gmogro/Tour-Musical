import json
from Entidades.review import Review

class ServicioRutaVisita:

    def __init__(self):
        reviews = []
        try:
            with open("Persistencia/Reviews.json","r") as file:
                reviews_json = json.load(file)
            for data in reviews_json:
                reviews.append(Review.from_json(data))
        except Exception as error:
            with open("Persistencia/Reviews.json","w") as file:
                json.dump(reviews, file, indent=4)
        finally:
            self.reviews = reviews

    def crearReview(self,id_evento,id_usuario,califacion,comentario,animo):
        id = len(self.reviews) + 1 
        review = Review(id,id_evento,id_usuario,califacion,comentario,animo)
        self.reviews.append(review)
    
    def eliminarReview(self,review):
        self.reviews.remove(review)
    
    def buscarReview(self,id_review):
        for review in self.reviews:
            if review.id == id_review:
                return review
        return None
    
    def modificar(self,id_review,id_evento,id_usuario,califacion,comentario,animo):
        review = self.buscarReview(id_review)
        if not(review is None):
            review.id_evento = id_evento
            review.id_usuario = id_usuario
            review.califacion = califacion
            review.comentario = comentario
            review.animo = animo
        else:
            print("que no se encuentra la review")
    
    def finalizar(self):
        with open('Persistencia/Reviews.json', 'w') as f:
            reviews = []
            for review in self.reviews:
                reviews.append(review.to_json())
            json.dump(reviews, f, indent=4)
