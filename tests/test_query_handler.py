from src.query_handler import generate_answer

def test_answer_generation():
    context = ["This is a test context."]
    query = "What is this?"
    answer = generate_answer(context, query)
    assert isinstance(answer, str)
