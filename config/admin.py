from books.models import Autor, Libro

def dashboard_callback(request, context):
    """
    Dashboard personalizado para Unfold.
    """
    total_autores = Autor.objects.count()
    total_libros = Libro.objects.count()

    context.update({
        "kpis": [
            {
                "title": "Total de Autores",
                "metric": total_autores,
            },
            {
                "title": "Total de Libros",
                "metric": total_libros,
            },
        ],
    })
    return context