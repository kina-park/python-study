import requests
import html

params = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()  # 만약, 오류가 있다면 response가 예외를 생성하도록
question_data = response.json()["results"]
for question in question_data:
    question["question"] = html.unescape(question["question"])

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#]