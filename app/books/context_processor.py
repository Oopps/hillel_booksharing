from books import model_choises as mch


def model_choices_context(request):
    return {
        'mch': mch,
    }
