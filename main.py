from treys import Card, Evaluator
from fastapi import FastAPI

app = FastAPI()
evaluator = Evaluator()

@app.get("/poker/check_it_please/")
def get_combination(hand: str):
    data = hand.split("-")
    board = []
    hand = [Card.new(card) for card in data]
    score = evaluator.evaluate(hand, board)
    handClass = evaluator.get_rank_class(score)
    return handClass