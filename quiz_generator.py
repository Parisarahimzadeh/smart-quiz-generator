from transformers import pipeline
import pandas as pd
import json
import tkinter as tk
from tkinter import simpledialog, messagebox

# مدل Hugging Face
generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

# تولید سوالات
def generate_quiz(topic):
    prompt = (
        f"Create 5 multiple choice questions about {topic}.\n"
        "Each question should follow this exact format:\n"
        "1. Question?\n"
        "a) Option A\n"
        "b) Option B\n"
        "c) Option C\n"
        "d) Option D\n"
        "Answer: a\n\n"
        "Now generate:\n"
    )
    response = generator(prompt, max_length=1000, do_sample=True)[0]['generated_text']
    # فقط بخش بعد از "Now generate:" رو بگیر
    if "Now generate:" in response:
        response = response.split("Now generate:")[-1].strip()
    return response

# پردازش خروجی به لیست سوال
def parse_questions(raw_text):
    questions = []
    current = {}
    for line in raw_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit() and '.' in line:
            if current:
                questions.append(current)
                current = {}
            current['question'] = line
            current['options'] = []
        elif line.lower().startswith(("a)", "b)", "c)", "d)")):
            current['options'].append(line)
        elif 'answer:' in line.lower():
            current['answer'] = line.split(':')[-1].strip().lower()
    if current:
        questions.append(current)
    return questions

# ذخیره در json
def save_to_json(data, filename="quiz.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ذخیره در csv
def save_to_csv(data, filename="quiz.csv"):
    rows = []
    for q in data:
        rows.append({
            "Question": q.get('question', ''),
            "Option A": q['options'][0] if len(q['options']) > 0 else '',
            "Option B": q['options'][1] if len(q['options']) > 1 else '',
            "Option C": q['options'][2] if len(q['options']) > 2 else '',
            "Option D": q['options'][3] if len(q['options']) > 3 else '',
            "Answer": q.get('answer', '')
        })
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)

# نمایش سوالات و گرفتن پاسخ کاربر
def ask_questions_gui(questions):
    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        q_text = q['question'] + '\n' + '\n'.join(q['options'])
        answer = simpledialog.askstring(f"Question {i+1}", q_text + "\n\nYour answer (a/b/c/d):")
        if answer:
            if answer.strip().lower() == q['answer']:
                score += 1

    messagebox.showinfo("Result", f"You scored {score} out of {total}")
    print(f"\n🎯 Final Score: {score}/{total}")

# نمایش در ترمینال
def show_questions_terminal(questions):
    print("\n======= QUIZ QUESTIONS =======\n")
    for i, q in enumerate(questions):
        print(f"{i+1}. {q['question']}")
        for option in q['options']:
            print(option)
        print(f"Answer: {q['answer']}\n")
    print("==============================\n")

# اجرای اصلی
def main():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Smart Quiz Generator", "Quiz Generator (Hugging Face Edition)")
    topic = simpledialog.askstring("Enter Topic", "Please enter a topic for the quiz:")

    if not topic:
        messagebox.showerror("Error", "No topic entered. Exiting.")
        return

    try:
        raw_output = generate_quiz(topic)
        print("\nRaw AI Output:\n", raw_output)

        parsed = parse_questions(raw_output)

        if not parsed:
            messagebox.showerror("Error", "Failed to parse questions from AI output.")
            return

        save_to_json(parsed)
        save_to_csv(parsed)

        show_questions_terminal(parsed)       # نمایش در ترمینال
        ask_questions_gui(parsed)             # گرفتن پاسخ در محیط گرافیکی

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    main()