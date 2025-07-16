
# Smart Quiz Generator (with Hugging Face + GUI)

This is a Python-based quiz generator that creates multiple-choice questions on any topic using a large language model (LLM) from Hugging Face (`falcon-7b-instruct`). It saves the questions in both JSON and CSV formats, and allows you to answer them through a simple graphical interface (Tkinter).

---

## 📌 Features

- Generate 5 multiple-choice questions based on any topic
- Uses the Falcon-7B-Instruct model from Hugging Face
- Automatically saves questions in:
  - `quiz.json`
  - `quiz.csv`
- Simple GUI with score calculation (Tkinter)
- Terminal preview of generated questions

---

## 🧰 Requirements

Make sure you have Python 3.8 or newer installed.  
Install dependencies using:

```bash
pip install -r requirements.txt

requirements.txt

transformers==4.41.1
torch>=2.0.0
pandas
tk

> Note: On some systems, you may need to install Tkinter separately using your package manager:

Ubuntu: sudo apt install python3-tk

MacOS: Comes pre-installed

Windows: Comes with standard Python install





---

🚀 How to Run

python quiz_generator.py

1. A window will ask you to enter a topic (e.g., "machine learning", "space", "Shakespeare").


2. The app will generate 5 questions using Falcon-7B.


3. Questions will be displayed in the terminal and also shown one by one in a popup for answering.


4. Your final score will be displayed at the end.




---

🧪 Example Output

1. What is the capital of France?
a) Berlin
b) Madrid
c) Paris
d) Rome
Answer: c


---

📁 Output Files

quiz.json → structured version of questions/answers

quiz.csv → spreadsheet-ready version for Excel or Google Sheets



---

⚠️ Notes

The first few lines of the model's output (like formatting instructions) are filtered automatically.

This script uses do_sample=True, so results may vary slightly each time.

The model (falcon-7b-instruct) is large, so running it may take time or need a GPU / offloading.



---

📜 License

This project is for educational and personal use.


---

✨ Author

Created with ❤️ by Parisa Rahimzadeh

---

اگه خواستی بخش‌هایی مثل "Author", "License" یا توضیح درباره خودت رو اختصاصی‌تر کنم، کافیه بگی.  
همچنین اگه فایل رو به صورت آماده با اسم `README.md` بخوای، می‌تونم برات بسازم و آپلود کنم.

بگو دوست داری مرحله بعدی چیه؟ 😊
